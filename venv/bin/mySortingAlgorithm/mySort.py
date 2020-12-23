import numpy as np

#O(n^2) stable
def bubbleHelper(li, i, end):
    if i > end:
        return li
    else:
        li[i], li[i+1] = min(li[i], li[i+1]), max(li[i], li[i+1])
        bubbleHelper(li, i+1, end)

def bubbleSort(li):
    for end in range(len(li)-1)[::-1]:
        bubbleHelper(li, 0, end)
    return li

def bubbleSort2(li):
    for end in range(len(li))[::-1]:
        count = 0
        for i in range(end):
            li[i], li[i + 1] = min(li[i], li[i + 1]), max(li[i], li[i + 1])
            count += 1
        if count == 0:
            break
    return li

####################################################

#O(n^2) unstable

def selectSort(li):
    if len(li) < 2:
        return li
    else:
        for j in range(len(li)):
            minIndex = j
            for i in range(j, len(li)):
               if li[minIndex] > li[i]:
                   minIndex = i
            li[minIndex], li[j] = li[j], li[minIndex]
    return li

##################################################
#O(n^2) stable

def insertSort(li):
    for j in range(1, len(li)):
        i = j
        while i > 0:
            if li[i] < li[i-1]:
                li[i], li[i-1] = li[i-1], li[i]
                i -= 1
            else:
                break
    return li

##################################################
#O(nlogn) unstable

def quickSort2Helper(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort2(arr, low, high):
    if low < high:
        pi = quickSort2Helper(arr, low, high)
        quickSort2(arr, low, pi-1)
        quickSort2(arr, pi+1, high)

def quickSort(li, left, right):
    if left >= right:
        return
    low = left
    high = right
    mid = li[low]
    while left < right:
        while left < right and li[right] > mid:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= mid:
            left += 1
        li[right] = li[left]
    li[right] = mid
    quickSort(li, low, left-1)
    quickSort(li, left+1, high)

##################################################
# O(nlogn) to O(n^2) unstable

def shellSort(li):
    n = len(li)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while (i-gap) >= 0:
                if li[i] < li[i-gap]:
                    li[i], li[i-gap] = li[i-gap], li[i]
                    i -= gap
                else:
                    break
        gap //= 2

##################################################
#O(nlogn) stable

def mergeSort(arr):
    if len(arr)<2:
        return arr
    middle = len(arr) // 2
    left, right = arr[0:middle], arr[middle:]
    return mergeHelper(mergeSort(left), mergeSort(right))

def mergeHelper(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result




##################################################
if __name__ == "__main__":
    li = np.random.randint(10, size=10).tolist()
    print(li)
    # print(bubbleSort2(li))
    # print(selectSort(li))
    # print(insertSort(li))
    #quickSort(li, 0, len(li)-1)
    mergeSort(li)
    print(li)