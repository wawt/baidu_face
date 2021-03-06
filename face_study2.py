# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 18:50:15 2018
https://blog.csdn.net/qq_26123853/article/details/79194139
@author: wutao
"""

# 利用baidu-aip库进行人脸识别  
import cv2  
from aip import AipFace  
import base64 
import os
  
  
def detection(APP_ID, API_KEY, SECRET_KEY, filename, maxnum):  
    ''''' 
 
    :param APP_ID: https://console.bce.baidu.com/ai/创建人脸检测应用对应的APP_ID 
    :param API_KEY: https://console.bce.baidu.com/ai/创建人脸检测应用对应的API_KEY 
    :param SECRET_ID: https://console.bce.baidu.com/ai/创建人脸检测应用对应的SECRET_ID 
    :param filename: 图片路径 
    :param maxnum: 最大检测数 
    :return: 
    '''  
    # 初始化AirFace对象  
    aipface = AipFace(APP_ID, API_KEY, SECRET_KEY)  
  
    # 设置  
    options = {  
        'max_face_num': maxnum,  # 检测人脸的最大数量  
        'face_fields': "age,beauty,expression,faceshape",  
    }  
  
    # 读取文件内容  
    def get_file_content(filePath):  
        with open(filePath, 'rb') as fp: 
            b64data = base64.b64encode(fp.read())        
            return b64data
    imageType = 'BASE64'
    result = aipface.detect(get_file_content(filename),imageType, options)  
    return result  
  
  
def result_show(filename, result):  
    ''''' 
 
    :param filename: 原始图像 
    :param result: 检测结果 
    :return: 
    '''  
    img = cv2.imread(filename)  
    face_num = result['result']['face_num']  
    for i in range(face_num):  
        location = result['result']['face_list'][i]['location']  
        left_top = (int(location['left']), int(location['top']))  
        right_bottom = (left_top[0] + location['width'], left_top[1] + location['height'])  
  #      cv2.rectangle(img, left_top, right_bottom, (200, 100, 0), 2)  
        cv2.rectangle(img, left_top, right_bottom, (0, 0, 255), 2)  
        cropImg = img[left_top[1]:right_bottom[1],left_top[0]:right_bottom[0]] #获取感兴趣区域
        [dirname,filestr]=os.path.split(filename)
        cv2.imwrite('Cut_'+str(i)+'_'+filestr,cropImg) #保存到指定目录
  
    cv2.imshow('img', img)  
    cv2.waitKey(0)  
  
  
if __name__ =='__main__':  
  
    # 定义APP_ID、API_KEY、SECRET_KEY  
    APP_ID = '11336667'  
    API_KEY = 'TfqQNm3O5QjWMbqPiB9hUmeV'  
    SECRET_KEY = 'Ey7oWgvbrUTY5LLfD1Keg16WP5QYO7kZ '  
  
    filename = 'test.jpg'  
    result = detection(APP_ID, API_KEY, SECRET_KEY, filename, 10)  
    result_show(filename, result)  