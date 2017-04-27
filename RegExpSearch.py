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

# Start of the main-function
# Iterate over the years
def main(argv=None):
    # Init
    # Dict = normal dictonary
    # Cities = dictionary contains only Cities
    # Forenames = dictionary contains only Forenames
    dict_typ = 'Dict'
    dict_lng = 'ger'
    wordfreq = 15
    year_start = 1956
    year_end = 1957
    word_min_len = 3
    # Status True print everything that is found in the dict
    # Status False print everything that isnt found in the dict
    Status = True
    for i in range(year_start, year_end):
        # Read the dictonary File and split it into a list
        dict_file = open("Dictionaries\\%s_%s.txt" % (dict_typ,dict_lng), 'r')
        dict_list = list()
        for word in dict_file:
            dict_list.append(word)
        # Read the datafile
        txt_file = open("U:\\Eigene Dokumente\\Aktienfuehrer_Dokumente\\Aktienfuehrer_PostOCR_Format\\%d\\WordFreq_%d" % (i,i), 'r')
        # Open outputfile
        output_file = open("U:\\Eigene Dokumente\\Aktienfuehrer_Dokumente\\Aktienfuehrer_PostOCR_Format\\%d\\%s_%d.txt" % (i,dict_typ,i), 'w')
        # Search in every line of the datafile the given words of the dictonary
        for line in txt_file:
            if (int(re.search(r"\d*", line).group(0)) > wordfreq):
                count = 0;
                for word in dict_list:
                    if len(word) > word_min_len:
                        if (Status == True):
                                if line.find(word) != -1:
                                    output_file.write(word)
                                    del dict_list[count]
                                    break
                        if (Status == False):
                                if line.find(word) != -1:
                                    break
                                if word == dict_list[-1]:
                                    output_file.write(re.search(r"\s*", line).group(0))
                    count +=1;
        output_file.close()
        dict_file.close()
        txt_file.close()

if __name__ == "__main__":
    main()
