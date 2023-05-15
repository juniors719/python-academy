print("Questão 7.1")
s1 = "AABBEFAATT"
s2 = "BE"
print(f"{s2} encontrado na posição {s1.find(s2)} de {s1}")

print("-"*50)

print("Questão 7.2")
s1 = "AAACTBF"
s2 = "CBT"
s3 = ""
for i in s2:
    if i in s1:
        s3 += i
print(s3)

print("-"*50)

print("Questão 7.3")
s1 = "CTA"
s2 = "ABC"
s3 = ""
for i in s2:
    if i not in s1:
        s3 += i
for i in s1:
    if i not in s2:
        s3 += i
print(s3)

print("-"*50)

print("Questão 7.4")
s1 = "TTAAC"
s2 = ""
for i in s1:
    if i not in s2:
        s2+=i
for i in s2:
    print(f"{i}: {s1.count(i)}x")

print("-"*50)

print("Questão 7.5")
s1 = "AATTGGAA"
s2 = "TG"
s3 = ""
for i in s1:
    if i not in s2:
        s3+=i
print(s3)

print("-"*50)

print("Questão 7.6")
s1 = "AATTCGAA"
s2 = "TG"
s3 = "AC"
s4 = ""
for i in s1:
    if i not in s2:
        s4 += i
    else:
        s4 += s3[s2.find(i)]
print(s4)


