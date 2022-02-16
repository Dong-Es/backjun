repeat= int(input())

for i in range(repeat):
    cpu,data = map(int,input().split())
    
    number = cpu%10

    if number==0: ## 0인의 경우 10이 출력
        print(10)
    elif number == 1 or number == 5   or number==6: ## 1,5,6는 밑수가 같다
        print(number)
    elif number == 4 or number == 9: ##4,9 는 두 값이 반복된다.
        data= data%2
        if data== 1:
            print(number)
        else:
            print((number*number)%10)
    else: ##2,3,7,8 일 경우 어떤 지수든 4개의 값이 반복
        data= data%4
        if data == 0:
            print((number**4)%10%10%10)
        else:
            print((number**data)%10%10%10)

##    repeat = int(input())
##    for i in range(repeat):
##          data,cpu = map(int,input().split())
##    number= (data**cpu)%10
##    print(number)
##  이 코드를 사용했을 경우 수가 높아지면 시간이 비효율적으로 사용이 된다.

##1,5,6 같은 경우는 지수가 어떤 값이든 밑수가 같다. 
##4,9 는 두 값이 반복된다.
##2,3,7,8 일 경우 어떤 지수든 4개의 값이 반복되는데
##지수가 4의 배수라면 cpu^4 한값과 같 듯이
##나머지들도 cpu^1 cpu^2 cpu^3 한 값과 동일 합니다
##다만 지수를 4로 나눈 나머지를 적용시키면 런타임 오류가 발생하기 때문에 출력 값에 4를 직접 나누기 연산하도록 합니다.            

