#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:24:04 2018

@author: claudia
"""
import os
import csv
import shutil
import glob

trainrows = []
testrows = []

#THIS CODE IS USED TO SORT THE RESULTS INTO THE APPOPRIATE CSV
"""
finalwr = []
for fname in glob.glob("results/*.csv"):
    png = fname.split("/")[1].strip('.csv')
    with open(fname, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        index = 0
        for row in reader:
            if (index > 0):
                finalwr.append([png] + row[0:4])
            index += 1

finalwr.sort()
with open('grouped_ID/pred_anchor_FEMALE.csv', 'w') as pr:
    writer = csv.writer(pr, delimiter=',')
    writer.writerow(['', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact'])   
    for w in finalwr:
        writer.writerow(w)
"""



# THIS CODE IS USED TO SEPARATE EVERYTHING BY GENDER

gendrows = []
with open('grouped_ID/with_extra/cropped_test_anchor.csv', 'r') as g:
    reader = csv.reader(g, delimiter=',')
    index = 0
    for row in reader:
        if (index > 0 and row[6] == 'Female'):
            #print(str(row[:5]))
            gendrows.append(row[:5])
        index += 1

gendrows.sort()

with open('grouped_ID/anchor_test_label_FEMALE.csv', 'w') as wr:
    writer = csv.writer(wr, delimiter=',')
    writer.writerow(['', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact']) 
    for r in gendrows:
        writer.writerow(r)

newfeats = []
finalfeats = []
with open ('grouped_ID/anchor_test_label_FEMALE.csv', 'r') as r:
    reader = csv.reader(r, delimiter=',')
    index = 0
    for row in reader:
        if (index > 0):
            newfeats.append(row[0])
        index += 1
    
    newfeats.sort()
    with open('grouped_ID/cropped_test_feat_anchor.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        index2 = 0
        for row in reader:
            if (row[0] in newfeats and index2 > 0):
                finalfeats.append(row)
            index2 += 1
finalfeats.sort()       
with open('grouped_ID/anchor_test_feat_FEMALE.csv', 'w') as wr:
    writer = csv.writer(wr, delimiter=',')
    writer.writerow([''] +  list(range(128)))
    for f in finalfeats:
        writer.writerow(f)

with open ('grouped_ID/anchor_test_label_FEMALE.csv', 'r') as r:
    reader = csv.reader(r, delimiter=',')
    index = 0
    for row in reader:
        if (index > 0):
            shutil.copyfile(("cropped_test/" + row[0]), ("grouped_ID/anchor_test_FEMALE/" + row[0]))
        index += 1


#THIS CODE IS USED TO SEPARATE IMAGES INTO THEIR CORRECT FOLDERS
"""
with open('grouped_ID/cropped_train_WX.csv', 'r') as cta:
    reader = csv.reader(cta, delimiter=',') 
    index = 0
    for row in reader:
        if (index > 0):
            shutil.copyfile(("cropped_train/" + row[0]), ("grouped_ID/wx_train/" + row[0]))
        index += 1
"""

# THIS CODE WAS USED TO SEPARATE LABELS INTO PROPER CSVS
"""
trainnames = []
testnames = []
with open('cropped_train_label_ID.csv', 'r') as t:
    reader = csv.reader(t, delimiter=',')
    index = 0
    for row in reader:
        if (index > 0):
            trainrows.append(row)
        index += 1

with open('cropped_test_label_ID.csv', 'r') as t:
    reader = csv.reader(t, delimiter=',')
    index = 0
    for row in reader:
        if (index > 0):
            testrows.append(row)
            
        index += 1
        
trainrows.sort()
testrows.sort()

with open('grouped_ID/cropped_train_anchor.csv', 'w') as cta:
    writer = csv.writer(cta, delimiter=',')
    writer.writerow(['', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact', 'NewsID', 'Gender', 'Race'])
    for tr in trainrows:
        if (int(tr[5]) == 2):
            writer.writerow(tr)
            trainnames.append(tr[0])
            

with open('grouped_ID/cropped_test_anchor.csv', 'w') as cta2:
    writer = csv.writer(cta2, delimiter=',')
    writer.writerow(['', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact', 'NewsID', 'Gender', 'Race'])
    for tr in testrows:
        if (int(tr[5]) == 2):
            writer.writerow(tr)
            testnames.append(tr[0])
        
with open('grouped_ID/cropped_test_feat_anchor.csv', 'w') as ctf:
    writer = csv.writer(ctf, delimiter=',')
    writer.writerow([''] +  list(range(128)))
    with open('cropped_test_feature2.csv', 'r') as fe:
        reader = csv.reader(fe, delimiter=',')
        for row in reader:
            if row[0] in testnames:
                writer.writerow(row)

with open('grouped_ID/cropped_train_feat_anchor.csv', 'w') as ctf:
    writer = csv.writer(ctf, delimiter=',')
    writer.writerow([''] +  list(range(128)))
    with open('cropped_train_feature3.csv', 'r') as fe:
        reader = csv.reader(fe, delimiter=',')
        for row in reader:
            if row[0] in trainnames:
                writer.writerow(row)
"""
# THIS CODE WAS PREVIOUSLY USED TO ATTACH THE CORRECT IDS TO EVERY LABEL THAT WAS ALREADY ORGANIZED
"""
numfiles = 0
imgnames = []
featrows = []
featfile = 'cropped_test_feature2.csv'
labelfile = 'cropped_test-new.csv'

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
        if (index > 1410):
        #if (index < 1410):
            test = [row[0].strip(), row[1].strip()]
            #print(str(test))
            names.append(test)
            test2 = [row[2].strip(), row[3].strip(), row[4].strip(), row[5].strip(), row[6].strip()]
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
                    print(see + " is in " + str(tr))
                    newrow = [img] + tr[-5:]
                    finalrows.append(newrow)
                    #print("NEW ROW: " + str([img] + tr[-4:]))
                    count += 1
                    toadd.remove(tr)
    
print("FINAL COUNT OF AVAILABLE ROWS: " + str(len(finalrows)))

finalrows.sort()

names = []
lout = []
with open('attribs_uncut.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    index = 0
    count = 0
    for row in spamreader:
        #print("CURRENT INDEX: " + str(index) + " IS NOT IN " + str((index in indices)))
        #if (index < 1411):
        if (index > 1410):
            fullname = str(row[1].strip() + "_" + row[0].strip())
            fullname.replace(" ", "_")
            names.append(fullname)
            for imgn in dupnames:
                if fullname in imgn:
                    #print("NAME " + fullname + " IS IN " + imgn + " AT INDEX " + str(index))
                    lout.append([imgn] + row[-5:])
                    #print("APPENDING " + str(row[-4:]) + " TO LOUT")
                    count += 1
                    dupnames.remove(imgn)
                    break
        index += 1
       # print (thisrow)
    print("FINAL AMOUNT OF INDICES SEEN: " + str(count))


with open('cropped_test_label_ID.csv', 'w') as idw:
    writer = csv.writer(idw, delimiter=',')
    writer.writerow(['', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact', 'NewsID'])
    for row in lout:
        writer.writerow(row)
"""