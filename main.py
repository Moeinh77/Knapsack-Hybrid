from collections import namedtuple

Item = namedtuple("Item", "Weight Value isFractional")

InFile=open("IN.TXT","r+")

lines=InFile.readlines()

Items_list=[]

for line in lines:
    i=line.split()
    m=Item(int(i[0]),int(i[1]),int(i[2]))
    Items_list.append(m)

#print(Items_list)


def cmpfunc(ItemX):
    return ItemX.Value/ItemX.Weight

def KnapSack(W,list,N):
    Items_list.sort(key=cmpfunc, reverse=True)



print(Items_list)
