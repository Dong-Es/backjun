for i in range(2,10):
    for x in range(2,i):
        if i%x ==0:
            print (i, 'is not Prime Number')
            break
    else:
     print(i,'is Prime Number')
