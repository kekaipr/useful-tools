import numpy as np
import cv2
from glob import glob
import os 

current_path = os.getcwd()
before_path = os.path.join(current_path,"before")
after_path = os.path.join(current_path,'after')
img_list = os.listdir(before_path)

for i ,j in enumerate(img_list):
    name = before_path+'/'+ j
    img = cv2.imread(name)
    #加上黑色
    x=img.shape[1]##宽度
    y=img.shape[0]##高度
    add_array=np.zeros((x-y, x))
    add_array = np.expand_dims(add_array, axis=2) #把(222,323)變成(222,323,1)
    image1 = np.concatenate((add_array, add_array, add_array), axis=-1)#把[0,][0,][0,]變成[0,0,0]
    image_last = np.vstack((img, image1))#將原圖和黑圖疊起來
    cv2.imwrite(f'{after_path}'+'/'+j, image_last)