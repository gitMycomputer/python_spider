import socket
try:
    print(1/0)
except Exception as e:
    print("error::",e)
else:
    print("right")
finally:
    print("ok")


# 自定义异常
a="asda"
if(len(a)>6):
    ex=Exception("长度不能大于6")
    raise ex# 抛出异常