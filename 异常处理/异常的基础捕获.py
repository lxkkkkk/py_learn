f=None
try:
    f=open("./test.txt","r",encoding="utf-8")
except:
    f=open("./test.txt","w",encoding="utf-8")

print(f.read())
f.close()
