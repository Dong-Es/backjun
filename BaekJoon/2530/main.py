hour, minute, second= map(int,input().split())
plus_second = int(input())

second += plus_second%60
plus_second = plus_second// 60

if second > 59:
    second -= 60
    minute += 1

minute += plus_second%60
plus_second =  plus_second//60

if minute >59:
    minute -= 60
    hour += 1 
hour += plus_second% 24
if hour > 23:
    hour -= 24

print(hour,minute,second)    
