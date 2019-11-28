import time
import tools

global msg
global highlight
global highlight2
global last_highlight
global last_highlight2
global highlight3
global last_highlight3

msg = "beginning sort..."
highlight = 0
last_highlight = 0
highlight2 = 0
last_highlight2 = 0
highlight3 = 0
last_highlight3 = 0

list_recolour = []
list_highlight = []


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

    global msg
    global highlight
    global highlight2
    global last_highlight
    global last_highlight2
    global highlight3
    global last_highlight3

    highlight = 0
    highlight2 = 0
    last_highlight = 0
    last_highlight2 = 0

    n = len(array)
    swapped = True
    x = -1
    iteration = 0

    while swapped:
        swapped = False

        iteration += 1
        x = x + 1

        for i in range(1, n - x):
            if array[i - 1] > array[i]:
                tools.swap(array, i - 1, i)
                swapped = True
                tools.change_msg(f"Iteration ({iteration}). Red Bar: {array[i]}")
                tools.change_highlight(i)
                tools.change_highlight2(n - x)

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
        tools.change_msg(f"Inserted {a[j]} between {a[j - 1]} and {a[j + 1]}")


def merge_sort(xs):
    """Inplace merge sort of array without recursive. The basic idea
    is to avoid the recursive call while using iterative solution.
    The algorithm first merge chunk of length of 2, then merge chunks
    of length 4, then 8, 16, .... , until 2^k where 2^k is large than
    the length of the array
    """

    global msg
    global highlight
    global highlight2
    global last_highlight
    global last_highlight2
    global list_highlight

    highlight = 0
    highlight2 = 0

    last_highlight = 0
    last_highlight2 = 0

    list_highlight = []


    unit = 1
    while unit <= len(xs):
        h = 0
        for h in range(0, len(xs), unit * 2):
            l, r = h, min(len(xs), h + 2 * unit)
            mid = h + unit
            # merge xs[h:h + 2 * unit]
            p, q = l, mid
            while p < mid and q < r:
                # use <= for stable merge merge
                if xs[p] <= xs[q]:
                    p += 1
                    for y in range(h, mid):
                        tools.add_highlight_list(y)
                    tools.change_msg(f"Sorting chunks of array of size {unit*2}, between indexes {h} and {mid}")
                    yield xs
                    tools.clear_highlight_list()
                else:
                    tmp = xs[q]
                    xs[p + 1: q + 1] = xs[p:q]
                    xs[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1
                    for y in range(h, mid):
                        tools.add_highlight_list(y)
                    tools.change_msg(f"Sorting elements in sub-array of size {unit*2}, between indexes {h} and {mid}")
                    yield xs
                    tools.clear_highlight_list()

        unit *= 2

    return xs
