import sys
input=sys.stdin.readline

odd_number = []

for _ in range(7):
    a=int(input())

    if a%2 != 0:
        odd_number.append(a)

if odd_number:
    print(sum(odd_number))
    print(min(odd_number))
else:
    print(-1)

