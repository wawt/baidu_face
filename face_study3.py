# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 17:49:54 2018

@author: wutao
"""

from aip import AipFace
import base64 
import shutil,os

import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np



APP_ID = '11336667'
API_KEY = 'TfqQNm3O5QjWMbqPiB9hUmeV'
SECRET_KEY = 'Ey7oWgvbrUTY5LLfD1Keg16WP5QYO7kZ'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)



def get_file_content(filepath):
    with open(filepath, 'rb') as fp:
        b64data = base64.b64encode(fp.read())        
        return b64data

def analysis(filepath):    
    [dirname,filename]=os.path.split(filepath)
    image = get_file_content(filepath)
    print ('image')
    imageType = 'BASE64'
    # 定义参数变量  
    options = {  
        'max_face_num': 1,  
        'face_field': "age,beauty,expression,faceshap",  
        } 
    r = client.detect(image, imageType, options)

    try:
      for i in r['result']['face_list']:
#        print (i['beauty'])
        print('{} 颜值 {} 优秀 {} 年龄'.format(filename,i['beauty'],i['age']))
        if i['beauty']>=80:           
           shutil.copy(filepath,"./best")
           lena = mpimg.imread(filepath) # 读取和代码处于同一目录下的 lena.png
           # 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
 #          lena.shape #(512, 512, 3)

           plt.imshow(lena) # 显示图片
           plt.axis('off') # 不显示坐标轴
           plt.show()

    except:
        print(filename+ ' no face')

    
dir = './pic/'
if os.path.exists(dir):
#    print ('dir exists')
    pass
else:
    print ('no exists')

best = './best/'
if os.path.exists(best):
#    print ('dir exists')
    pass
else:
    os.mkdir(best)

    
if os.path.exists(dir):
    dirs = os.listdir(dir)
    for dirc in dirs:
        if os.path.isfile(dir+ dirc) :
            analysis(dir+dirc)
    
#            print (dir+dirc)
else:
    print ("dir not exists")
