<<<<<<< HEAD
import tools
import algorithms
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import PySimpleGUI as sg

if __name__ == "__main__":

    # Setting layout of GUI element

    layout = [
        [sg.Text("Sorting Speed "), sg.Slider(range=(1, 100), default_value=50, size=(20,15), orientation='horizontal')],
        [sg.Text("Array size    "), sg.Slider(range=(1, 100), default_value=50, size=(20,15), orientation='horizontal')],
        [sg.Button("Bubble Sort"), sg.Button("Insertion Sort"), sg.Button("Merge Sort"), sg.Button("Selection Sort")],
        [sg.Radio("Study Mode", "study_mode")]
    ]

    # Drawing GUI window
    window = sg.FlexForm("Window", layout)

    # parsing information from GUI
    button, values = window.Read()

    # closing window on OK
    window.close()

    # # for debugging and implementation
    # print(button)
    # print(values)

    sorting_method = button

    algorithms.delay = 1 if values[len(values)-1] else 0

    # reading information from GUI
    size = int(values[len(values)-2])
    a = tools.generate_random_list(size)
    sorting_speed = int(105 - values[len(values)-3])
    if sorting_method == "Selection Sort":
        generator = algorithms.selection_sort(a)
        title = f"Selection Sort of {size} numbers"
    elif sorting_method == "Insertion Sort":
        generator = algorithms.insertion_sort(a)
        title = f"Insertion Sort of {size} numbers"
    elif sorting_method == "Bubble Sort":
        generator = algorithms.bubble_sort(a)
        title = f"Bubble Sort of {size} numbers"
    elif sorting_method == "Merge Sort":
        generator = algorithms.merge_sort(a)
        title = f"Merge Sort of {size} numbers"

    # Generating bar graph
    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rects = ax.bar(range(len(a)), a, align="edge", color="#61b0ff")
    ax.set_xlim(0, size)
    ax.set_ylim(0, 100)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]

    def update_fig(A, rects, i):
        """
        Updates the bar graph after each iteration of sort.
        highlight: highlight the first iterating rectangle
        highlight2: highlight the secon iterating rectangle
        last_highlight(1/2): previously highlighted rectangles

        counter tracks with rectangle is being updated, and is the main variable controlling which rectangles are
        going to highlighted

        :param A: data to be graphed
        :param rects: rectangles
        :param i: literally no idea what i is
        """
        message = algorithms.msg

        highlight = algorithms.highlight
        highlight2 = algorithms.highlight2
        highlight3 = algorithms.highlight3

        last_highlight = algorithms.last_highlight
        last_highlight2 = algorithms.last_highlight2
        last_highlight3 = algorithms.last_highlight3

        list_recolour = algorithms.list_recolour
        list_highlight = algorithms.list_highlight

        list_recolour2 = algorithms.list_recolour2
        list_highlight2 = algorithms.list_highlight2
        counter = 0

        for rect, val in zip(rects, A):
            rect.set_height(val)
            if counter == highlight:
                rect.set_color('r')
            elif counter == highlight2:
                rect.set_color("#03fc2c")
            elif counter == highlight3:
                rect.set_color('#fbff00')
            elif counter == last_highlight or counter == last_highlight2 or counter == last_highlight3:
                rect.set_color("#61b0ff")
            elif counter in list_highlight:
                rect.set_color("#d900ff")
            elif counter in list_highlight2:
                rect.set_color('b')
            elif counter in list_recolour or list_recolour2:
                rect.set_color("#61b0ff")

            counter += 1
        i[0] += 1
        text.set_text(message)


    anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects, iteration), frames=generator,
                                   interval=sorting_speed, repeat=False)
    plt.show()
=======
import tools
import algorithms
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import PySimpleGUI as sg


if __name__ == "__main__":
    # Setting layout of GUI element

    layout = [
        [sg.Text("Sorting Speed "), sg.Slider(range=(1, 100), default_value=50, size=(20,15), orientation='horizontal')],
        [sg.Text("Array size    "), sg.Slider(range=(1, 100), default_value=50, size=(20,15), orientation='horizontal')],
        [sg.Button("Bubble Sort"), sg.Button("Insertion Sort"), sg.Button("Merge Sort"), sg.Button("Selection Sort")],
        [sg.Radio("Study Mode", "study_mode")]
    ]

    # Drawing GUI window
    window = sg.FlexForm("Window", layout)

    # parsing information from GUI
    button, values = window.Read()

    if button is None:
        exit()

    # closing window on OK
    window.close()

    # # for debugging and implementation
    # print(button)
    # print(values)
    # print(event)

    sorting_method = button

    algorithms.delay = 1 if values[len(values)-1] else 0

    # reading information from GUI
    size = int(values[len(values)-2])
    a = tools.generate_random_list(size)
    sorting_speed = int(105 - values[len(values)-3])
    if sorting_method == "Selection Sort":
        generator = algorithms.selection_sort(a)
        title = f"Selection Sort of {size} numbers"
    elif sorting_method == "Insertion Sort":
        generator = algorithms.insertion_sort(a)
        title = f"Insertion Sort of {size} numbers"
    elif sorting_method == "Bubble Sort":
        generator = algorithms.bubble_sort(a)
        title = f"Bubble Sort of {size} numbers"
    elif sorting_method == "Merge Sort":
        generator = algorithms.merge_sort(a)
        title = f"Merge Sort of {size} numbers"

    # Generating bar graph
    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rects = ax.bar(range(len(a)), a, align="edge", color="#61b0ff")
    ax.set_xlim(0, size)
    ax.set_ylim(0, 100)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]

    def update_fig(A, rects, i):
        """
        Updates the bar graph after each iteration of sort.
        highlight: highlight the first iterating rectangle
        highlight2: highlight the secon iterating rectangle
        last_highlight(1/2): previously highlighted rectangles

        counter tracks with rectangle is being updated, and is the main variable controlling which rectangles are
        going to highlighted

        :param A: data to be graphed
        :param rects: rectangles
        :param i: literally no idea what i is
        """
        message = algorithms.msg

        highlight = algorithms.highlight
        highlight2 = algorithms.highlight2
        highlight3 = algorithms.highlight3

        last_highlight = algorithms.last_highlight
        last_highlight2 = algorithms.last_highlight2
        last_highlight3 = algorithms.last_highlight3

        list_recolour = algorithms.list_recolour
        list_highlight = algorithms.list_highlight

        list_recolour2 = algorithms.list_recolour2
        list_highlight2 = algorithms.list_highlight2
        counter = 0

        for rect, val in zip(rects, A):
            rect.set_height(val)
            if counter == highlight:
                rect.set_color('r')
            elif counter == highlight2:
                rect.set_color("#03fc2c")
            elif counter == highlight3:
                rect.set_color('#fbff00')
            elif counter == last_highlight or counter == last_highlight2 or counter == last_highlight3:
                rect.set_color("#61b0ff")
            elif counter in list_highlight:
                rect.set_color("#d900ff")
            elif counter in list_highlight2:
                rect.set_color('b')
            elif counter in list_recolour or list_recolour2:
                rect.set_color("#61b0ff")

            counter += 1
        i[0] += 1
        text.set_text(message)


    anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects, iteration), frames=generator,
                                   interval=sorting_speed, repeat=False)
    plt.show()
>>>>>>> Added exit() on "x-ing" of the GUI window
