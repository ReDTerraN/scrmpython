#!/bin/python3.7
import re
import datetime

fname ="stats.txt"
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
        searchObj = re.search( r'(.*):(.*):(.*):(.*):(.*)', line, re.M|re.I)
 
        race = searchObj.group(1)
        opposing = searchObj.group(2)
        points = searchObj.group(3)
        winloss = searchObj.group(4)
        date = searchObj.group(5) 
        if race == "zerg" and opposing == "terran":
            print ("zvt")  
        if race == "zerg":
            print ("z") 
        if race == "protoss":
            print ("p") 
        if searchObj:
              print ("searchObj.group() : ", searchObj.group())
              print ("searchObj.group(1) : race :", searchObj.group(1))
              print ("searchObj.group(2) : opposing :", searchObj.group(2))
              print ("searchObj.group(3) : points :", searchObj.group(3))
              print ("searchObj.group(4) : win/loss :", searchObj.group(4))
        

              print ("searchObj.group(5) : date :", searchObj.group(5))
        else:
               print ("Nothing found!!")
print("Number of lines:")
print(num_lines)

time = datetime.datetime.now()

thedate = (time.strftime("%d")+ "." + time.strftime("%m") + "." + time.strftime("%y")) 

print (thedate)



