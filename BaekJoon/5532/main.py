vacation= int(input())
math_page= int(input())
korean_page=int(input())
math_study=int(input())
korean_study=int(input())

math_day= math_page//math_study
korean_day= korean_page//korean_study

if math_page%math_study!=0:
    math_day += 1

if korean_page%korean_study!=0:
    korean_day += 1

print(vacation-max(math_day,korean_day))
    
