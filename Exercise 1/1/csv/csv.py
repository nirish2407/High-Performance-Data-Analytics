#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 00:21:38 2024

@author: nirish
"""

import sys
import csv

#Commandline arguments are avalible in the sys.argv list
print(sys.argv)

count = 0

#Implement this function, do not use a function to completely parse the CSV file!
def computeMeanCSV(filename, column_number):
    
    csv_file = open(filename,"r")
    
    reader = csv.reader(csv_file, delimiter=',')
    
    count = 0
    
    for row in reader:

        count = count + 1
        
        if count == 1 :
            
            length = len(row)
            sums = [0] * length
            
            continue
        
        length = len(row)
        
        for i in range(0, length):
            
            sums[i] = sums[i] + int(row[i])
            
    for i in range(0, length):
            
        sums[i] = sums[i] / (count-1)
    
    print (sums)

computeMeanCSV("csv.csv", 1)