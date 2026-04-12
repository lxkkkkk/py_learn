class Student:
    teacher='光头强'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'姓名：{self.name},年龄：{self.age}'
    
s1=Student('熊大',18)
s2=Student('熊二',17)

print(s1)
print(s2)

print(f'{s1.name}的老师：{s1.teacher}')
print(f'{s2.name}的老师：{s2.teacher}')

print('-'*90)

Student.teacher='翠花'
print(f'{s1.name}的老师：{s1.teacher}')
print(f'{s2.name}的老师：{s2.teacher}')

print('-'*90)

s1.teacher='诸葛亮'
print(f'{s1.name}的老师：{s1.teacher}')
print(f'{s2.name}的老师：{s2.teacher}')
print(f'Student的老师:{Student.teacher}')