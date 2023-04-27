import math
def decimalBinary(n):
    binary = []
    res = ''
    while(n>=1):
        binary.insert(0, (n%2))
        n//=2
    for i in range(len(binary)):
        res = res + str(binary[i])
    return res

def binaryDecimal(n):
    res = 0
    binary = str(n)
    j = -1
    for i in range(len(binary)):
        res += (int(binary[j]) * (2**i))
        j-=1
    return str(res)

def decimalOctal(n):
    octal = []
    res = ''
    while(n>=1):
        octal.insert(0, (n%8))
        n//=8
    for i in range(len(octal)):
        res = res + str(octal[i])
    return res

def decimalHex(n):
    hex = []
    resu = ''
    while(n>=1):
        hex.insert(0, (n%16))
        n//=16
    for i in range(len(hex)):
        d = hex[i]
        if d == 10:
            d2 = 'A'
            resu = resu + d2
        elif d == 11:
            d2 = 'B'
            resu = resu + d2
        elif d == 12:
            d2 = 'C'
            resu = resu + d2
        elif d == 13:
            d2 = 'D'
            resu = resu + d2
        elif d == 14:
            d2 = 'E'
            resu = resu + d2
        elif d == 15:
            d2 = 'F'
            resu = resu + d2
        else:
            resu = resu + str(hex[i])
    return resu

def binaryOctal(n):
    binary = str(n)
    tamanho = len(binary)
    blocos = math.ceil(tamanho/3)
    ind = -1
    res = []
    resultado = ''
    for i in range(blocos):
        strB = ''
        b = []
        for j in range(3):
            b.insert(0,int(binary[ind]))
            ind-=1
            if(abs(ind)>tamanho):
                while(len(b) < 3):
                    b.insert(0,0)
                break
        for k in b:
            strB = strB + str(k)
        res.insert(0, str(binaryDecimal(strB)))
    for k in res:
        resultado = resultado + str(k)
    return resultado

def binaryHex(n):
    binary = str(n)
    tamanho = len(binary)
    blocos = math.ceil(tamanho/4)
    ind = -1
    res = []
    resultado = ''
    for i in range(blocos):
        strB = ''
        b = []
        for j in range(4):
            b.insert(0,int(binary[ind]))
            ind-=1
            if(abs(ind)>tamanho):
                while(len(b) < 4):
                    b.insert(0,0)
                break
        for k in b:
            strB = strB + str(k)
        res.insert(0, str(decimalHex(int(binaryDecimal(strB)))))
    for k in res:
        resultado = resultado + str(k)
    
    return resultado
            
    # print(blocos)

def octalDecimal(n):
    octal = list(str(n))
    res = 0
    j = -1
    for i in range(len(octal)):
        res += (int(octal[j]) * (8**i))
        j-=1
    return str(res)

def octalHex(n):
    decimal = octalDecimal(n)
    hexa = decimalHex(int(decimal))
    return hexa

def octalBinary(n):
    octal = list(str(n))
    binaryV = []
    indice = len(octal)
    exp = 0
    res = []
    resultado = ''
    for i in range(-1, ((len(octal)+1) * -1), -1):
        l = decimalBinary(int(octal[i])).zfill(3)
        res.insert(0, l)
    for i in res:
        resultado = resultado + i
    return str(int(resultado))

def hexBinary(n):
    hex = list(str.upper(n))
    res = []
    resultado = ''
    for i in range(-1, ((len(hex)+1) * -1), -1):
        l = decimalBinary(int(hexletters(hex[i]))).zfill(4)
        res.insert(0, l)
    for i in res:
        resultado = resultado + i
    return str(int(resultado))

def hexDecimal(n):
    binary = hexBinary(str(n))
    decimal = binaryDecimal(int(binary))
    return decimal

def hexOctal(n):
    binary = hexBinary(str(n))
    octal = binaryOctal(int(binary))
    return octal

def hexletters(st):
    if st == 'A':
        return '10'
    elif st == 'B':
        return '11'
    elif st == 'C':
        return '12'
    elif st == 'D':
        return '13'
    elif st == 'E':
        return '14'
    elif st == 'F':
        return '15'
    else:
        return st

# print(binaryDecimal(11011000011))
# print(binaryOctal(1111111))
# print(binaryHex(1111111))
# print(decimalBinary(463))
# print(decimalOctal(127))
# print(decimalHex(127))
# print(octalDecimal(177))
# print(octalHex(177))
# print(octalBinary(177))
# print(hexBinary('7F'))
# print(hexDecimal('7F'))
# print(hexOctal('7F'))

print("*"*10+"CONVERSOR DE SISTEMAS NUMÉRICOS"+"*"*10+"\n"+"-"*51)

base = input('Digite a base do número a ser convertido: ')
numero = input('Digite o número a ser convertido: ')
conv = input('Digite para qual base deseja converter: ')
if(base == '2'):
    if(conv == '8'):
        res = binaryOctal(int(numero))
    elif(conv == '10'):
        res = binaryDecimal(int(numero))
    elif(conv == '16'):
        res = binaryHex(int(numero))
    else:
        res = "ERROR"
if(base == '8'):
    if(conv == '2'):
        res = octalBinary(int(numero))
    elif(conv == '10'):
        res = octalDecimal(int(numero))
    elif(conv == '16'):
        res = octalHex(int(numero))
    else:
        res = "ERROR"
if(base == '10'):
    if(conv == '2'):
        res = decimalBinary(int(numero))
    elif(conv == '8'):
        res = decimalOctal(int(numero))
    elif(conv == '16'):
        res = decimalHex(int(numero))
    else:
        res = "ERROR"
if(base == '16'):
    if(conv == '2'):
        res = hexBinary(numero)
    elif(conv == '8'):
        res = hexOctal(numero)
    elif(conv == '10'):
        res = hexDecimal(numero)
    else:
        res = "ERROR"

print("-"*51)
print(f"O resultado é: {res}")