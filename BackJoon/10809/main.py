s=input()
alphabet= list(range(97,123)) # 아스키코드 알파벳 범위

for i in alphabet:
    print(s.find(chr(i)))
