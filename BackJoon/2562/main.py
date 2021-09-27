a_list=[]

for i in range(9):
    a= int(input())
    a_list.append(a)
    
print(max(a_list))
print(a_list.index(max(a_list))+1)
