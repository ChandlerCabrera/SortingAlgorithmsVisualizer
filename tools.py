def swap(input_list, i, j):
    """
    :param input_list: the list in which the elements are to be swapped
    :param i: the index of the first element to be swapped
    :param j: the index of the second element to be swapped
    :return: the original list, but with the elements at each index swapped
    """
    temp = input_list[i]
    print(f"swapping {input_list[i]} and {input_list[j]}")
    input_list[i] = input_list[j]
    input_list[j] = temp
    return


def insertion_shift(arr, j):
    save = arr[j]
    print(f"saving value: {save}")
    for a in range(0, j - 1):
        arr[a + 1] = arr[a]
    arr[0] = save
