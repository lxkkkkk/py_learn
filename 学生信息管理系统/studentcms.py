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
        print() #空行隔开

    def add(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def query(self):
        pass

    def query_all(self):
        pass

    def save(self):
        pass

    def load(self):
        pass

    def start(self):
        while True:
            self.show_view()
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
                res=input('您确定要退出吗？（y/n）')
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