# 221230 Junwoo Park
import pandas as pd
import shutil
import os

# Requirements:
## 1. a brainwave folder with backup folders from each EEG station
## 2. CSV file consisting file names for the samples used in experiments

station_name = os.listdir('C:/Users/user/Desktop/brainwave_221229')[:-1]
# makes a list of station folder names (e.g q1n6_(2022_12_28_12h_38m)
folder_names = ['na', 'nf', 'ni', 'np', 'nr', 'ns', 'nt']
# default backup folder elements found under 'data' folder
dict = {}

for i in station_name:
    os.mkdir('C:/Users/user/Desktop/brainwave_221229/%s/db_fx/newdata' % i)
    # make 'newdata' folder and each data folders under the directory
    for j in folder_names:
        os.mkdir('C:/Users/user/Desktop/brainwave_221229/%s/db_fx/newdata/%s' % (i, j))
        # making blank folder under 'newdata'
        filelist = [f for f in os.listdir('C:/Users/user/Desktop/brainwave_221229/%s/db_fx/data/%s' % (i, j))]
        dict['%s%s' % (i, j)] = filelist
        # Key = 'station name' + 'folder name'
        # Value = a list of filenames for each folder
        ## e.g (dict[q1n10_(2022_12_28_13h_22m)ni] = 'niat.has')

total = pd.read_csv("C:/Users/user/Desktop/total.csv")['Name'].tolist()
# experiment sample list


for i in station_name:
    for j in folder_names:
        for p in dict['%s%s' % (i, j)]:
            if p in total:
                shutil.copy('C:/Users/user/Desktop/brainwave_221229/%s/db_fx/data/%s/%s' % (i, j, p),
                            'C:/Users/user/Desktop/brainwave_221229/%s/db_fx/newdata/%s' % (i, j))
                # copy if filename matches 'total' list
            elif p == '%sat.has' % j:
                shutil.copy('C:/Users/user/Desktop/brainwave_221229/%s/db_fx/data/%s/%s' % (i, j, p),
                            'C:/Users/user/Desktop/brainwave_221229/%s/db_fx/newdata/%s' % (i, j))
                # copy 'XXat.has' files to the folder (necessary)
            else:
                pass
                # pass for mismatches