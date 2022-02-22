first, second, third = map(int,input().split())
 
#3개의 주사위 던졌을 때 모든 숫자가 동일 할 때 
if first == second == third: 
    print(10000+1000*first)

#3개의 주사위 던졌을 때 2개의 숫자가 같을 때
elif first == second:
    print(1000+100*first)

elif first == third:
    print(1000+100*first)

elif second == third:
    print(1000+100*second)

#3개의 주사위 던졌을 때 3개의 숫자가 다 제각각 다를 때
else:
    print(100*max(first,second,third))
