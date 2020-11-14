import pandas as pd
import shutil
import os


csv="C:\\Users\\dostj\\Downloads\\trainLabels.csv"

filedir="D:\\dataset\\train"
def findByteFiles():#byte로 끝나는 파일 list로 저장
    dataFiles = os.listdir(filedir)
    dataFiles = list(filter(lambda x: x.endswith('.bytes'), dataFiles))
    return dataFiles

files=findByteFiles()
line_counter=0
with open(csv) as f :
    while 1:
        data=f.readline()
        if not data:break
        if line_counter==0 :#첫번째 줄
            header=data.split(",")
        else :
            arr=data.split(",")#csv파일
            arr[0]=arr[0].strip('"')
            arr[1]=arr[1].strip('\n')
            for file in files :#byte파일 하나씩 불러오기->f_name에 저장
                f_name=file.split('.')[0]
                if(arr[0]==f_name) : #csv,byte이름같으면
                    shutil.move(filedir+'\\'+file,filedir+'\\'+arr[1])#class로 이동시키기
        line_counter+=1

