import os
import subprocess
directory=[]
directory.append('/home')
i=0
while i==0:
    opening=str(input())
    if opening.startswith("cancel"):
        i=1
    else:
        if opening.startswith("open"):
            op=opening.replace("open ","")
            if opening=="open" and directory[-1]=="/home":
                s=directory[0]
                list_of_files=os.listdir(s)
                print(s)
                print(list_of_files)
            else:
                op="/"+op
                directory.append(op)
                yes=''.join(directory)
                if os.path.isdir(yes):
                    print(yes)
                    list_of_files=os.listdir(yes)
                    print(list_of_files)
                else:
                    print("This is not a directory")
                    
        elif opening.startswith("go back"):
            retn=opening.split(" ")
            if retn[-2]=="to":
                x=retn[-1]
                x="/"+x
                y=directory.index(x)
                directory=directory[:y+1]
                retrn=''.join(directory)
                print(retrn)
                list_of_files=os.listdir(retrn)
                print(list_of_files)
            else:
                directory.pop(-1)
                back=''.join(directory)
                print(back)
                list_of_files=os.listdir(back)
                print(list_of_files)
        else:
            print("You Entered A Wrong Keyword")
    #to create new file
    if opening.startswith("create new"):
        op2=opening.replace("create new ","")
        new="/"+op2
        directory.append(new)
        file_path=''.join(directory)
        with open(file_path,"w") as f:
            con=str(input("Enter the content\n"))
            f.write(con)
            if con=="come out of write":
                pass
