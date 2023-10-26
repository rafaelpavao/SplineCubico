# README - Interpolação de Spline Cúbico

Este é um exemplo de código Python para interpolação de Spline Cúbico. Ele calcula os coeficientes de Splines Cúbicos com base em pontos de dados de entrada e os plota para criar uma curva suave que passa pelos pontos. Abaixo estão as etapas para executar o código e uma explicação do seu funcionamento.

## Passos para Executar o Código

1. **Instalação de Bibliotecas**

   Certifique-se de que você tenha as bibliotecas necessárias instaladas. Você pode usar o `pip` para instalar as dependências:

```bash
pip install numpy matplotlib
```



2. **Execute o Código**

Execute o código Python `spline_cubico.py`. Este arquivo contém o código necessário para calcular os Splines Cúbicos e gerar um gráfico.

```bash
python spline_cubico.py
```


Isso executará o código e gerará um arquivo "spline.pdf" contendo o gráfico das Splines Cúbicas.

3. **Visualize o Gráfico**

Abra o arquivo "spline.pdf" para visualizar o gráfico gerado. Ele mostrará as Splines Cúbicas que interpolam os pontos de dados originais.

[Visualize o Gráfico](spline.pdf)

## Explicação do Código

O código fornece uma implementação da interpolação de Spline Cúbico. Aqui está uma visão geral das principais partes do código:

- Importação das bibliotecas necessárias, incluindo NumPy para cálculos matemáticos e Matplotlib para plotagem.

- Definição da função `spline(x, y)` que calcula os coeficientes das Splines Cúbicas com base em pontos de dados de entrada. Os coeficientes são usados para criar as equações das Splines Cúbicas.

- Definição dos pontos de dados de entrada (X e Y).

- Cálculo das Splines Cúbicas usando a função `spline` e armazenamento das equações e domínios em um dicionário.

- Geração de gráficos para cada segmento de Spline Cúbico interpolado.

- Salvamento do gráfico em "spline.pdf" e exibição do gráfico.

## Por que uma Solução Automatizada para Splines?

Uma solução automatizada para Splines Cúbicos é útil porque simplifica o processo de interpolação. Em vez de calcular manualmente os coeficientes para cada segmento de spline, o código faz isso automaticamente, economizando tempo e evitando erros. Além disso, a plotagem automática dos splines oferece uma representação visual clara da interpolação, o que é útil em muitos contextos, como ajuste de curvas e análise de dados.


