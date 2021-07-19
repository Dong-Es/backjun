#손익분기점 문제(BREAK -EVEN POINT)

a,b,c = map(int,input().split())
#3개의 값을 입력
if b >= c:
    print(-1)
#이익이 생기기 위해서는 c의 값이 b이상이 되어야합니다.
else:
    print(a//(c-b)+1)
    
