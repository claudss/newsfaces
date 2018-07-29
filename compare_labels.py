#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 21:44:13 2018

@author: claudia
"""

import sklearn.metrics as m
import sklearn.preprocessing as pp
import csv
import scipy.stats as stats
import numpy as np

comparison = []
predrecall = []
predposrat = []
predperfrat = [] 
predimpact = []
truerecall = []
trueposrat = []
trueperfrat = []
trueimpact = []
names = []

with open('finalfinaltest.csv', 'r') as labelread:
#with open('finalfinaltrain2.csv', 'r') as labelread:
    reader = csv.reader(labelread, delimiter=',')
    index = 0
    for row in reader:
        if (index > 0):
            names.append(row[0])
            
            truerecall.append(float(row[1]))
            trueposrat.append(float(row[2]))
            trueperfrat.append(float(row[3]))
            trueimpact.append(float(row[4]))
        index += 1
print("NAME AMOUNT: " + str(len(names)))
names2 = []
with open('predictionresults.csv', 'r') as featread:
#with open('predictionresults_train.csv', 'r') as featread:
    reader = csv.reader(featread, delimiter=',')
    index = 0
    count = 0
    for row in reader:
        if (index > 0 and row[0] in names):
            predrecall.append(float(row[1]))
            predposrat.append(float(row[2]))
            predperfrat.append(float(row[3]))
            predimpact.append(float(row[4]))
            count += 1
        index += 1
    print("COUNT: " + str(count))
    print("INDEX: " + str(index))
    #print(fname.strip('results/').strip('.csv'))
"""
names2.sort()
for name in names2:
    print(name)
"""

        
print("RECALL MEAN SQUARED ERROR: " + str(m.mean_squared_error(truerecall, predrecall)))
print("POSITIVE RATING MEAN SQUARED ERROR: " + str(m.mean_squared_error(trueposrat, predposrat)))
print("PERFORMANCE RATIO MEAN SQUARED ERROR: " + str(m.mean_squared_error(trueperfrat, predperfrat)))
print("IMPACT MEAN SQUARED ERROR: " + str(m.mean_squared_error(trueimpact, predimpact)))
print("-------------")


truerecall_norm = pp.normalize([truerecall])
trueposrat_norm = pp.normalize([trueposrat])
trueperfrat_norm = pp.normalize([trueperfrat])
trueimpact_norm = pp.normalize([trueimpact])

predrecall_norm = pp.normalize([predrecall])
predposrat_norm = pp.normalize([predposrat])
predperfrat_norm = pp.normalize([predperfrat])
predimpact_norm = pp.normalize([predimpact])

print("SAMPLE RECALL NORMALIZED MEAN SQUARED ERROR: " + str(m.mean_squared_error(truerecall_norm[0], predrecall_norm[0])))
print("SAMPLE POSRAT NORMALIZED MEAN SQUARED ERROR: " + str(m.mean_squared_error(trueposrat_norm[0], predposrat_norm[0])))
print("SAMPLE PERFRATIO NORMALIZED MEAN SQUARED ERROR: " + str(m.mean_squared_error(trueperfrat_norm[0], predperfrat_norm[0])))
print("SAMPLE IMPACT NORMALIZED MEAN SQUARED ERROR: " + str(m.mean_squared_error(trueimpact_norm[0], predimpact_norm[0])))
print("--------------")

print("CORRELATION BETWEEN TRUE AND PREDICTED RECALL: " + str(stats.pearsonr(truerecall_norm[0], predrecall_norm[0])))
print("CORRELATION BETWEEN TRUE AND PREDICTED POSITIVE RATING: " + str(stats.pearsonr(trueposrat_norm[0], predposrat_norm[0])))
print("CORRELATION BETWEEN TRUE AND PREDICTED PERFRATIO: " + str(stats.pearsonr(trueperfrat_norm[0], predperfrat_norm[0])))
print("CORRELATION BETWEEN TRUE AND PREDICTED IMPACT: " + str(stats.pearsonr(trueimpact_norm[0], predimpact_norm[0])))