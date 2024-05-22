# -*- coding: utf-8 -*-
"""3ª Prova de Probabilidade.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F5TXtSnNFtByhUZnrNBHWzKp2YX-q2Z6
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, expon, uniform, norm

def gerar_amostras(distribuicao, parametros, m, n):
    return distribuicao.rvs(size=(m, n), *parametros)

def plotar_histograma(data, titulo, xlabel, ylabel):
    plt.hist(data, bins=30, density=True, alpha=0.7)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def analisar_tcl(dist_name, dist_params, n, m):
    means = []

    for _ in range(m):
        samples = np.random.__getattribute__(dist_name)(*dist_params, size=n)
        sample_mean = np.mean(samples)
        means.append(sample_mean)

    plt.hist(means, bins=30, density=True, alpha=0.5, color='b', label='Médias Amostrais')

    mean_true = np.mean(means)
    std_true = np.std(means, ddof=1)
    x = np.linspace(min(means), max(means), 100)
    y = norm.pdf(x, mean_true, std_true)
    plt.plot(x, y, 'r-', label='Normal Teórica (Média e Desvio-Padrão Amostral)')

    standardized_means = (means - mean_true) / (std_true / np.sqrt(n))
    y_std = norm.pdf(x, 0, 1)
    plt.plot(x, y_std, 'g--', label='Normal Padronizada (0, 1)')

    print(f'Média Amostral para {dist_name.capitalize()}: {mean_true:.4f}')

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), fancybox=True, shadow=True, ncol=3)

    plt.title(f'TCL - {dist_name.capitalize()}')
    plt.xlabel('Valores')
    plt.ylabel('Densidade')
    plt.show()

# Solicita ao usuário os valores de n e m
n = int(input("Digite o valor de n (tamanho da amostra): "))
m = int(input("Digite o valor de m (número de amostras): "))

# (i) Binomial com p = 0.5
p = 0.5
binomial = binom(n, p)
amostras_binomial = gerar_amostras(binomial, (), m, n)
plotar_histograma(amostras_binomial.flatten(), 'Amostras - Binomial p = 0.5', 'Valores', 'Densidade')
medias_binomial = np.mean(amostras_binomial, axis=1)
plotar_histograma(medias_binomial, 'Médias Amostrais - Binomial p = 0.5', 'Valores', 'Densidade')
analisar_tcl('binomial', (n, p), n, m)

# (ii) Exponencial com lambda = 2
lmbda = 2
exponencial = expon(scale=1/lmbda)
amostras_exponencial = gerar_amostras(exponencial, (), m, n)
plotar_histograma(amostras_exponencial.flatten(), 'Amostras - Exponencial', 'Valores', 'Densidade')
medias_exponencial = np.mean(amostras_exponencial, axis=1)
plotar_histograma(medias_exponencial, 'Médias Amostrais - Exponencial', 'Valores', 'Densidade')
analisar_tcl('exponential', (lmbda,), n, m)

# (iii) Uniforme(a=0, b=1)
a, b = 0, 1
uniforme = uniform(loc=a, scale=b-a)
amostras_uniforme = gerar_amostras(uniforme, (), m, n)
plotar_histograma(amostras_uniforme.flatten(), 'Amostras - Uniforme', 'Valores', 'Densidade')
medias_uniforme = np.mean(amostras_uniforme, axis=1)
plotar_histograma(medias_uniforme, 'Médias Amostrais - Uniforme', 'Valores', 'Densidade')
analisar_tcl('uniform', (a, b-a), n, m)

