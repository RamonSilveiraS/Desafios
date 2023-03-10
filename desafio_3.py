# -*- coding: utf-8 -*-
"""desafio 3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aaXuwVt8X0q0oJTlnNFSFGT_EU_hSCI_

Suponha que você deseja precificar uma opção double digital, que paga um valor fixo se
o ativo subjacente estiver dentro de um determinado intervalo no vencimento. Escreva
um código em Python para calcular o preço teórico dessa opção, usando o modelo de
Black-Scholes. Os inputs devem ser: os preços atuais dos ativos subjacentes, os preços
de exercício da opção, a volatilidade, o tempo até o vencimento e a taxa livre de risco. O
output deve ser o preço teórico da opção.
"""

import math
from scipy.stats import norm

def double_digital_payoff(S, K1, K2):
    if S >= K1 and S <= K2:
        return 1
    else:
        return 0

def double_digital_price(S, K1, K2, v, T, r):
    d1 = (math.log(S/((K1 + K2)/2)) + (r + (v**2)/2)*T) / (v*math.sqrt(T))
    d2 = d1 - v*math.sqrt(T)
    
    price = S * norm.cdf(d1) - ((math.exp(-r*T)) * ((K2 - K1) * norm.cdf(d2)))
    return price


S = float(input("Preço atual do ativo subjacente: ")) # Preço atual do ativo subjacente
K1 = float(input("Preço de exercício inferior: ")) # Preço de exercício inferior
K2 = float(input("Preço de exercício superior: ")) # Preço de exercício superior
v = float(input("Volatilidade do ativo: ")) # Volatilidade
r = float(input("Taxa livre de risco: ")) # Taxa livre de risco
T = float(input("Tempo restante até o vencimento da opção (em anos): ")) # Tempo até o vencimento, em anos

PAYOFF = double_digital_payoff (S,K1,K2)
if PAYOFF == 1:
  preco_teorico = double_digital_price(S, K1, K2, v, r, T)  
  print("O preço teórico da opção é: ", preco_teorico)  
else:
  print('ERRO!! O valor subjacente tem que se encontrar no intervalo entre os valores do exercício inferior e superior.')