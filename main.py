from collections import namedtuple

Item = namedtuple("Weight_Value", "Weight Value isFractional")

InFile=open("IN.TXT","r+")

lines=InFile.readlines()

for line in lines:
    i=line.split()
    m=Item(i[0],i[1],i[2])
    print(m)