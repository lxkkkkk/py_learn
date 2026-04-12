class Master:
    def __init__(self):
        self.kongfu='[古法配方]'
    
    def make_cake(self):
        print(f'使用{self.kongfu}做蛋糕！')

class School:
    def __init__(self):
        self.kongfu='[新式配方]'

    def make_cake(self):
        print(f'使用{self.kongfu}做蛋糕！')

class Prentice(School,Master):
    pass

p=Prentice()

p.make_cake()