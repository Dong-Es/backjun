repeat= int(input())

for i in range(repeat):
    floor,room,customer = map(int,input().split())

    if customer%floor==0:
        print((floor*100)+(customer/floor))
    else:
        print(((customer%floor)*100)+(customer/floor)+1)
