for i in range(3):
    test = int(input())
    number = [int(input()) for _ in range(test)]
    
    if sum(number) == 0:
        print(0)
    elif sum(number) > 0:
        print('+')
    else:
        print('-')
    
    
##이런식으로 하면 시간 초과 오류가 나온다

import sys
input = sys.stdin.readline

for i in range(3):
    test = int(input())
    number = [int(input()) for _ in range(test)]
    
    if sum(number) == 0:
        print(0)
    elif sum(number) > 0:
        print('+')
    else:
        print('-')
    
    
