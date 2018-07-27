#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 14:21:24 2018

@author: claudia
This file was made to put the prediction results of the model into a single file.
"""
import glob
import csv

towrite = []

for fname in glob.glob("results/*.csv"):
    with open(fname, 'r') as featread:
        reader = csv.reader(featread, delimiter=',')
        index = 0
        for row in reader:
            if (index == 1):
                towrite.append([fname.strip('results/').strip('.csv') + '.jpg'] + row[0:4])
            index += 1
    #print(fname.strip('results/').strip('.csv'))
towrite.sort()
with open('predictionresults.csv', 'w') as resout:
#with open('predictionresults_train.csv', 'w') as resout:
    writer = csv.writer(resout, delimiter=',')
    writer.writerow(['', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact'])
    for row in towrite:
        writer.writerow(row)

"""
predimgs = []
for w in towrite:
    predimgs.append(w[0])

origfinal = []
with open('finalfinaltrain.csv', 'r') as wrout:
    reader = csv.reader(wrout, delimiter=',')
    for row in reader:
        origfinal.append(row)

finalwr= []
for name in towrite:
    if name[0] in predimgs:
        finalwr.append(name)
        
finalwr.sort()
        
with open('finalfinaltrain2.csv', 'w') as wrout:
    writer = csv.writer(wrout, delimiter=',')
    writer.writerow(['', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact'])
    for r in finalwr:
        writer.writerow(r)
"""