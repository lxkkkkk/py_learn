try:
    open('tet.txt','r')
except Exception as e:
    print('出现异常：',e)
else:
    print('没有异常')