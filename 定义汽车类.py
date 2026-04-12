class Car:
    def run(self):
        print("汽车会跑......")
        print(f"我是run函数，self的值是{self}")


c1=Car()

print(f"c1对象：{c1}")
print(f"c1对象的地址值：{id(c1)}")

c1.run()

print("-" * 90)

c2=Car()

print(f"c2对象：{c2}")
print(f"c2对象的地址值：{id(c2)}")

c2.run()