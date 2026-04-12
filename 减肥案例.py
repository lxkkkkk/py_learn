class Student:
    def __init__(self):
        self.curr_weight=100
    
    def run(self):
        print('跑步....')
        self.curr_weight-=0.5

    def eat(self):
        print('大吃大喝....')
        self.curr_weight+=2

    def __str__(self):
        return f'当前体重：{self.curr_weight}'
    
xm=Student()
print(xm)

xm.run()
print(xm)

xm.eat()
print(xm)