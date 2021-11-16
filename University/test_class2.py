class calculator:
  def __init__(self,num1,num2):
    self.num1=num1
    self.num2=num2

  def setdata(self,num1,num2):
    self.num1=num1
    self.num2=num2

  def __str__(self):
    return (f"first number {self.num1} second number{self.num2}")

a=calculator(2,100)
print(a)
