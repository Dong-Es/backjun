repeat= 3
sum_=0
for i in range(repeat):
    test = int(input())
    for _ in range(test):
        number = int(input())
        sum_ += number

    if sum_ == 0:
        print(0)
    elif sum_ > 0:
        print('+')
    else:
        print('-')
    
    
##이런식으로 하면 시간 초과 오류가 나온다
