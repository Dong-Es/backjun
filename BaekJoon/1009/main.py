repeat = int(input())

for i in range(repeat):
    data,cpu = map(int,input().split())

    number= (data**cpu)%10

    print(number)
