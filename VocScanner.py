#Program to detect words of a vocabulary in a certain textfile
#WARNING: The textfile for this program should be an output of an hocr-file
#         through "hocr-tools"-WordFreq
#Program:  **VocScanner**
#Info:     **Python 2.7**
#Project:  **Aktienführer II**
#Author:   **Jan Kamlah**
#Date:     **26.04.2017**

import os
import re

# Start of the main-function
# Iterate over the years
# Init
# voc = normal vocabulary
# Cities = vocionary contains only Cities
# Forenames = vocionary contains only Forenames
voc_typ = 'voc'
voc_lng = 'ger'
wordfreq = 100
year_start = 1960
year_end = 1978
word_min_len =1
# Status True print everything that is found in the voc
# Status False print everything that isnt found in the voc
Status = False
for i in range(year_start, year_end):
    # Read the vocabulary File and split it into a list
    voc_file = open("vocionaries\\%s_%s.txt" % (voc_typ,voc_lng), 'r')
    voc_list = list()
    for word in voc_file:
        voc_list.append(word)
    # Read the datafile
    txt_file = open("U:\\Eigene Dokumente\\Aktienfuehrer_Dokumente\\Aktienfuehrer_PostOCR_Format\\%d\\WordFreq_%d" % (i,i), 'r')
    # Open outputfile
    output_file = open("U:\\Eigene Dokumente\\Aktienfuehrer_Dokumente\\Aktienfuehrer_PostOCR_Format\\%d\\%s_%d.txt" % (i,voc_typ,i), 'w')
    # Search in every line of the datafile the given words of the vocabulary
    for line in txt_file:
        if (int(re.search(r"\d*", line).group(0)) > wordfreq):
            if (len(line.split()[1]) > word_min_len):
                count = 0;
                for word in voc_list:
                    if len(word) > word_min_len+1:
                        if (Status == True):
                                if line.find(word) != -1:
                                    output_file.write(word)
                                    del voc_list[count]
                                    break
                        if (Status == False):
                                if line.find(word) != -1:
                                    break
                                if word == voc_list[-1]:
                                    output_file.write(line.split()[1]+'\n')
                    count +=1;
    output_file.close()
    voc_file.close()
    txt_file.close()
