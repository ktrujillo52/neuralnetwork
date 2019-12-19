#!/usr/bin/python
import os
import math
import subprocess
import csv
########################
#Modify these variables#
########################
pca_csv_path = "data"



###########################################################
#Do not modify below if you do not know what you are doing#
###########################################################

#Set path
p = os.chdir(pca_csv_path)

#Get contents of directory
c = os.listdir(pca_csv_path)

f = []
for item in c:
    f.append(item)

#Remove bitcoin csv from array

#Open bitcoin.csv
def extract(k):
    with open(k) as fi:
        reader = csv.reader(fi)
        reader.next()
        data = []
        for row in reader:
            data.append(row)
        fi.close()
    #Extract prices from csv
    price = []
    for i in data:
        price.append(i[1])
    return price
#Calculate NNJA
string = ""
low = 1000
key = []
track = []
for i in range(len(f)):
    key.append(i)
    track.append(0)
for k in f:
    ret = extract(k)
    for i in f:
        with open(i) as fi:
            reader = csv.reader(fi)
            reader.next()
            data = []
	    for row in reader:
                data.append(row)
            fi.close()
        count = 0
        arr = []
        for j in data:
	    arr.append(j[1])
        #print arr
        #print ret
        diffarray = []
        for x, b in zip(arr, ret):
	    diff = float(x) - float(b)
            diff = diff ** 2
            diff = math.sqrt(float(diff))
            count += float(diff)
            diffarray.append(diff)
        mult1 = 1.2 * diff
	mult2 = 1.4 * diff
	mult3 = 1.6 * diff
	mult4 = 1.8 * diff
	mult5 = 2 * diff
	multarr = [mult1, mult2, mult3, mult4, mult5]
        for l in multarr:
            for m in f:                                           	    
                ret = extract(k)
                for p in f: 
                    with open(p) as fip:
			reader = csv.reader(fip)
                        reader.next()
                        data = []
            	    	for q in reader:
                            data.append(q)
                        fip.close()
                    count = 0
                    ver = []
                    for n in data:
            	    	ver.append(n[1])
                    #print data
		    #print ver
                    #print ret
                    diffarray = []
                    for h, c in zip(ver, ret):
            	        #print h
			#print c
			diff = float(h) - float(c)
                        diff = diff ** 2
                        diff = math.sqrt(float(diff))
                        count += float(diff)
                        #print count
			diffarray.append(diff)
                    if count < multarr[0]:
			strin = p
			#print strin.split('.')[0]
			track[int(strin.split('.')[0])] += 1
		    if count < multarr[1]:
			strin = p
			#print strin
			track[int(strin.split('.')[0])] += 1 
		    if count < multarr[2]:
			strin = p
			#print strin
			track[int(strin.split('.')[0])] += 1 
		    if count < multarr[3]:
			strin = p
			#print strin
			track[int(strin.split('.')[0])] += 1 
		    if count < multarr[4]:
			strin = p
			#print strin
			track[int(strin.split('.')[0])] += 1 
		    #print track
#Now you have NN, use that as cutoff for clusters.
count = 0
string = ""
for x in range(len(track)):
    if track[x] > count:
	string = str(x)    
	count = track[x]



#Change name of NN to final.csv
os.chdir("/home/kevin/Desktop/Bot/data/")
variable = "cp "+str(string)+".csv final.csv"
sub = subprocess.check_output(['bash', '-c', variable])



