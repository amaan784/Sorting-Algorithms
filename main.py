def bubbleSort(unsortedList):
    """
    Time complexity: O(n^2)
    We iterate through the list
    We keep on comparing the current element with the next element
    If the current element is larger than the next element then we swap them

    :param unsortedList: an unsorted list
    :return: a sorted list
    """
    for i in range(len(unsortedList)-1):
        for j in range(len(unsortedList)-1):
            if unsortedList[j] > unsortedList[j+1]:
                temp = unsortedList[j]
                unsortedList[j] = unsortedList[j+1]
                unsortedList[j+1] = temp
    return unsortedList


def insertionSort(unsortedList):
    pass

def selectionSort():
    pass

def quickSort():
    pass


def mergeSort():
    pass

def shellSort():
    pass


def heapSort():
    pass


if __name__ == '__main__':
    l = [1, 21, 9, 8, 7, 101, 2022, 2, 3, 1]
    print(bubbleSort(l))


# UNDERSTAND AND IMPLEMENT THE MENTIONED SORTING ALGORITHMS
# WRITE EXPLAINATIONS
# PUT EVERY ALGORITHM IN A SEPERATE FILE
# POSSIBLE EACH ONE MAY HAVE DIFFERENT VERSIONS (IMPLEMENT AS MANY AS POSSIBLE)