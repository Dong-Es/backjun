a=int(input())

for i in range(a):
    repeat,word=input().split()
    for x in word:
        print(x*int(repeat),end='')
    print()
