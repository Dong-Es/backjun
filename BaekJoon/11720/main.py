a=int(input())

## a_list 혼자만의 리스트를 생성
a_list=list(input()) 

result=0

## a_list안에 있는 적은 숫자들은 더하는 for문
for i in a_list:
    result += int(i)
print(result)    
