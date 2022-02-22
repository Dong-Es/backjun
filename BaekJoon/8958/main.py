repeat=int(input())


for i in range(repeat):
    OXgame_list=list(input())
    score = 0
    result_score=0

    for ox in OXgame_list:
        if ox == 'O':
            score += 1
            result_score += score
        else:
            score = 0
    print(result_score)   
