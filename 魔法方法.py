class Car:
    def __init__(self,color):
        print('我是init方法，我自动调用了')

        self.color=color
    
    def __str__(self):
        return f'颜色：{self.color}'
    
    def __del__(self):
        print(f'{self}对象被删除了')

c1=Car('黄色')
print(c1)
del c1