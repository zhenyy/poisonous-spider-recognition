import os
path = 'C:\\Users\\vincent916735\\Desktop\\poisonous-spider-recognition\\labelled_dataset\\Daddy Long Legs Spider\\'
f=os.listdir(path)
n=0
spider = 'Daddy Long Legs Spider_'
for i in f:
    oldname=path+f[n]    
    tail = i[len(i)-4:]
    print(oldname)
    print(tail)
    if tail == '.jpg':
        newname = path+spider+str(n)+tail
    elif tail =='.xml':
        newname = path+spider+str(n-1)+tail
    os.rename(oldname,newname)
    print(oldname,'======>',newname)
    n+=1
    