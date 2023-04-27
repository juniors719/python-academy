def calculadora(num1,num2,op='+'):
    if op == '+':
        return n1+n2
    if op == '-':
        return n1-n2
    if op == '*':
        return n1*n2
    if op == '/':
        return n1/n2
    if op == '%':
        return n1%n2

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação: ")

print(calculadora(n1,n2,operacao))