import time
import tools

global msg
global highlight
global highlight2
global last_highlight

msg = "beginning sort..."
highlight = 0
last_highlight = 0
highlight2 = 0
last_highlight2 = 0


def selection_sort(array):
    """
     Selection sort compares the first element in the array, and each element after it. The smaller one is swapped and placed first.
     After the entire array is iterated, it sorts through the array [1, N], then [2, N] until [N,N]

    :param array: the input array to be sorted
    :return: the sorted input array
    """
    global msg
    global highlight
    global highlight2
    global last_highlight
    global last_highlight2

    highlight = 0
    highlight2 = 0
    last_highlight = 0
    last_highlight2 = 0
    if len(array) == 1:
        msg = "Sorting finished!"
        return

    for i in range(len(array)):
        tools.change_highlight2(i)
        minVal = array[i]
        minIdx = i
        for j in range(i, len(array)):
            tools.change_highlight(j)
            if array[j] < minVal:
                msg = f"({array[j]}) is less than the current smallest number ({minVal})"
                minVal = array[j]
                minIdx = j
            yield array
        tools.change_msg(f"swapping {array[i]} and {array[minIdx]}")
        tools.swap(array, i, minIdx)
        yield array


def bubble_sort(array):
    """
    Bubble sort looks at each element in an array, and the element next to it.
    If the second element is greater than the first element, swap them.
    If the algorithm iterates through each element without a swap occurring, then the array is sorted.
    :param array: the array to be sorted
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
            yield array


def insertion_sort(a):
    """
    In-place insertion sort.
    :param a: array to be sorted, in place
    """

    global msg
    global highlight
    global highlight2
    global last_highlight
    global last_highlight2

    for i in range(1, len(a)):
        j = i
        tools.change_highlight2(i)

        while j > 0 and a[j] < a[j - 1]:
            tools.swap(a, j, j - 1)
            j -= 1
            tools.change_highlight(j)
            yield a
        tools.change_msg(f"Inserted {a[j]} between {a[j-1]} and {a[j + 1]}")