marks=[90,10,25,67,45,80]

higher_list=[]

for i in marks:

  if i >= 50 and i>0:
    higher_list.append(i)

print(f"sum={sum(higher_list)}, avg={sum(higher_list)/len(higher_list)}")
