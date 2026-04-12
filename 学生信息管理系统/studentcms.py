from student import Student

class StudentCMS(object):
    def __init__(self):
        # 存储学生信息列表
        self.stu_list=[]

    # 打印界面
    def show_view(self):
        print('*'*90)
        print('学生信息管理系统')
        print('\t1.添加学生信息')
        print('\t2.删除学生信息')
        print('\t3.修改学生信息')
        print('\t4.查询单个学生信息')
        print('\t5.查询所有学生信息')
        print('\t6.保存学生信息')
        print('\t0.退出系统')
        print('*'*90)