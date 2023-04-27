a = int(input())
b = int(input())
c = int(input())
h = int(input())
l = int(input())
cabe = False

if a <= h:
    if b <= l or c <= l:
        cabe = True
if b <= h:
    if a <= l or c <= l:
        cabe = True
if c <= h:
    if b <= l or a <= l:
        cabe = True

if cabe:
    print("S")
else:
    print("N")