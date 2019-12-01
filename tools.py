import random
import app
import algorithms
import time


def swap(input_list, i, j):
    """
    :param input_list: the list in which the elements are to be swapped
    :param i: the index of the first element to be swapped
    :param j: the index of the second element to be swapped
    :return: the original list, but with the elements at each index swapped
    """

    temp = input_list [i]
    # change_msg(f"swapping {input_list[i]} and {input_list[j]}")
    input_list [i] = input_list [j]
    input_list [j] = temp
    return


def change_msg(string):
    algorithms.msg = string


def change_highlight(i):
    algorithms.last_highlight = algorithms.highlight
    algorithms.highlight = i


def change_highlight2(i):
    algorithms.last_highlight2 = algorithms.highlight2
    algorithms.highlight2 = i


def change_highlight3(i):
    algorithms.last_highlight3 = algorithms.highlight3
    algorithms.highlight3 = i


def add_highlight_list(i):
    algorithms.list_highlight.append(i)


def add_highlight_list2(i):
    algorithms.list_highlight2.append(i)


def clear_highlight_list():
    algorithms.list_recolour = algorithms.list_highlight
    algorithms.list_highlight = []


def clear_highlight_list2():
    algorithms.list_recolour2 = algorithms.list_highlight2
    algorithms.list_highlight2 = []


def insertion_shift(arr, j):
    save = arr [j]
    print(f"saving value: {save}")
    for a in range(0, j - 1):
        arr [a + 1] = arr [a]
    arr [0] = save


def generate_random_list(n):
    result = []
    for i in range(0, n):
        result.append(random.randint(1, 100))
    print(result)

    return result
