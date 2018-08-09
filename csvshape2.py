
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 14:21:24 2018

@author: claudia
This file was made to put the prediction results of the model into a single file.
"""
import glob
import csv
import os
import shutil


index = 0
"""
for fname in glob.glob("cropped_train2/*"):
    test = str(fname).split("/")[1]
    folder = "cropped_train2/" + test.split(".")[0]
    #print(folder)
    os.makedirs(folder)
    shutil.move(fname, folder)
    index += 1

tomove= []
with open('reclassified/male_train_label.csv', 'r') as gr:
    reader = csv.reader(gr, delimiter=',')
    index = 0
    for row in reader:
        if (index > 0):
            tomove.append(row[0])
        index += 1
        

for fname in tomove:
    loc = 'cropped_train/' + fname
    shutil.copy(loc, "reclassified/male_train/")



"""
towrite = []

for fname in glob.glob("reclassified/results_male2/*.csv"):
    with open(fname, 'r') as featread:
        reader = csv.reader(featread, delimiter=',')
        index = 0
        for row in reader:
            if (index == 1):
                towrite.append([fname.strip('reclassified/results_female/').strip('.csv') + '.jpg'] + row[0:4])
            index += 1
    #print(fname.strip('results/').strip('.csv'))
towrite.sort()
with open('reclassified/male_pred2.csv', 'w') as resout:
#with open('predictionresults_train.csv', 'w') as resout:
    writer = csv.writer(resout, delimiter=',')
    writer.writerow(['', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact'])
    for row in towrite:
        writer.writerow(row)
"""


charrows = []
with open('characteristics.csv', 'r') as charread:
    reader = csv.reader(charread, delimiter=',')
    index = 0
    for row in reader:
        if (index > 0):
            charrows.append(row)
        index += 1
        
charrows.sort()

available = []
with open('cropped_test_label.csv', 'r') as gread:
    reader = csv.reader(gread, delimiter=',')
    index = 0
    for row in reader:
        if (index > 0):
            available.append(row)
        index += 1

available.sort()

finals = []
for crow in charrows:
    for row in available:
        if (crow[0] in row[0]):
            newrow = row + [crow[2]] + [crow[1]]
            finals.append(newrow)
            

finals.sort()

with open('cropped_test-new.csv', 'w') as newr:
    writer = csv.writer(newr, delimiter=',')
    writer.writerow(['', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact', 'Gender', 'Race'])
    for row in finals:
        writer.writerow(row)
"""