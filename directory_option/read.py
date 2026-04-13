f=open('./hi.txt','r',encoding='UTF-8')

content=f.read(3)
print(content)

f.close()