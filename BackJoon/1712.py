a,b,c = map(int,input().split())
#3개의 값을 입력
if b >= c:
    print(-1)

else:
    print(a//(c-b)+1)
    
