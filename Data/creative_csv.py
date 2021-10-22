import pandas as pd
import sys
import os
from os import listdir
import glob

origin_cwd = os.getcwd()

#dataset path
path= 'G:\download\SEN12MS-CR'
os.chdir(path)

file_list = listdir(path)
 # ['spring_', 'summer_', 'fall_', 'windter_']
file_list_py = [file for file in file_list if file.endswith("_")]

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

f = open('datasetfilelist.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)

# 1	s1	s2_cloudFree	s2_cloudy	ROIs1158_spring_101_0.tif
for name in new_set_names : 
    wr.writerow(['1	s1	s2_cloudFree	s2_cloudy	' + name])

f.close()
