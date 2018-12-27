#!/usr/bin/python3.7



race = str(input("what race are you? \n 1.Zerg \n 2.Terran \n 3.Protoss \n 4.Random\n:"))
print (race)
if  race == "1":
        race1 = "Zerg"
if  race == "2": 
        race1 = "Terran"
if  race == "3":
        race1 = "Protoss"
if  race == "4":
        race1 = "Random"
 

#print (race1)
#f= open(race1 + ".txt","w+")
#f.write(race1)
#f.close()

#print ("what race did you face? \n 1.Zerg \n 2.Terran \n 3.Protoss" )
opposingrace = str(input("what race are you? \n 1.Zerg \n 2.Terran \n 3.Protoss\n:"))
print (opposingrace)
if  opposingrace == "1":
        opposingrace1 = "Zerg"
if  opposingrace == "2": 
        opposingrace1 = "Terran"
if  opposingrace == "3":
        opposingrace1 = "Protoss"
 
points = int(input('how. much points did you win or lose? [syntax +number or -number]'))
if points >= 0:
    print ("you win " + str(points))
else:
    print ("you lost " + str(points))

f= open(race1 + "vs" + opposingrace1 + ".txt", "a+")
f.write(race1 + ":" + opposingrace1 + ":" + str(points) + "\n")
f.close()




#print ("what strategy did you face?")
#print ("what strategy did you face?")
#print ("what strategy did you face?")
#print ("what race are you?")
