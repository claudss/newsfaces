#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:43:36 2018

@author: claudia
"""

import csv



#this code was used to grab all features that were in the updated anchor train/test files 


# this code was used to rearrange all the data from the updated_attribs csvs into different files.
"""
anchorrows = []
initrow = []

with open('updated_attribs_test.csv', 'r') as up:
    reader = csv.reader(up, delimiter=',')
    index = 0
    for row in reader:
        if (index > 0):
            if (int(row[45]) == 2):
                anchorrows.append(row)
        elif (index == 0):
            initrow = row
        index += 1

anchorrows.sort()

with open('grouped_ID/anchor_label_test.csv', 'w') as w:
    writer = csv.writer(w, delimiter=',')
    writer.writerow(initrow)
    for row in anchorrows:
        writer.writerow(row)
"""

# this code was used to grab all columns in the test/train set that were present in df_final.csv
"""
fullrows = []
subrows = []

newlabels = []

with open('df_final.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    index = 0
    for row in reader:
        if (index == 0):
            newlabels = row
        else:
            fullrows.append(row)
        index += 1

fullrows.sort()


with open('cropped_train-new.csv', 'r') as at:
    reader = csv.reader(at, delimiter=',')
    index = 0
    for row in reader:
        if (index > 0):
            subrows.append(row)
        index += 1
        
#subrows.sort()

newrows = []
for f in fullrows:
    for s in subrows:
        if (float(s[1]) == float(f[1]) and float(s[2]) == float(f[2]) and float(s[3]) == float(f[3]) and 
            float(s[4]) == float(f[4])):
            newr = [s[0]] + [s[1]] + f[2:] + [s[5]] + [s[6]]
            newrows.append(newr)

newrows.sort()
with open('updated_attribs_train.csv', 'w') as w:
    writer = csv.writer(w, delimiter=',')
    writer.writerow([''] + newlabels[1:] + ['Gender_Annotated'] + ['Race_Annotated'])
    for n in newrows:
        writer.writerow(n)
"""