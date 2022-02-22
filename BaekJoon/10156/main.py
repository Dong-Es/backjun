price,number,money=map(int,input().split())

need_money= price*number-money

if money >= price*number:
    print(0)
    
else:
    print(need_money)
