from BinSearchTree import *
mytree = BinarySearchTree()
mytree[3] = "red"
mytree[4] = "blue"
mytree[6] = "yellow"
mytree[2] = "at"

print(len(mytree))
print(mytree[6])
print(mytree.get(6))
print(6 in mytree)
for key in mytree:
    print(key, mytree[key])
