f=open('./hi.txt','r',encoding='UTF-8')

# content=f.read(3)
# print(content)

# lst=f.readlines()
# print(lst)
# print(type(lst))

# for line in f.readlines():
#     line=line.strip()
#     print(line)

print(f.readline().strip())
print(f.readline().strip())
print(f.readline().strip())


f.close()