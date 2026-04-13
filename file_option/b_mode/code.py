fr=open('./a/picture.png', 'rb')
fw=open('./b/picture.png','wb')

content=fr.read()
fw.write(content)

fr.close()
fw.close()