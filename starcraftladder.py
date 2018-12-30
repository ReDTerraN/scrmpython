#!/usr/bin/python3.7
import re
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime

race = str(input("what race are you? \n 1.Zerg \n 2.Terran \n 3.Protoss \n 4.Random\n:"))
print (race)
if  race == "1":
        race1 = "zerg"
if  race == "2": 
        race1 = "terran"
if  race == "3":
        race1 = "protoss"
if  race == "4":
        race1 = "random"
 

#print (race1)
#f= open(race1 + ".txt","w+")
#f.write(race1)
#f.close()

#print ("what race did you face? \n 1.Zerg \n 2.Terran \n 3.Protoss" )
opposingrace = str(input("what race did you face? \n 1.Zerg \n 2.Terran \n 3.Protoss\n:"))
print (opposingrace)
if  opposingrace == "1":
        opposingrace1 = "zerg"
if  opposingrace == "2": 
        opposingrace1 = "terran"
if  opposingrace == "3":
        opposingrace1 = "protoss"
 
points = int(input('with how many points did you win or lose? [syntax +number or -number]'))
if points >= 0:
    status = "win"
    print ("you won " + str(points))
else:
    print ("you lost " + str(points))
    status = "lost"

time = datetime.datetime.now()
thedate = (time.strftime("%d")+ "." + time.strftime("%m") + "." + time.strftime("%y"))
print (thedate)

f= open("stats.txt", "a+")
f.write(race1 + ":" + opposingrace1 + ":" + str(points) + ":" + status + ":" + thedate + "\n")
f.close()

fname ="stats.txt"
num_lines = 0
wintick = 0
losstick = 0
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


        if winloss == "win":
            wintick += 1
        if winloss == "lost":
            losstick += 1



print("Number of lines:")
print(num_lines)

print (wintick)
#print (losstick)
#wresults = (wintick - losstick)
#print (wlresults)
wlresults =  (wintick / num_lines * 100)
print (wlresults)
x = np.linspace(0, num_lines, 100)
y = np.linspace(wlresults, wlresults, 100) # A = vart den börjar B = games total C =
plt.plot(x, y, label='overall')
#plt.plot(y, y, label='ZvZ')
#plt.plot(x, x**3, label='ZvT')
#plt.plot(x, x**4, label='ZvP')
#plt.plot(x, x**5, label='TvP')

plt.ylabel('winrate %')
plt.xlabel('games total')

plt.title("Winrate for each MU")

plt.legend()

plt.show()


#print ("what strategy did you face?")
#print ("what strategy did you face?")
#print ("what strategy did you face?")
#print ("what race are you?")
