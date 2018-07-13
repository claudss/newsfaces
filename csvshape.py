#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:21:05 2018

@author: Claudia Seidel

This file was made to trim the existing results/label csv into manageable columns. Not needed for the main model execution.
"""
import pandas as pd
import csv
import os
imagepath = "cropped_train/"
filelist = os.listdir(imagepath)
filelist.sort()

firsts =[]
lasts = []

with open('attribs_uncut.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='"')
    for row in spamreader:
        thisrow = row[0].split(",")
        lasts.append(thisrow[0])
        firsts.append(thisrow[1])
        #print (thisrow)

found=0
finalf = []
finall = []
matches = []
for file in filelist:
    for f, l in zip(firsts, lasts):
        if file.find(f) > 0 and file.find(l) > 0:
            print("File " + file + " has a match in our CSV!")
            matches.append(file)
            finalf.append(f)
            finall.append(l)
            found += 1
            
outrows = []
with open('attribs_uncut.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='"')
    for row in spamreader:
        thisrow = row[0].split(",")
        for f, l in zip(finalf, finall):
            if (thisrow[0] == l) and (thisrow[1] == f) and thisrow not in outrows:
                outrows.append(thisrow)
                #print (thisrow)

with open('label.csv','w') as csvout:
    writer = csv.writer(csvout)
    writer.writerow(['LastName','FirstName', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact'])
    for r in outrows:
        #print("Row " + str(r) + " written successfully.")
        writer.writerow(r)

        
foutrows = []
with open('feature.csv', 'r') as featin:
    reader = csv.reader(featin, delimiter='"')
    for row in reader:
        thisrow = row[0].split(",")
        #print ("Thisrow[0]: " + thisrow[0])
        if thisrow[0] in filelist:
            for f, l in zip(finalf, finall):
                if f in thisrow[0] and l in thisrow[0]:
                    if thisrow not in foutrows:
                        foutrows.append(thisrow)
                        print("Row " + str(thisrow) + " to be written.")

toprow = [''] + list(range(0, 128))
foutrows.sort()
with open('features.csv', 'w') as featout:
    writer = csv.writer(featout, delimiter=',')
    writer.writerow(toprow)
    for r in foutrows:
        print ("Row " + str(r) + " written successfully.")
        writer.writerow(r)

        
print("Amount of images available: " + str(len(filelist) ))
#print("Matches found: " + str(found))