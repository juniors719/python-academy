# 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

nums = []

for i in range(3):
    nums.append(int(input()))

nums.sort()

print(f'{nums[0]} < {nums[1]} < {nums[2]}')