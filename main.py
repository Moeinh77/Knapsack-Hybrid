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
    i=0
    currentValue=0
    remainedWeight=W

    for i in range(0,N):

        if(list[i].Weight<=remainedWeight):

            currentValue+=list[i].Value
            remainedWeight-=list[i].Weight

        else:

            if(list[i].isFractional==1):
                currentValue+=(list[i].Value/list[i].Weight)*remainedWeight
                remainedWeight=0

            else:
                continue


print(Items_list)
