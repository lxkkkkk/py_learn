from 学生信息管理系统.student import Student

s=Student('1','1','1','1','1')
print(s)

my_dict=s.__dict__
print(my_dict)
print(type(my_dict))

s2=Student('2','2','2','2','2')
s3=Student('3','3','3','3','3')
s4=Student('4','4','4','4','4')
stu_dict=[s2,s3,s4]

list_dict=[stu.__dict__ for stu in stu_dict]
print(list_dict)

print('*'*80)

my_dict={'name':6,'gender':6,'age':6,'phone':6,'desc':6}
s6=Student(**my_dict)
print(s6)