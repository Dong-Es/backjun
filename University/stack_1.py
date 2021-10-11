decimal=11
result=[]
while (decimal>0):
    remainder=decimal%2
    decimal=decimal//2
    result.append(str(remainder))

print(result)

while result:
    x=result.pop()
    print(x, end=' ')
