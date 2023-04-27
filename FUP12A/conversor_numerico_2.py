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
    n = str(n).upper()
    num = ''
    for i in n:
        if i.isalpha():
            i = ord(i) - ord('A') + 10
        else:
            i = int(i)
        num += decimaltoBinary(i)
    return num

def hexadecimaltoDecimal(n):
    n = str(n).upper()
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
    n = str(n).upper()
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

def octal(n, base):
    if base == '2':
        return octaltoBinary(n)
    elif base == '10':
        return octaltoDecimal(n)
    elif base == '16':
        return octaltoHexadecimal(n)
    
def hexadecimal(n, base):
    if base == '2':
        return hexadecimaltoBinary(n)
    elif base == '10':
        return hexadecimaltoDecimal(n)
    elif base == '8':
        return hexadecimaltoOctal(n)
    
def decimal(n, base):
    if base == '2':
        return decimaltoBinary(n)
    elif base == '16':
        return decimaltoHexadecimal(n)
    elif base == '8':
        return decimaltoOctal(n)

def binary(n, base):
    if base == '10':
        return binarytoDecimal(n)
    elif base == '16':
        return binarytoHexadecimal(n)
    elif base == '8':
        return binarytoOctal(n)

n = input("Digite o número a ser convertido: ")
base = input("Digite a base do número: ")
# baseconversao = input("Digite a base para conversão: ")
sistemas = [['binary', 'decimal', 'hexadecimal', 'octal'], ['2', '10', '16', '8']]
for i in range(4):
    bc = sistemas[0][i]
    basec = sistemas[1][i]
    if base != sistemas[1][i]:
        print(f'{bc:-<15} {eval(f"{bc}({n}, {basec})")}')
