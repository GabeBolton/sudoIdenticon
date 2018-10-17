# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 17:32:29 2018

@author: Gabe Bolton
"""

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

plt.set_cmap(cm.Greens)
plt.axis('off')


def stringMaker():
    inString=input("What string do you want to represent: ")
    length = len(inString)
    divisable = False
    divisability=[]
    for i in range(1,length+1):
        if length % i==0:
            divisable=True
            divisability.append(str(i)+','+str(int(length/i)))
    if divisable==True:
        print('Possible column/row combinations:')
        print(divisability)
    else:
        print('No nice column/row combinations appear to be possible other than n by 1 (or 1 by n), consider padding your string')
    goOn=input('Do you want to pad and try again? y/n  ')
    if (goOn=='y'):
        stringMaker()
    return inString
            
inString=stringMaker()

columns = int(input('columns: '))
rows = int(input('rows: '))
gridX=[]
gridY=[]
i=0
while i<rows:
    j=0
    while j<columns:
        gridX.append(j)
        gridY.append(i)
        j+=1
    i+=1
data=np.zeros([(max(gridY)+1)*3,(max(gridX)+1)*3])

def characterGrid(character):
    ringString=format(ord(character),'b')
    ringString='{:0>8}'.format(ringString)

    return np.array([[float(ringString[0]),float(ringString[1]),float(ringString[2])],
               [float(ringString[3]),float(ord(character)/255),float(ringString[4])],
               [float(ringString[5]),float(ringString[6]),float(ringString[7])]])


def gridGrid(character,x,y):
    x=x*3
    y=y*3
    grid=characterGrid(character)
    print(grid)
    #plt.imshow(grid)
    data[y:(y+3),x:(x+3)] = grid
    #plt.imshow(data)

i=0
while i <len(gridX):
    gridGrid(inString[i],gridX[i],gridY[i])
    i+=1
plt.imshow(data)

for x in inString:
    grid=characterGrid(x)
    print(grid)

plt.imshow(data)

plt.show()

if input('Save Image? y/n ')=='y':
    fig = plt.figure()
    fig.set_size_inches([data.shape[1],data.shape[0]])
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(data, aspect='equal')
    plt.savefig(fname=input('Where? '), dpi=100)


def deGrid(gridMajor):
    print("Degridding:")
    outString=''
    gridMajor=data
    y=0
    while y < gridMajor.shape[0]:
        x=0
        while x < gridMajor.shape[1]:
            ringString=''
            gridMinor=gridMajor[y:(y+3),x:(x+3)]
            i=0
            while i < 3:
                j=0
                while j<3:
                    if not((i==1)&(j==1)):
                        ringString+=(str(int(gridMinor[i][j])))
                    j+=1
                i+=1
                    
            print(ringString)
            outString+=chr(int(ringString,2))
            x+=3
        y+=3
    print(outString)

deGrid(data)
