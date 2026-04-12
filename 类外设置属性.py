class Car:
    def run(self):
        print('汽车会跑...')

c1=Car()
c1.run()

c1.color='red'
print(f'c1汽车的颜色：{c1.color}')

print('-'*80)

c2=Car()
c2.run()

c2.color='black'
print(f'c2汽车的颜色：{c2.color}')