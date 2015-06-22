from random import randint

def randArray():
    array = []

    for i in range(0, 10):
        randnum = randint(1, 100)
        array.append(randnum)
    return array

def bubleSort(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                tmp = array[j]
                array[j] = array[i]
                array[i] = tmp
    return array

array = randArray()
print(array)
array = bubleSort(array)
print("sorted")
print(array)