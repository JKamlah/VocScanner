#Program to detect words of a library in a certain textfile
#WARNING: The textfile for this program should be an output of an hocr-file
#         through "hocr-tools"-WordFreq
#Program:  **RegExpSearch**
#Info:     **Python 2.7**
#Project:  **Aktienführer II**
#Author:   **Jan Kamlah**
#Date:     **26.04.2017**

import os
import re

for i in range(1956, 1978):
    # Read the dictonary File and split it into single pieces
    dictonary_data=open('\\Dictonaries\\Forename_ger.txt', "r+")
    dictonary = list()
    for word in dictonary_data:
        dictonary.append(word)
    #print dictonary
    # Read the datafile
    datafile=open("U:\\Eigene Dokumente\\Aktienfuehrer_Dokumente\\Aktienfuehrer_PostOCR_Format\\%d\\WordFreq_%d" % (i,i), "r+")

    # Open outputfile
    output = open("U:\\Eigene Dokumente\\Aktienfuehrer_Dokumente\\Aktienfuehrer_PostOCR_Format\\%d\\Cities_%d.txt" % (i,i), 'a')

    # Search in every line of the datafile the given words of the dictonary
    for line in datafile:
        if (int(re.search(r"\d*", line).group(0)) > 7):
            count = 0;
            for word in dictonary:
                if line.find(word) != -1:
                    output.write(word)
                    del dictonary[count]
                    break
                count +=1;

    output.close()
