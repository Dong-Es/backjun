repeat = int(input())

for i in range(repeat):
    a,b=map(int,input().split())
    x,y=a,b
    while a!=0:
        b=b%a
        a,b=b,a
    gcd=b
    lcm=x*y//b
    print(lcm)
