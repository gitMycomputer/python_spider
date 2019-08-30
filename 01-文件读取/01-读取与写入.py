

# #fh表示为文件的句柄
fh1=open(r"C:\Users\PcUser\Desktop\text.txt","r")# 文件的读取
fh2=open(r"C:\Users\PcUser\Desktop\text.txt","w")# 文件的写入
fh3=open(r"C:\Users\PcUser\Desktop\text.txt","a")# 文件的追加
# data=fh1.read()
# ---------------“rb”读取二进制文件，“wb”写入二进制文件


# #会覆盖掉原有的数据，如果不存在则新建文件
fh2.write("asdasaaa12671")

data=fh1.readlines()
print(data)


# for i in range(1,10,2):
#     print(i)

for j in fh1:
    print(j)

fh1.close()

class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def est(self):
        print(self.name)

a=Dog("asd",12)
a.est()


