hour, minute= map(int,input().split())

plus_time = int(input())

need_time = minute+plus_time

hour +=  need_time//60
minute = need_time%60

if hour > 23:
    hour -= 24

print(hour,minute)
