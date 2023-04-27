def binarytoDecimal(n):
    n = int(n)
    num = 0
    i = 0
    while n>=1:
        q = n%10
        n //= 10
        num += q*(2**i)
        i += 1
    return num

def binarytoHexadecimal(n):
    n = int(n)
    num = ''
    while n>=1:
        q = n%10000
        n //= 10000
        q = binarytoDecimal(q)
        if q >= 10:
            num = chr(ord('A') + q - 10) + num
        else:
            num = str(q) + num
    return num

def binarytoOctal(n):
    n = int(n)
    num = ''
    while n>=1:
        q = n%1000
        n //= 1000
        q = binarytoDecimal(q)
        num = str(q) + num
    return num

def decimaltoBinary(n):
    n = int(n)
    num = ''
    while n>=1:
        q = n%2
        n //= 2
        num = str(q) + num
    return num

def decimaltoHexadecimal(n):
    n = int(n)
    num = ''
    while n>=1:
        q = n%16
        n //= 16
        if q >= 10:
            num = chr(ord('A') + q - 10) + num
        else:
            num = str(q) + num
    return num

def decimaltoOctal(n):
    n = int(n)
    num = ''
    while n>=1:
        q = n%8
        n //= 8
        num = str(q) + num
    return num

def hexadecimaltoBinary(n):
    n = str(n)
    num = ''
    for i in n:
        if i.isalpha():
            i = ord(i) - ord('A') + 10
        else:
            i = int(i)
        num += decimaltoBinary(i)
    return num

def hexadecimaltoDecimal(n):
    n = str(n)
    num = 0
    i = 0
    for i in range(len(n)-1,-1,-1):
        if n[i].isalpha():
            q = ord(n[i]) - ord('A') + 10
        else:
            q = int(n[i])
        num += q*(16**i)
    return num

def hexadecimaltoOctal(n):
    n = str(n)
    num = ''
    for i in n:
        if i.isalpha():
            i = ord(i) - ord('A') + 10
        else:
            i = int(i)
        num += decimaltoOctal(i)
    return num

def octaltoBinary(n):
    n = int(n)
    num = ''
    while n>=1:
        q = n%1000
        n //= 1000
        q = binarytoDecimal(q)
        num = str(q) + num
    return num

def octaltoDecimal(n):
    n = int(n)
    num = 0
    i = 0
    while n>=1:
        q = n%10
        n //= 10
        num += q*(8**i)
        i += 1
    return num

def octaltoHexadecimal(n):
    n = int(n)
    num = ''
    while n>=1:
        q = n%1000
        n //= 1000
        q = binarytoDecimal(q)
        if q >= 10:
            num = chr(ord('A') + q - 10) + num
        else:
            num = str(q) + num
    return num

# print(binarytoDecimal(1010))
# print(binarytoHexadecimal(1010))
# print(binarytoOctal(1010))
# print(decimaltoBinary(10))
# print(decimaltoHexadecimal(10))
# print(decimaltoOctal(10))
# print(hexadecimaltoBinary('A'))
# print(hexadecimaltoDecimal('A'))
# print(hexadecimaltoOctal('A'))
# print(octaltoBinary(12))
# print(octaltoDecimal(12))
# print(octaltoHexadecimal(12))

n = input("Digite o número a ser convertido: ")
base = input("Digite a base do número: ")
if base == '2':
    print("Binário para Decimal: ", binarytoDecimal(n))
    print("Binário para Hexadecimal: ", binarytoHexadecimal(n))
    print("Binário para Octal: ", binarytoOctal(n))
elif base == '10':
    print("Decimal para Binário: ", decimaltoBinary(n))
    print("Decimal para Hexadecimal: ", decimaltoHexadecimal(n))
    print("Decimal para Octal: ", decimaltoOctal(n))
elif base == '16':
    print("Hexadecimal para Binário: ", hexadecimaltoBinary(n))
    print("Hexadecimal para Decimal: ", hexadecimaltoDecimal(n))
    print("Hexadecimal para Octal: ", hexadecimaltoOctal(n))
elif base == '8':
    print("Octal para Binário: ", octaltoBinary(n))
    print("Octal para Decimal: ", octaltoDecimal(n))
    print("Octal para Hexadecimal: ", octaltoHexadecimal(n))