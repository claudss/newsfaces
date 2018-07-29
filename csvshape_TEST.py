#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 20:10:58 2018

@author: claudia
"""

import csv


imgs = []
with open('cropped_test_feature.csv', 'r') as featread:
#with open('train_feature.csv', 'r') as featread:
        reader = csv.reader(featread, delimiter=',')
        index = 0
        for row in reader:
            if index > 0:
                imgs.append(row[0].strip())
            index += 1
        print("FINAL INDEX: " + str(index))
            
    #print(fname.strip('results/').strip('.csv'))
    
imgs.sort()

names = []
numbers = []
toadd = []
with open('attribs_uncut.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    index = 0
    count = 0
    for row in spamreader:
        #if (index < 1411):
        if (index > 1410):
            test = [row[0].strip(), row[1].strip()]
            names.append(test)
            test2 = [row[2].strip(), row[3].strip(), row[4].strip(), row[5].strip()]
            #print("TEST2: " + str(test2))
            numbers.append(test2)
            toadd.append(row)
        index += 1


count = 0
finalrows = []
for name in names:
 
    see = name[1].strip() + "_" + name[0].strip()
    see.replace(" ", "_")
    #print("SEE: " + see)
    for img in imgs:
        if see in img:
            for tr in toadd:
                thistest = (tr[1].strip() + "_" + tr[0].strip())
                if see == thistest:
                    print(see + " is in " + str(tr))
                    newrow = [img] + tr[-4:]
                    finalrows.append(newrow)
                    print("NEW ROW: " + str([img] + tr[-4:]))
                    count += 1
    
print("FINAL COUNT: " + str(count))

finalrows.sort()

with open('cropped_test_label.csv', 'w') as resout:
#with open('finalfinaltrain.csv', 'w') as resout:
    writer = csv.writer(resout, delimiter=',')
    writer.writerow(['', 'Recall', 'PositiveRating', 'PerfRatio', 'Impact'])
    for row in finalrows:
        writer.writerow(row)

featrows = []
with open('cropped_test_feature.csv', 'r') as featread:
#with open('train_feature.csv', 'r') as featread:
    reader = csv.reader(featread, delimiter=',')
    for row in reader:
        featrows.append(row)



with open('cropped_test_feature2.csv', 'w') as featwr:
#with open('train_feature2.csv', 'w') as featwr:
    writer = csv.writer(featwr, delimiter=',')
    writer.writerow([''] + list(range(128)))
    for fr in featrows:
        for fr2 in finalrows:
            if fr[0] == fr2[0]:
               writer.writerow(fr)




