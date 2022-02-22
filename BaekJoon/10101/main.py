a=int(input())
b=int(input())
c=int(input())

plus=a+b+c

if plus == 180:
    if a==b==c:
        print("Equilateral")
    elif a==b or a==c or b==c:
        print("Isosceles")
    elif a!=b or a!=c or b!=c:
        print("Scalene")
else:
    print("Error")

