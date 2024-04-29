import os
import sys
from tkinter import *           ##хуй лалала
from random import randint

coloda = [2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11]
z = randint(2, 11)

count = 0
count_array = []
countt = 0
countt_array = []
ii = 0


def clicked(count=count):
    if sum(count_array) < 21:
        z = randint(0, 12)
        current = coloda[z]

        lbl.configure(text='Вам попалась карта достоинством {0}'.format(current))
        count_array.append(current)

        if sum(count_array) > 21 and (11 in count_array):
            count_array[count_array.index(11)] = 1
        lbll.configure(text='У вас {0} очков и {1}'.format(sum(count_array), count_array))

    if sum(count_array) == 21:
        lbll1.configure(text="очко")
        lbl1.configure(text="очко")

    elif sum(count_array) > 21:
        lbll.configure(text='У вас {0} очков и {1}, перебор'.format(sum(count_array), count_array))
        lbll1.configure(text="ты проиграл компьютеру клоун")
        lbl1.configure(text="ты проиграл компьютеру клоун")

    return sum(count_array)


def clicked1(countt=countt, ii=ii):
    if sum(count_array) < 21 and ii == 0:
        while sum(countt_array) < 21 and countt <= sum(count_array):
            z = randint(0, 12)
            currentt = coloda[z]
            ii += 1
            countt_array.append(coloda[z])
            countt += currentt

            if sum(countt_array) > 21 and (11 in countt_array):
                count_array[countt_array.index(11)] = 1
            lbl1.configure(text="не столе {0} в сумме {1}".format(countt_array, countt))

            if countt > 21:
                lbll1.configure(text="ты победил компьютеп, радуйся")
            else:
                lbll1.configure(text="ты проиграл компьютеру клоун")
        return countt_array


def clicked2():
    python = sys.executable
    os.execl(python, python, *sys.argv)


window = Tk()
window.title("21 (слей последние деньги боту)")
w = 600
h = 200
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

lbl = Label(window, text=' ')
lbl.grid(column=0, row=0)
lbll = Label(window, text=' ')
lbll.grid(column=0, row=1)
btn = Button(window, text="В руку", command=clicked)
btn.grid(column=0, row=2)

lbl1 = Label(window, text=' ')
lbl1.grid(column=2, row=0)
lbll1 = Label(window, text=' ')
lbll1.grid(column=2, row=1)
btn1 = Button(window, text="Крупье", command=clicked1)
btn1.grid(column=2, row=2)

btn2 = Button(window, text="СЪИГРАТЬ", command=clicked2)
btn2.grid(column=1, row=3)

window.mainloop()
