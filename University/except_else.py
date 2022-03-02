temp = [3.6, 4.6, 3.3, -50, 5.2, 6.2]
total=0
wrong=0

for t in temp:
  try:
    if t < -10:
      wrong += 1
      raise ValueError
  except ValueError as e:
    pass
  else:
    total += t
print(total/len(temp) - wrong)    
