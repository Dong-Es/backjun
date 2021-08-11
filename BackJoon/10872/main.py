#팩토리얼(10872)
# 팩토리얼 함

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(int(input())))

#factorial이란 (5!=5*4*3*2*1)
