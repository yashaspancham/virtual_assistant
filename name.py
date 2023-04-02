import glob
import v1
name=str(input().split(" "))
x=glob.glob('your*')
y=' '.join(x)
if((name.find(y)+1)!=0 or (name.find("name")+1)!=0 or (name.find("call")+1)!=0 (name.find("speaking")+1)!=0):
    print("My Name is Mr.Baahu!!What help do you need??")
else:
    pass