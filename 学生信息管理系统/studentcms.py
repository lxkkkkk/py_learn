from student import Student
import time

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
        print() #空行隔开

    def add(self):
        name=input('请输入学生姓名：')
        age=int(input('请输入学生年龄：'))
        gender=input('请输入学生性别：')
        phone=input('请输入学生电话：')
        desc=input('请输入学生描述信息：')

        self.stu_list.append(Student(name,age,gender,phone,desc))

        print(f'添加{name}学生信息成功！')

    def delete(self):
        del_name=input('请输入要删除的学生姓名：')
        flag=False
        for stu in self.stu_list:
            if stu.name==del_name:
                self.stu_list.remove(stu)
                print(f'学员{del_name}信息删除成功')
                flag=True
                break
        if not flag:
            print('查无此人，请检查后重新删除')


    def update(self):
        upd_name = input('请输入要修改的学生姓名：')
        flag = False
        for stu in self.stu_list:
            if stu.name == upd_name:
                stu.gender=input('请输入新的性别：')
                stu.age=input('请输入新的年龄：')
                stu.phone=input('请输入新的电话号码：')
                stu.desc=input('请输入新的描述：')

                print(f'学员{upd_name}信息修改成功')
                flag = True
                break
        if not flag:
            print('查无此人，请检查后重新修改')

    def query(self):
        query_name = input('请输入要查找的学生姓名：')
        flag = False
        for stu in self.stu_list:
            if stu.name == query_name:
                print(stu)
                flag = True
                break
        if not flag:
            print('查无此人，请检查后重新查找')

    def query_all(self):
        if len(self.stu_list)==0:
            print('暂无学生信息，空的')
        else:
            for stu in self.stu_list:
                print(stu)
            print('学生信息打印完毕')

    def save(self):
        try:
            with open('./stu_data.txt', 'w') as dest_f:
                stu_dict = [stu.__dict__ for stu in self.stu_list]
                dest_f.write(str(stu_dict))
                print('保存学生信息成功')
        except:
            with open('./stu_data.txt', 'w') as dest_f:
                pass

    def load(self):
        with open('./stu_data.txt','r') as source_f:
            stu_data=source_f.read()
            stu_list=eval(stu_data)
            if len(stu_list)==0:
                stu_list=[]
            self.stu_list=[Student(**stu_dict) for stu_dict in stu_list]

    def start(self):
        self.load()
        while True:
            time.sleep(1)
            self.show_view()
            print('='*80)
            input_num=input('请输入您要操作的编号：')
            if input_num=='1':
                print('添加学生信息\n')
                self.add()
            elif input_num=='2':
                print('删除学生信息\n')
                self.delete()
            elif input_num=='3':
                print('修改学生信息\n')
                self.update()
            elif input_num=='4':
                print('查询单个学生信息\n')
                self.query()
            elif input_num=='5':
                print('查询所有学生信息\n')
                self.query_all()
            elif input_num=='6':
                print('保存学生信息\n')
                self.save()
            elif input_num=='0':
                res=input('您确定要退出吗？(请先确认已经保存信息)（y/n）')
                if res.lower()=='y':
                    print('退出系统，谢谢您的使用\n')
                    break
                elif res.lower()=='n':
                    print('你弄错了啊，继续用吧老登！')
                else:
                    print('录入有误！请重新输入\n')
            else:
                print('录入有误！请重新输入\n')


if __name__=='__main__':
    s=StudentCMS()
    s.start()