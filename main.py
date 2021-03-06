# exaples : IN => capacity 10 and capacity 12
#           last item 0 isfractional and capacity 1

#           IN2=> capacity 4 and 3 and 5

from collections import namedtuple

Item = namedtuple("Item", "Weight Value isFractional")

with open("IN2.TXT", "r") as InFile:
    lines = InFile.readlines()

Items_list = []
KnapSack_list=[]
fractionated=None

for line in lines:
    i = line.split()
    m = Item(int(i[0]), int(i[1]), int(i[2]))
    Items_list.append(m)

print("\n***Items available : ")
print(Items_list)


def cmpfunc(ItemX):
    return ItemX.Value / ItemX.Weight


def KnapSack(W, list, N):
    global fractionated
    Items_list.sort(key=cmpfunc, reverse=True)

    # print("\nList sorted by value per weight:")
    # print(Items_list)

    currentValue = 0
    remainedWeight = W

    for i in range(0, N):

        if (list[i].Weight <= remainedWeight):

            currentValue += list[i].Value
            remainedWeight -= list[i].Weight
            KnapSack_list.append(list[i])

        else:

            if remainedWeight == 0:
                break

            if list[i].isFractional == 1:

                currentValue += (list[i].Value / list[i].Weight) * remainedWeight
                KnapSack_list.append(list[i])
                fractionated=i
                break

            else:
                continue

    return currentValue



W = int(input("\nEnter the MAXIMUM capacity of the KNAPSACK: "))

Maxval=KnapSack(W, Items_list, len(Items_list))

if not KnapSack_list:
    print("Sorry your bag is just too small!\nCould'nt take anything")
else:
    print("\n***Taken items:")
    print(KnapSack_list)

if(fractionated!=None):
    print("\n"+str(Items_list[fractionated])+ " is Fractionated!!!")

print("\nMax value that can be collected: " + str(Maxval))