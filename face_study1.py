# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 17:49:54 2018

@author: wutao
"""

from aip import AipFace
import base64 

APP_ID = '11336667'
API_KEY = 'TfqQNm3O5QjWMbqPiB9hUmeV'
SECRET_KEY = 'Ey7oWgvbrUTY5LLfD1Keg16WP5QYO7kZ'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

img1='1601.jpg'
img2='2.jpg'
img3='3.jpg'
img4='4.jpg'
img5='5.jpg'

url_dict = {'a':img1, 'b':img2, 'c':img3, 'd':img4, 'e':img5}

def get_file_content(filepath):
    with open(filepath, 'rb') as fp:
        b64data = base64.b64encode(fp.read())        
        return b64data
    
for key, value in url_dict.items():
    image = get_file_content(value)
    imageType = 'BASE64'
    # 定义参数变量  
    options = {  
        'max_face_num': 1,  
        'face_field': "age,beauty,expression,faceshap",  
        } 
    r = client.detect(image, imageType, options)
#    print (r['result'])
#    print (r['result']['face_list'])
#    print ('=============================')
    
    for i in r['result']['face_list']:
#        print (i['beauty'])
     #   if i['beauty']>=60:
           print('{} 颜值 {} 优秀 {} 年龄'.format(key,i['beauty'],i['age']))

    
#    for i in r['result']:
#        print (i['face_list'])
#        beauty = (i['beauty'])
#        if beauty>=90:
 #           print('{} 颜值 {} 优秀'.format(key,i['beauty']))
