"""
compare s1 and s2, if they have same letter return True else False
small case and same length
"""

# n^2
def anagramSolution1(s1, s2):
    alist = list(s2)
    pos = 0
    stillOK = True
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            alist[pos2] = None
        else:
            stillOK = False
        pos1 = pos1 + 1
    return stillOK

# log(n)
def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)
    return alist1.sort() == alist2.sort()

# n
def anagramSolution3(s1, s2):
    c = [0] * 26
    for i in range(len(s1)):
        pos1 = ord(s1[i]) - ord('a')
        pos2 = ord(s2[i]) - ord('a')
        c[pos1] += 1
        c[pos2] -= 1
    return sum(c) == 0

print(anagramSolution2("heart", "earth"))
print(anagramSolution3("heart", "earth"))