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
import collections
imagepath = "cropped_train/"
filelist = os.listdir(imagepath)
filelist.sort()

firsts = []
lasts = []

matches = []
imgnames = []

numfiles = 0

featrows = []
featfile = 'test_feature.csv'
labelfile = 'test_label.csv'
with open(featfile, 'r') as featread:
    reader = csv.reader(featread, delimiter='"')
    for row in reader:
        thisrow = row[0].split(",")
        featrows.append(thisrow)
        imgnames.append(thisrow[0])
        #print("TESTING NAME: " + thisrow[0])
        numfiles += 1
        
print("AMOUNT OF FILES TO FIND LABELS FOR : " + str(numfiles))
print("AMOUNT OF ROWS IN FEATROWS: " + str(len(featrows)))

dupimg = imgnames[:]

names = []
lout = []
with open('attribs_uncut.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    index = 0
    count = 0
    for row in spamreader:
        #print("CURRENT INDEX: " + str(index) + " IS NOT IN " + str((index in indices)))
        if (index < 1411):
            
            lasts.append(row[0].strip())
            firsts.append(row[1].strip())
            fullname = str(row[1].strip() + "_" + row[0].strip())
            fullname.replace(" ", "_")
            names.append(fullname)
            for imgn in dupimg:
                if fullname in imgn:
                    #print("NAME " + fullname + " IS IN " + imgn + " AT INDEX " + str(index))
                    lout.append([imgn] + row[-4:])
                    #print("APPENDING " + str(row[-4:]) + " TO LOUT")
                    count += 1
                    dupimg.remove(imgn)
                    break
            index += 1
       # print (thisrow)
    print("FINAL AMOUNT OF INDICES SEEN: " + str(count))
    
with open(labelfile,'w') as csvout:
    writer = csv.writer(csvout, delimiter=',')
    writer.writerow(['', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact'])
    index = 0
    for outrow in lout:
        #print("AT INDEX " + str(index) + ": " + str(loutfinal[index]))
        #if (i < len(lout) - 1):
        #print("ROW TO BE WRITTEN: INDEX " + str(i) + " " + str(loutfinal[i]))
        #print("\tIMGN: " + str(imgnames[index]))
        writer.writerow(outrow)
        index += 1
        
with open(featfile,'w') as featout:
    writer = csv.writer(featout, delimiter=',')
    #writer.writerow(['', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact'])
    writer.writerow(list(range(128)))
    index = 0
    for outrow in lout:
        #print("AT INDEX " + str(index) + ": " + str(loutfinal[index]))
        #if (i < len(lout) - 1):
        #print("ROW TO BE WRITTEN: INDEX " + str(i) + " " + str(loutfinal[i]))
        #print("\tIMGN: " + str(imgnames[index]))
        for row in featrows:
            if outrow[0] == row[0]:
                writer.writerow(row)
        #index += 1

    
    
"""
for f in filelist:
    imgnames.append(f)
    cur = f.split("-")[0]
    matches.append(int(cur))
    #print("MATCH OF " + str(f) + ": " + str(int(cur)))

with open('features.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='"')
    for row in spamreader:
        
        thisrow = row[0].split(",")
        print("img name: " + str(thisrow[0]))
       

#imgnames.sort()
print("How many images on file? " + str(len(imgnames)))
matches.sort()

names = []
lout = []
with open('attribs_uncut.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    index = 0
    for row in spamreader:
        #print("CURRENT INDEX: " + str(index) + " IS NOT IN " + str((index in indices)))
        if (index < 1411):
            lout.append(row)
            lasts.append(row[0].strip())
            firsts.append(row[1].strip())
            names.append(str(row[1].strip() + "_" + row[0].strip()))
        index += 1
       # print (thisrow)


index = 0
loutfinal = []

indices = []
#for f, l in zip(firsts, lasts):
currcount = 0
for imgn in imgnames:
    index = 0
    for name in names:
        
        if (name in imgn):
            print("NAME " + name + " IS IN IMG " + imgn + " AT INDEX " + str(index))
            print("STATS: " + str(lout[index][-4:]))
            loutfinal.append([imgn] + lout[index][-4:])
            
            #print("LOUTFINAL: " + str(loutfinal))
            indices.append(index)
            break
        

        if (f in imgn) and (l in imgn):
            print("INDEX OF " + f + " " + l + ": " + str(index))
            #print("TEST: " + str(lout[index]))
            #loutfinal.append(lout[index])

       
        index += 1
    
   




print("How many indices? " + str(len(loutfinal)))

with open('train_label.csv','w') as csvout:
    writer = csv.writer(csvout, delimiter=',')
    writer.writerow(['', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact'])
    index = 0
    for i in indices:
        #print("AT INDEX " + str(index) + ": " + str(loutfinal[index]))
        #if (i < len(lout) - 1):
        #print("ROW TO BE WRITTEN: INDEX " + str(i) + " " + str(loutfinal[i]))
        #print("\tIMGN: " + str(imgnames[index]))
        writer.writerow(loutfinal[index])
        index += 1

"""
#print("Amount of images available: " + str(len(filelist) ))
#print("Matches found: " + str(found))
