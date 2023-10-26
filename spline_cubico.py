# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define a function 'spline' to calculate cubic spline coefficients
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

    # RESOLVE N SISTEMAs DE QUAÇÕES USANDO NUMPY E SALVA EM DICIONARIO c
    c = dict(zip(range(n), np.linalg.solve(A, B)))

    # INICIALIZANDO DICIONARIO DE COEFICIENTES B E D
    b = {}
    d = {}

    # Calculate 'b' and 'd' coefficients for each segment
    for k in range(n - 1):
        b[k] = (1 / h_xdiff[k]) * (y_dict[k + 1] - y_dict[k]) - (h_xdiff[k] / 3) * (2 * c[k] + c[k + 1])
        d[k] = (c[k + 1] - c[k]) / (3 * h_xdiff[k])

    # Initialize a dictionary 's' to store the spline equations and their domains
    s = {}
    for k in range(n - 1):
        # Construct the spline equation as a string
        equacao = f'{y_dict[k]}{b[k]:+}*(x{-x[k]:+}) {c[k]:+}*(x{-x[k]:+})**2 {d[k]:+}*(x{-x[k]:+})**3'
        s[k] = {'equacao': equacao, 'dominio': [x[k], x[k + 1]]}

    return s

# Define data points (X and Y)
X = [2, 25, 40, 90, 110, 140, 165, 180, 198, 212, 215, 220, 223, 225, 226.5, 228.5, 230, 235, 240, 245, 248, 251, 254, 258]
Y = [50, 65, 70, 75, 75, 74, 72, 70, 69, 78, 78, 78, 78, 78, 78, 62, 60, 58, 56, 52, 54, 52, 54, 50]

# Calculate the spline equations for the given data
equacoes = spline(X, Y)

# Print the spline equations and their domains
print("     Segments: ")
for key, value in equacoes.items():
    equation_str = value['equacao']
    domain_str = f"Domain: [{value['dominio'][0]}, {value['dominio'][1]}]"
    print(f'Segment {key} - {domain_str}\nEquation: {equation_str} \n')

# Iterate through each spline segment and plot them
for key, value in equacoes.items():
    # Define a function 'p(x)' that evaluates the spline equation
    def p(x):
        return eval(value['equacao'])
    
    # Generate a range of x-values within the domain of the spline segment
    t = np.linspace(*value['dominio'], 100)
    
    # Plot the spline curve
    plt.plot(t, p(t), label=f'$S_{key}(x)$')

im = plt.imread('image.png')
im = np.flipud(im)
implot = plt.imshow(im) 

# Scatter plot the original data points
plt.scatter(X, Y)

# Set axis limits for the plot
plt.axis([0, 270, 0, 190])

# Save the plot as "spline.pdf"
plt.savefig("spline.png")

# Display the plot
plt.show()
