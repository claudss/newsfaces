#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:21:05 2018

@author: Claudia Seidel

This file was made to trim the existing results/label csv into manageable columns. Not needed for the main model execution.
"""
import pandas as pd
import glob
import csv
import os
import shutil
import collections
import numpy as np
imagepath = "cropped_train/"
filelist = os.listdir(imagepath)
filelist.sort()

firsts = []
lasts = []

matches = []
imgnames = []

numfiles = 0

featrows = []
featfile = 'cropped_train_feature.csv'
labelfile = 'cropped_train_label.csv'
"""
with open(featfile, 'r') as featread:
    reader = csv.reader(featread, delimiter='"')
    for row in reader:
        if (numfiles > 0):
            thisrow = row[0].split(",")
            featrows.append(thisrow)
            imgnames.append(thisrow[0])
            #print("TESTING NAME: " + thisrow[0])
        numfiles += 1

print("AMOUNT OF ROWS IN FEATROWS: " + str(len(featrows)))
names = []
toadd = []
with open('attribs_uncut.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    index = 0
    count = 0
    for row in spamreader:
        if (index < 1411):
        #if (index < 1410):
            test = [row[0].strip(), row[1].strip()]
            
            names.append(test)
            test2 = [row[2].strip(), row[3].strip(), row[4].strip(), row[5].strip()]
            #print("TEST2: " + str(test2))
            toadd.append(row)
        index += 1

dupnames = imgnames[:]
count = 0
finalrows = []
for name in names:
 
    see = name[1].strip() + "_" + name[0].strip()
    see.replace(" ", "_")
    #print("SEE: " + see)
    for img in imgnames:
        if see in img:
            for tr in toadd:
                thistest = (tr[1].strip() + "_" + tr[0].strip())
                if see == thistest:
                    #print(see + " is in " + str(tr))
                    newrow = [img] + tr[-4:]
                    finalrows.append(newrow)
                    #print("NEW ROW: " + str([img] + tr[-4:]))
                    count += 1
                    toadd.remove(tr)
    
#print("FINAL COUNT OF AVAILABLE ROWS: " + str(len(finalrows)))

finalrows.sort()
with open('cropped_train_label.csv', 'w') as resout:
#with open('finalfinaltrain.csv', 'w') as resout:
    writer = csv.writer(resout, delimiter=',')
    writer.writerow(['', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact'])
    for row in finalrows:
        writer.writerow(row)

"""

featrows = []
with open('cropped_test_feature2.csv', 'r') as featread:
#with open('cropped_train_feature3.csv', 'r') as featread:
#with open('train_feature.csv', 'r') as featread:
    reader = csv.reader(featread, delimiter=',')
    for row in reader:
        featrows.append(row)

genfeats = []
labelrows = []
"""
#with open('cropped_train-new.csv', 'r') as labelread:
with open('cropped_test-new.csv', 'r') as labelread:
    reader = csv.reader(labelread, delimiter=',')
    for row in reader:
        if (row[5] == "Male"):
            labelrows.append(row[0:5])
"""
with open('cropped_test-new.csv', 'r') as labelread:
    reader = csv.reader(labelread, delimiter=',')
    for row in reader:
        if (row[5] == "Male"):
            labelrows.append(row[0])

# for every file in reclassified/male_train and reclassified/male_test get their filenames and put them 
#into a new male only folder
labelrows = []    
labelnames = []
with open('reclassified/male_train_label.csv', 'r') as l:
    reader = csv.reader(l, delimiter=',')
    index = 0
    for row in reader:
        labelrows.append(row)
        #labelnames.append(row[0])
        if (index > 0):
            labelnames.append(row[0])
            shutil.copyfile(("reclassified/male_train/" + row[0]), ("reclassified/ALL_male/imgs/" + row[0]))
            labelnames.append(row[0])
        index += 1

with open('reclassified/male_test_label.csv', 'r') as l2:
    reader = csv.reader(l2, delimiter=',')
    index = 0
    for row in reader:
        if (index > 0):
            labelrows.append(row)
            labelnames.append(row[0])
            shutil.copyfile(("reclassified/male_test/" + row[0]), ("reclassified/ALL_male/imgs/" + row[0]))
            labelnames.append(row[0])
        index += 1

labelrows.sort()
labelnames.sort()
"""
"""
with open('reclassified/ALL_male/labels_male.csv', 'w') as labels:
    writer = csv.writer(labels, delimiter=',')
    for row in labelrows:
        writer.writerow(row)
"""
"""
newnames = []
for fname in glob.glob("aligned-faces-updated/*"):
    name = fname.split("/")[1]
    smallname = name.strip(".jpg").strip(".png").strip("-NEW")
    for l in labelnames:
        if (smallname in l):
            newnames.append(name)
            #shutil.copyfile(fname, "reclassified/ALL_male/imgs_test/" + name)
            labelnames.remove(l)
    #print(smallname)
newnames.sort()
for n in newnames:
    print(n)
    
    
    
with open('labels_male_final.csv', 'w') as labels2:
    writer = csv.writer(labels2, delimiter=',')
    for l in labelrows:
        print(test)
     
    
    
    
    
"""
finallabels = []
for fname in glob.glob("reclassified/ALL_male/imgs/*"):
    name = fname.split("/")[3]
    finallabels.append(name)

finallabels.sort()

for f in finallabels:
    print(f)
    
    


labs = np.array(labelrows)[:, 0].tolist()
for fr in featrows:
    for lr in labs:
        if (lr in fr):
            genfeats.append(fr)

#with open('reclassified/male_train_label.csv', 'w') as wrout:
with open('reclassified/male_test_label.csv', 'w') as wrout:            
    writer = csv.writer(wrout, delimiter=',')
    writer.writerow(['', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact'])
    for row in labelrows:
        writer.writerow(row)
        
        

        
#with open('reclassified/male_train_feature.csv', 'w') as wrout2:
with open('reclassified/male_test_feature.csv', 'w') as wrout2:        
    writer = csv.writer(wrout2, delimiter=',')
    writer.writerow([''] + list(range(128)))
    for row in genfeats:
        writer.writerow(row)
"""


"""        
newfeat = []
for lr in labelrows:    
    for fr in featrows:
        if (lr[0] == fr[0]):
            newfeat.append(fr)
            continue

newfeat.sort()
with open('cropped_train_feature3.csv', 'w') as featwr:
    writer = csv.writer(featwr, delimiter=',')
    for o in newfeat:
        writer.writerow(o)
"""
















"""
with open('cropped_train_feature2.csv', 'w') as featwr:
#with open('train_feature2.csv', 'w') as featwr:
    writer = csv.writer(featwr, delimiter=',')
    writer.writerow([''] + list(range(128)))
    for fr in featrows:
        for fr2 in finalrows:
            if fr[0] == fr2[0]:
               writer.writerow(fr)
"""









"""
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

