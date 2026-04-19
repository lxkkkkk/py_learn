def f1():
    print('f1,start')
    1/0
    print('f1,end')

def f2():
    print('f2,start')
    f1()
    print('f2,end')

def main():
    f2()

try:
    main()
except Exception as e:
    print(e)