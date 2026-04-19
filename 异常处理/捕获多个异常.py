# try:
#     open("./test1.txt","r")
# except (ZeroDivisionError,FileNotFoundError) as e:
#     print("出现异常：",e)

try:
    open("./qqq.txt","r")
except ZeroDivisionError:
    print("除0了！")
except FileNotFoundError:
    print("文件没有找到！")