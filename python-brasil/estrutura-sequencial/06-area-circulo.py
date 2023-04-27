# 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input("Digite o raio do círculo: "))

pi = math.pi

# Fórmula área círculo:
#  pi * raio**2

area = pi * (raio**2)

print(f"Área do Círculo: {area:.2f}")