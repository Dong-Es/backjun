import sys

n= int(input())
result = 0

for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    result = a+b
    print(result)
