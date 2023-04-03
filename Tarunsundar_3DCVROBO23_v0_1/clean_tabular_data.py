import os
import pandas as pd

dirs = os.listdir('some_apples/')
print(len(dirs))

if os.path.exists("cleaned_apples/")==False:
    os.makedirs("cleaned_apples/")

count = 0

for n, item in enumerate(dirs, 1):
    filename=str(item)
    apple_example= pd.read_csv('some_apples/' + filename, sep= ' ' ,names= ['x', 'y', 'z', 'r', 'g', 'b','unk1','unk2','unk3', 'x1','y1','z1'])
    count=+1
    apple_truncated=apple_example[['x','y','z','r','g','b']]
    headerList = ['x','y','z','r','g','b']
    apple_truncated.to_csv('cleaned_apples/'+filename, sep= ' ' , index=True, columns=headerList)
