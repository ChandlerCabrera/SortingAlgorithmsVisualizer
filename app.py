import tools
import algorithms
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import PySimpleGUI as sg


if __name__ == "__main__":

    #Setting layout of GUI element
    layout = [
        [sg.Text("Which sorting algorithm would you like to use?")],
        [sg.Radio("Selection Sort", "selection_sort"), sg.Radio("Insertion Sort", "insertion_sort")],
        [sg.Text("Size of array to be sorted"), sg.Slider(range=(1, 50), default_value=50, size=(20, 15),
                                                          orientation='horizontal', font=('Helvetica', 12))],
        [sg.Text("Sorting Speed                "), sg.Slider(range=(1, 100), default_value=50, size=(20, 15),
                                                             orientation='horizontal', font=('Helvetica', 12))],
        [sg.OK()]
    ]
    button, values = sg.FlexForm("GUI").layout(layout).Read()
    print(button)
    print(values)

    # reading information from GUI
    size = int(values[2])
    a = tools.generate_random_list(size)

    sorting_speed = int(105 - values[3])

    if values[0]:
        generator = algorithms.selection_sort(a)
        title = f"Selection Sort of {size} numbers"
    elif values[1]:
        generator = algorithms.insertion_sort(a)
        title = f"Insertion Sort of {size} numbers"

    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rects = ax.bar(range(len(a)), a, align="edge")
    ax.set_xlim(0, size)
    ax.set_ylim(0, 100)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]


    def update_fig(A, rects, i):
        highlight = algorithms.highlight
        highlight2 = algorithms.highlight2
        message = algorithms.msg
        last_highlight = algorithms.last_highlight
        last_highlight2 = algorithms.last_highlight2

        counter = 0
        for rect, val in zip(rects, A):
            rect.set_height(val)
            if counter == highlight:
                rect.set_color('r')
            elif counter == highlight2:
                rect.set_color('g')
            elif counter == last_highlight or counter == last_highlight2:
                rect.set_color('b')

            counter += 1
        i[0] += 1
        text.set_text(message)


    anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects, iteration), frames=generator,
                                   interval=sorting_speed, repeat=False)
    plt.show()
