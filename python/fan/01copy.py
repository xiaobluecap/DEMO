from multiprocessing import Pool
import os
def copyFile(path1,path2):
    R=open(path1,'r')
    W=open(path2,'w')

    content=R.read()
    W.write(content)

    R.close()
    W.close()

path1=r'....'
path2=r'....'

fileList=os.listdir(path1)
pp=Pool(4)
for fileName in fileList:
    pp.apply_async(os.path.join(path1,fileName),os.path.join(path2,fileName))

pp.close()
pp.join()


