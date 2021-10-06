def fun(x):
    return x*2

result=list(map(fun,[5,4,3,2,1]))
print(result)            

result2=list(map(lambda x:x*2,[5,4,3,2,1]))
print(result2)
