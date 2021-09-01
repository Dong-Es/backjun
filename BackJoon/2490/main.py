for i in range(3):
    play=[]
    play=list(map(int,input().split()))

    if play.count(0)==1:
        print('A')
    elif play.count(0)==2:
        print('B')    
    elif play.count(0)==3:
        print('C')
    elif play.count(0)==4:
        print('D')
    else:
        print('E')
