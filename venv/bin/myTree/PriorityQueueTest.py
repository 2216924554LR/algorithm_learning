from PriorityQueue import  *
import numpy as np

np.random.seed(0)
myList = np.random.randint(20, size=10).tolist()
myHeap = BinHeap()
myHeap.buildHeap(myList)
myHeap.insert(2)
print(myHeap.heapList)

temp = [0]
t = myHeap.currentSize
for i in range(t):
    temp.append(myHeap.delMin())
myHeap.heapList = temp

print(myHeap.heapList)