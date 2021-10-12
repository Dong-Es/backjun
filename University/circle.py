line = input("input numbers")
numbers=line.split()
total=0
for x in numbers:
    total = total+int(x)

print(f'sum = {total}')    
