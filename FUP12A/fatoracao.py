n = int(input())
i = 2
exp = 0
nota = 3.333333
while(n>=1):
    exp = 0
    while(n%i==0):
        n/=i
        exp+=1
    if(exp>0):
        print(i, exp)
    i+=1
    if(n==1):
        break
print(f"{nota:.2f}")