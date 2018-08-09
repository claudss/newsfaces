#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 21:42:56 2018

@author: claudia
This program is to format the cropped images into their own folders with their names.
"""

import glob
import csv
import os
import shutil
from itertools import count


"""
for fname in glob.glob("reclassified/female_test/*.jpg"):
    print(str(fname))
"""
names = []
impactnames = []
maxlen = 0
with open('reclassified/male_pred2.csv', 'r') as pred:
    reader = csv.reader(pred, delimiter=',')
    index = 0
    for row in reader:
        if (index > 0):
            name = row[0].strip("2/")
            names.append(name)
            
            imp = str(row[1]) + "-" + name[6:]
            #print(imp)
            if (len(imp) > maxlen):
                maxlen = len(str(row[1]))
            impactnames.append(imp)
        index += 1

print("Maximum number length: " + str(maxlen))
impactnames.sort()


d = "reclassified/male_test/"
newd = "reclassified/sorted_traits_male/recall/"

index = 0
for im in impactnames:
    n1 = im.split("-")[1] + "-" + im.split("-")[2] # + "-" + im.split("-")[3]
    str0 = ""
    newim = ""
    if (len(im.split("-")[0]) < maxlen):
        correction = maxlen - len(im.split("-")[0])
        for i in range (0, correction-1):
            str0 = str0 + "0"
        newim = newd + im.split("-")[0] + str0 + "-" + n1
        print("CORRECTED: " + newim)
    
    for n in names:
        if (n1 in n):
            #print("copying " + n + " to " + im)
            shutil.copyfile((d + n), (newd + im))
    index += 1
    
       
    