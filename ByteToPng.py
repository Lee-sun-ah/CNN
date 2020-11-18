import os.path
import numpy as np
import array
import math
import io
from PIL import Image

undecodedByte = 'FF'
filedir="D:\\dataset\\test"#***숫자수

def findByteFiles():
    dataFiles = os.listdir(filedir)
    dataFiles = list(filter(lambda x: x.endswith('.bytes'), dataFiles))
    return dataFiles

def bytestopng(f): #바이트를 이미지로 변환하기
    image_name = f.split('.')[0] #확장자 변경하기 위해 분리 이름.bytes
    #print(image_name)
    image_buf = filedir.split('\\') #경로설정하기 위해 분리 D:\\dataset\\train\\숫자
    image_name = image_buf[0] + '\\' + image_buf[1] + '\\' + image_buf[2]+'\\'+image_name + '.png'
    #print(image_name)

    if os.path.isfile(image_name): #파일이 이미 존재하면
        print('Image already exists: {}' .format(image_name))
        return

    b_data = array.array('i') #정수형signed int(i)
    for line in open('D:\\dataset\\test\\'+f, 'r'): #파일을 한 줄씩 읽기 모드로 연다.***숫자수정
        for byte in line[9:].split(): #맨앞의주소제거->split(공백을 기준으로 잘라 리스트로만들어 byte에 저장)
            if (byte == '??'): byte = undecodedByte
            b_data.append(int(byte, base=16)) # 16진수 형태로 배열(b_data)에 넣기

    width=math.ceil(math.sqrt(len(b_data)))
    height=width
    #print(height)
    #height = ceil(len(b_data) / width) #높이=b_data의 길이(배열 크기=총 바이트 수)/너비(width),ceil은 올림
    if len(b_data) < (width * height):
        b_data += array.array('i', (0,) * (width * height - len(b_data)))#i:signed int,남은개수만큼0채우기
    image_buffer = np.fromiter(b_data, dtype=np.uint8).reshape((height, width))#unit8:0~255양수

    img = Image.fromarray(image_buffer, 'L')#grayscale이미지로 변환
    #print(img.size)
    resize_image=img.resize((256,256))
    resize_image.save(image_name)
    os.remove("D:\\dataset\\test\\"+f)#***숫자수정
    #print(resize_image.size)
    
files=findByteFiles()

for file in files : 
    bytestopng(file)

