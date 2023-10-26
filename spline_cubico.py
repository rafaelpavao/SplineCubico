import numpy as np
import matplotlib.pyplot as plt

def spline(x, y):
    """
    Retorna todos os coeficientes de todos os polinomios
    ou seja, todos ak, bk, ck, dk
    """
    # QUANTIDADE DE PONTOS
    n = len(x)

    # CRIA DICIONARIO COM VALORES DE Y E SEUS INDICES
    y_dict = {k: v for k, v in enumerate(y)}

    # CALCULA DIFERENCA ENTRE COORDENADAS X DOS PONTOS H[n] => X[n+1] - X[n]
    h_xdiff = {k: x[k + 1] - x[k] for k in range(n - 1)}

    # INICIALIZA MATRIZ DE COEFICIENTES
    A = [[1] + [0] * (n - 1)]

    # CALCULA COEFICIENTES E INSERE NA MATRIZ
    for i in range(1, n - 1):
        row = [0] * n
        row[i - 1] = h_xdiff[i - 1]
        row[i] = 2 * (h_xdiff[i - 1] + h_xdiff[i])
        row[i + 1] = h_xdiff[i]
        A.append(row)

    # FINALIZA A ULTIMA LINHA DA MATRIZ COM A[n][n] = 1 E O RESTO 0
    A.append([0] * (n - 1) + [1])

    # INICIALIZA ARRAY DE TERMOS INDEPENDENTES
    B = [0]

    # CALCULA TERMOS INDEPENDENTES E ADICIONA NO ARRAY
    for k in range(1, n - 1):
        row = (3 * (y_dict[k + 1] - y_dict[k]) / h_xdiff[k]) - (3 * (y_dict[k] - y_dict[k - 1]) / h_xdiff[k - 1])
        B.append(row)

    B.append(0)

    # RESOLVE N SISTEMAS DE EQUAÇÕES USANDO NUMPY E SALVA EM DICIONARIO  DE COEFICIENTES c
    c = dict(zip(range(n), np.linalg.solve(A, B)))

    # INICIALIZANDO DICIONARIO DE COEFICIENTES B E D
    b = {}
    d = {}

    # CALCULA COEFICIENTES b E d PARA CADA N
    for k in range(n - 1):
        b[k] = (1 / h_xdiff[k]) * (y_dict[k + 1] - y_dict[k]) - (h_xdiff[k] / 3) * (2 * c[k] + c[k + 1])
        d[k] = (c[k + 1] - c[k]) / (3 * h_xdiff[k])

    # INICIALIZA DICIONARIO s O QUAL GUARDA N EQUAÇÕES E SEUS RESPECTIVOS DOMINIOS
    s = {}
    for k in range(n - 1):
        # CONSTROI EQUAÇÃO COMO UMA STRING
        equacao = f'{y_dict[k]}{b[k]:+}*(x{-x[k]:+}) {c[k]:+}*(x{-x[k]:+})**2 {d[k]:+}*(x{-x[k]:+})**3'
        s[k] = {'Equacao': equacao, 'Dominio': [x[k], x[k + 1]]}

    return s

# DEFINE PONTOS
X = [2, 25, 40, 90, 110, 140, 165, 180, 198, 212, 215, 220, 223, 225, 226.5, 228.5, 230, 235, 240, 245, 248, 251, 254, 258]
Y = [50, 65, 70, 75, 75, 74, 72, 70, 69, 78, 78, 78, 78, 78, 78, 62, 60, 58, 56, 52, 54, 52, 54, 50]

# CALCULA EQUAÇÕES PARA PONTOS ACIMA
equacoes = spline(X, Y)

# MOSTRANDO CADA EQUAÇÃO E SEUS DOMINIOS
print("     Segmentos: ")
for key, value in equacoes.items():
    equation_str = value['Equacao']
    domain_str = f"Dominio: [{value['Dominio'][0]}, {value['Dominio'][1]}]"
    print(f'Segmento {key} - {domain_str}\Equacao: {equation_str} \n')

# ITERA DENTRO DE N EQUAÇÕES PARA N SEGMENTOS DE CURVA
for key, value in equacoes.items():
    # DEFINE A FUNÇÃO 'p(x)' A QUAL RESOLVE EQUAÇÃO N
    def p(x):
        return eval(value['Equacao'])
    
    # SALVA EM t O LIMITE DE X PARA A PLOTAGEM N ( DOMINIO )
    t = np.linspace(*value['Dominio'], 100)
    
    # PLOTANDO CURVA PARA EQUAÇÃO N
    plt.plot(t, p(t), label=f'$S_{key}(x)$')

# COLOCANDO IMAGEM NO FUNDO
im = plt.imread('image.png')
im = np.flipud(im)
implot = plt.imshow(im) 

# INSERINDO PLOTAGEM COMPLETA DOS PONTOS ORIGINAIS
plt.scatter(X, Y)

# LIMITANDO AS COORDENADAS DE X E Y PARA MELHOR VIZUALIZAÇÃO DA PLOTAGEM
plt.axis([0, 270, 0, 190])

# SALVA PDF DO GRÁFICO
plt.savefig("spline.png")

# MOSTRAR GRÁFICO
plt.show()
