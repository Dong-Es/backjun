#값어치가 가장 싼 세트-50 할인

a= 2000
c= 2000

for i in range(3):
    b= int(input())
    a= min(a,b)
    # 위에서 a의 최댓값은 2000으로 해놓았고 b에서 입력한 3개의 숫자 중 1개가 저장되게 하였다.
    
for i in range(2):
    b= int(input())
    c= min(c,b)
    # 위에서 c의 최댓값은 2000으로 해놓았고 d에서 입력한 2개의 숫자 중 1개가 저장되게 하였다.

print(a+c-50)
