f=open('./word.txt','r',encoding='utf-8')

cnt=0
for line in f.readlines():
    line=line.strip()
    for word in line.split(' '):
        if word=='it':
            cnt+=1

print(f'一共有{cnt}个it')

f.close()