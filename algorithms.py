import Runnable
import tools


def selection_sort(array):
    """
     Selection sort compares the first element in the array, and each element after it. The smaller one is swapped and placed first.
     After the entire array is iterated, it sorts through the array [1, N], then [2, N] until [N,N]

    :param array: the input array to be sorted
    :return: the sorted input array
    """

    starting_index = 0
    while starting_index != len(array) - 1:
        for i in range(starting_index + 1, len(array)):
            if array[i] < array[starting_index]:
                tools.swap(array, starting_index, i)
        starting_index += 1
        print(array)


def bubble_sort(array):
    """
    Bubble sort looks at each element in an array, and the element next to it.
    If the second element is greater than the first element, swap them.
    If the algorithm iterates through each element without a swap occurring, then the array is sorted.
    :param array: the array to be sorted
    :return: the sorted array, using bubble sort
    """
    swap_occurred = True

    while swap_occurred:
        swap_occurred = False
        for i in array[0:len(array) - 1]:
            j = array[i + 1]
            if i > j:
                tools.swap(array, i, j)
                print("swap has occurred")
                swap_occurred = True


def insertion_sort(array):
    for i in range(1, len(array)):
        chosen = array[i]
        j = i - 1
        while j >= 0 and chosen < array[j]:
            array[j + 1] = array[j]
            print(array)
            j -= 1
        array[j + 1] = chosen


def merge_sort(array):
    """
    recursively sub-divided the input array into two halves, until each sub-array is size 1
    then iterate and compare each element to put them back together again
    :param array:
    :return:
    """
    if len(array) > 1:
        mid = len(array) // 2
        L_sub = array[:mid]
        R_sub = array[mid:]

        merge_sort(L_sub)
        merge_sort(R_sub)

        i = j = k = 0

        while i < len(L_sub) and j < len(R_sub):
            if L_sub[i] < R_sub[j]:
                array[k] = L_sub[i]
                i += 1
            else:
                array[k] = R_sub[j]
                j += 1
            k += 1

        while i < len(L_sub):
            array[k] = L_sub[i]
            i += 1
        while j < len(R_sub):
            array[k] = R_sub[j]
            j += 1
