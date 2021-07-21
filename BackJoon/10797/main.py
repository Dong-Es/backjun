#10부제 문제 (10797)

day= int(input())
#먼저 10부제의 숫자를 적는다.

car= list(map(int,input().split()))
#차 번호를 입력하여 리스트에 저장한다.

print(car.count(day))
#10부제와 차번호가 일치하면 위반 자동차의 대수를 출력한다.
          
