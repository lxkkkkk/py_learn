class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('汪汪！')

class Cat(Animal):
    def speak(self):
        print('喵喵！')

d=Dog()
c=Cat()

def make_noise(an):
    an.speak()

make_noise(d)
make_noise(c)