fr=open('./bill.txt','r',encoding='utf-8')
fw=open('./bill.txt.bak','w',encoding='utf-8')

for line in fr.readlines():
    line=line.strip()
    if '测试'==line.split(',')[-1]:
        continue

    fw.write(line+'\n')

fr.close()
fw.close()