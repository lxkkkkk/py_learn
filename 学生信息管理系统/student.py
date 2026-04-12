class Student:
    def __init__(self,name,gender,age,phone,desc):
        self.name=name
        self.gender=gender
        self.age=age
        self.phone=phone
        self.desc=desc

    def __str__(self):
        return f'学生信息--姓名：{self.name},性别：{self.gender},年龄：{self.age},电话号码：{self.phone},描述：{self.desc}'
    
if __name__ == '__main__':
    s=Student('李新科','男',25,'12345678','丐帮帮主')
    print(s)