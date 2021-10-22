import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from os import rename, listdir
import os
import glob

origin_cwd = os.getcwd()

#dataset path
path= 'G:\download\SEN12MS-CR'
os.chdir(path)

file_list = listdir(path)
 # ['spring_', 'summer_', 'fall_', 'windter_']
file_list_py = [file for file in file_list if file.endswith("_")]

# "이미지 전체 glob"
cwd = path
image_names = []

for folder in file_list_py:
    os.chdir(cwd)
    cwd2 = cwd + '\\' + folder
    os.chdir(cwd2)
    
    file_list2 = listdir(cwd2)
    # ['s1', 's2', 'cludly'] 
    file_list_py2 = [file for file in file_list2 if file.endswith("_")]

    cwd3 = cwd2 + '\\' + file_list_py2[0]
    os.chdir(cwd3)
    glob_files2 = (glob.glob('*'))
    for folder2 in glob_files2:
        os.chdir(cwd3)
        cwd4 = cwd3 + '\\' + folder2
        os.chdir(cwd4)
        images = (glob.glob('*'))
        for img in images: iamge_names = image_names.append(img)
                
new_set_names = [x.replace('_s1', '').replace('_p', '_') for x in image_names]

os.chdir(origin_cwd)
# csv_path & read_csv
tes = pd.read_csv("origin_datasetfilelist.csv", header=None)#, delimiter='\t', names=['A'])
# tes = tes[tes['Index'] !=3] ; tes = tes[tes['Index'] !=2] ; tes = tes[tes['Index'] !=1]

# 1	s1	s2_cloudFree	s2_cloudy	ROIs1158_spring_101_0.tif
for name in new_set_names : 
    new_data ={
    '0' : '1	s1	s2_cloudFree	s2_cloudy	' + name
    }
    tes = tes.append(new_data, ignore_index=True)

tes.to_csv("datasetfilelist.csv", mode='w', index=False)

## 초기 값 삭제 후 자리 변경하면 됩니다.