try:
    1/0
except Exception as e:
    print('有异常：',e)
else:
    print('没有异常')
finally:
    print('不管有没有啥的异常，我都执行')