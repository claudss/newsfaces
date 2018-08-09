#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 20:25:39 2018

@author: claudia
"""
import csv
import numpy as np
recallmin = 100
recallmin_list = []
recallmax = 0
recallmax_list = []
posratmin = 100
posratmin_list = []
posratmax = 0
posratmax_list = []
perfratmin = 100
perfratmin_list = []
perfratmax = 0
perfratmax_list = []
impactmin = 100
impactmin_list = []
impactmax = 0
impactmax_list = []

recallmindex = 0
recallmaxindex = 0
posratmindex = 0
posratmaxindex = 0
perfratmindex = 0
perfratmaxindex = 0
impactmindex = 0
impactmaxindex = 0

index = 0
featrows = []
#with open('predictionresults.csv', 'r') as labelread:
with open('reclassified/female_pred2.csv', 'r') as labelread:
    reader = csv.reader(labelread, delimiter=',')
    
    for row in reader:
        if (index > 0):
            featrows.append(row)
        index += 1

featarray = np.array(featrows)
recall = featarray[:, 1].tolist()
posrat = featarray[:, 2].tolist()
perfrat = featarray[:, 3].tolist()
impact = featarray[:, 4].tolist()
"""
print("MAX RECALL: " + str(featarray[recall.index(max(recall))]))
print("MIN RECALL: " + str(featarray[recall.index(min(recall))]) + "\n")

print("MAX POSITIVE RATING: " + str(featarray[posrat.index(max(posrat))])) 
print("MIN POSITIVE RATING: " + str(featarray[posrat.index(min(posrat))]) + "\n")

print("MAX PERFRAT: " + str(featarray[perfrat.index(max(perfrat))]))
print("MIN PERFRATIO: " + str(featarray[perfrat.index(min(perfrat))]) + "\n")

print("MAX IMPACT: " + str(featarray[impact.index(max(impact))]))
print("MIN IMPACT: " + str(featarray[impact.index(min(impact))]))

"""

recall2 = recall[:]
recall3 = recall[:]

recall2.sort(reverse=True)
recall3.sort()

recallmaxindices = [recall.index(recall2[0]), recall.index(recall2[1]), recall.index(recall2[2]), recall.index(recall2[3]),
                 recall.index(recall2[4])]

recallminindices = [recall.index(recall3[0]), recall.index(recall3[1]), recall.index(recall3[2]), recall.index(recall3[3]),
                 recall.index(recall3[4])]

posrat2 = posrat[:]
posrat3 = posrat[:]

posrat2.sort(reverse=True)
posrat3.sort()

posratmax = [posrat.index(posrat2[0]), posrat.index(posrat2[1]), posrat.index(posrat2[2]), posrat.index(posrat2[3]),
             posrat.index(posrat2[4])]

posratmin = [posrat.index(posrat3[0]), posrat.index(posrat3[1]), posrat.index(posrat3[2]), posrat.index(posrat3[3]),
             posrat.index(posrat3[4])]

perfrat2 = perfrat[:]
perfrat3 = perfrat[:]

perfrat2.sort(reverse=True)
perfrat3.sort()

perfratmax = [perfrat.index(perfrat2[0]), perfrat.index(perfrat2[1]), perfrat.index(perfrat2[2]), perfrat.index(perfrat2[3]),
              perfrat.index(perfrat2[4])]

perfratmin = [perfrat.index(perfrat3[0]), perfrat.index(perfrat3[1]), perfrat.index(perfrat3[2]), perfrat.index(perfrat3[3]),
              perfrat.index(perfrat3[4])]

impact2 = impact[:]
impact3 = impact[:]

impact2.sort(reverse=True)
impact3.sort()

impactmax = [impact.index(impact2[0]), impact.index(impact2[1]), impact.index(impact2[2]), impact.index(impact2[3]),
             impact.index(impact2[4])]

impactmin = [impact.index(impact3[0]), impact.index(impact3[1]), impact.index(impact3[2]), impact.index(impact3[3]),
             impact.index(impact3[4])]

for ind in recallmaxindices:
    print(str(featrows[ind]))