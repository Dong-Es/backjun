while(True):
    try:
        a,b =  map(int,input().split())

        X= a*b

        if b%a ==0:
            print("factor")
        elif a%b==0:
            print("multiple")
        else :
            print("neither")
    except:
        break
