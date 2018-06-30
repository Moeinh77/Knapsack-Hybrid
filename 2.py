# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
from collections import namedtuple

Item = namedtuple("Item", "Weight Value isFractional")

with open("IN2.TXT", "r") as InFile:
    lines = InFile.readlines()

K = [[]]
Items_list = []
for line in lines:
    i = line.split()
    m = Item(int(i[0]), int(i[1]), int(i[2]))
    Items_list.append(m)


def knapSack(Items_list, W, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):

            if i == 0 or w == 0:

                K[i][w] = 0

            elif Items_list[i - 1].Weight <= w:

                K[i][w] = max(Items_list[i - 1].Value + K[i - 1][w - Items_list[i - 1].Weight]
                              , K[i - 1][w])

            elif Items_list[i - 1].Weight > w and Items_list[i - 1].isFractional == 1:

                K[i][w] = max((Items_list[i - 1].Value / Items_list[i - 1].Weight)
                              * (w)
                              , K[i - 1][w])

                print((Items_list[i - 1].Value / Items_list[i - 1].Weight)
                      * (1) + K[i - 1][w]
                      , K[i - 1][w])

            else:
                K[i][w] = K[i - 1][w]
            #  print(K[i][w])

    return K[n][W]


# Driver program to test above function
# val = [10, 17, 10]
# wt = [5, 9, 10]
# b=[0,0,1]
W = 11
n = len(Items_list)
K = knapSack(Items_list, W, n)
# for i in range(n + 1):
#     for w in range(W + 1):
#       if K[i][w]!=0:
#         Items_list.append(i)
# for i in knapsack:
#     for j in Items_list:
#         if(Items_list[j].Value==i):
#              Items_list.remove(j)
#
#
print(K)
# This code is contributed by Bhavya Jain
