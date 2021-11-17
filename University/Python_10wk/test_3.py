try:
  b=2/0
  a=1+'hundred'
except ZeroDivisionError:
  print('0으로 나누는 오류')  
except TypeError:
  print('지원되지 않은 연산자를 사용하는 오류')  
except Exception as e:
  print('error:',e)  
  
  #먼저 오류난 애는 b=2/0이므로 0으로 나누는 오류가 출력된다.
