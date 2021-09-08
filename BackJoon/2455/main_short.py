Station_people=[]
people = 0

for i in range(4):
    people_out,people_in=map(int,input().split())
    people += people_in
    people -= people_out
    Station_people.append(people)

print(max(Station_people))    
