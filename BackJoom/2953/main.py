team =[]
for i in range(5):
    team.append(sum(map(int,input().split())))
print(team.index(max(team))+1,max(team))

