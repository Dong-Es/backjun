class cat:
    def __init__(self,name="",color="",naw=""):
        self.name=name
        self.color=color
        self.naw=naw

    def __str__(self):
        return (f"cat name {self.name} car color{self.color} car sound{self.naw}")

    def meow(self):
        print(f'내 이름은{self.name}이고 색깔은 {self.color} 입니다. {self.naw}라고 울어요')

    def set_age(self, age): 
        if age > 0:
            self.__age = age
        else:
            self.__age = "Wrong value"
            
    def get_age(self):
        return self.__age

nabi.set_age(5)
print (nabi.get_age())

nero.set_age(-5)
print (nero.get_age())

mini.set_age(5)
print(mini.get_age())

nabi = cat("nabi","black","meow")
nabi.meow()
print(nabi)

nero = cat("nero","white","meow")
nero.meow()
print(nero)

mini = cat("mini","brown","meow")
mini.meow()
print(mini)


#self 자기를 호출하고 있는 객체 자신
