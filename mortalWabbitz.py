#Mortal Fibonacci Rabbits
#Rosalind Problem
#Spent way too long figuring out a bug. Seems taking an extremely large number
#from a list gives an innaccurate number, so I have to add long for it to work properly

import numpy

n = 82 #number of months
k = 1 #number of pairs of rabbits made
count = 2 #Always starts at 2
initial = 1 #first two numbers
initial2 = 1
countOfMonth = 17 #life of each pair in months

#############
totalWabbitz = numpy.zeros((n+1))
totalWabbitz[0] = initial
totalWabbitz[1] = initial2


def wabbits(B4, now):
    global count, k, n

    totalWabbitz[count] = (now)
    count = count+1
    if (count == n):
        print now
        return
    if (count < countOfMonth):
        wabbits(now, (now + B4))
    elif(count == (countOfMonth)):
        wabbits(now, (now+B4-1))
    else:  #without the long here it gives a wrong number on very large numbers
        wabbits(now, ((now) + (B4) - long(totalWabbitz[count-countOfMonth-1])))

if (n==1):
    print initial
elif (n==2):
    print initial2
elif (n>2):
    wabbits(initial2, (initial2+k))

#print totalWabbitz
