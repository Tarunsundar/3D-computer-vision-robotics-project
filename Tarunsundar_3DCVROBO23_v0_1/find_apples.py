import csv

from io import FileIO
import os
import pandas as pd
import numpy as np
import seaborn as sns

if os.path.exists("cleaned_apples/")==False:
    os.makedirs("cleaned_apples/")
dirs = os.listdir('cleaned_apples/')

count = 0
num_apples=0
suffix=""
n = 0

def find_suffix(num_apples):
        if(num_apples==1):
            suffix="st"
        elif(num_apples==2):
            suffix="nd"
        elif(num_apples==3):
            suffix="rd"
        else:
            suffix='th'

def find_fruit_colour(content):
     #find if the fruit is white in colour
     if((content[4]<=255 and content[4]>=215)and(content[5]<=255 and content[5]>=215)and(content[3])<=255 and content[3]>215):
        return True
     #find if the fruit is red in colour
     elif((content[4]<=50 and content[4]>=0)and(content[5]<=50 and content[5]>=0)and(content[3])<=255 and content[3]>215):
        return True
     #find if the fruit is green in colour
     elif((content[4]<=255 and content[4]>=215)and(content[5]<=50 and content[5]>=0)and(content[3])<=50 and content[3]>0):
        return True
     #find if the fruit is yellow in colour
     elif((content[4]<=255 and content[4]>=215)and(content[5]<=50 and content[5]>=0)and(content[3])<=255 and content[3]>215):
        return True
     else:#else if we didn't find the apple's colour
         return False

if os.path.exists("found_apples/")==False:
    os.makedirs("found_apples/")

for n, item in enumerate(dirs, 1):
    filename='cleaned_apples/' +str(item)
    df = pd.read_csv(filename)
    for row, series, in df.iterrows():
        #print(df.col)
        v0 = float(df.series.str.split('').str[1])
        v1 = float(df.series.str.split('').str[2])
        v2 = float(df.series.str.split('').str[3])
        v3 = float(df.series.str.split('').str[4])
        v4 = float(df.series.str.split('').str[5])
        v5 = float(df.series.str.split('').str[6])
        volume = (4/3)*(22/7)*(((v0)**2)+((v1)**2)+((v2)**2)**1/2)**3
        print(volume)
        row= [v0,v1,v2,v3, v4, v5]
        found_a = find_fruit_colour(row) 
        count=+1
        if(volume>=60 and volume<=100) and found_a: 
            num_apples=+1
            find_suffix(num_apples)
            print("found the " + num_apples +suffix+ "apple!!")
            print("data of the found apple = " + row)
            found_apples = series
            found_apples.to_csv('found_apples/'+' found '+num_apples+suffix+' apple', index=False, header=False)
            break


