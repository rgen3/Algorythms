__author__ = 'Александр'

from random import randint

def randArray():
    array = []

    for i in range(0, 10):
        randnum = randint(1, 100)
        array.append(randnum)

    return array

def merge(aLeft, aRight):
    left_indx = 0
    right_indx = 0
    result = []
    while left_indx < len(aLeft) and right_indx < len(aRight):
        if aLeft[left_indx] <= aRight[right_indx]:
            result.append(aLeft[left_indx])
            left_indx += 1
        else:
            result.append(aRight[right_indx])
            right_indx += 1

    if left_indx < len(aLeft):
        result.extend(aLeft[left_indx:])

    if right_indx < len(aRight):
        result.extend(aRight[right_indx:])
    return result

def mergeSort(aList):
    if len(aList) <= 1:
        return aList
    middle = len(aList) // 2
    leftPart = mergeSort(aList[middle:])
    rightPart = mergeSort(aList[:middle])
    return list(merge(leftPart, rightPart))


array = randArray()
sorted = mergeSort(array)
print(array)
print(sorted)

