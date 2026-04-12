class Father:
    def __init__(self):
        self.gender='男'

    def walk(self):
        print('饭后走一走，活到九十九')

    def smoke(self):
        print('老子会抽烟!')

class Son(Father):
    pass

son=Son()
print(son.gender)
son.walk()
son.smoke()