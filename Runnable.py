from random import randint

import algorithms


class Constraints:
    int_range = 100
    size_of_list = 10


def main():
    list = [None] * Constraints.size_of_list
    for i in range(0, Constraints.size_of_list):
        list[i] = randint(0, Constraints.int_range)

    print(f"unsorted numbers: {list}")
    algorithms.merge_sort(list)
    print(f"sorted numbers: {list}")


if __name__ == "__main__":
    main()
