min_guk= list(map(int,input().split()))
man_se= list(map(int,input().split()))

S = sum(min_guk)
T = sum(man_se)

if S == T:
    print(S)
else:
    print(max(S,T))
