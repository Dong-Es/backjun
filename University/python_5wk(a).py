import random

lst =list(range(200))

data= random.sample(lst,100)

def search_key(arr,key):
    found = False
    for i, x in enumerate(arr):
        if x == key:
            found=True
            break
    if found:
        return i
    else:
        return -1

key= 50
pos = search_key(data,key)        
if pos != -1:
    print(data[pos])
else:
    print('not found')    
