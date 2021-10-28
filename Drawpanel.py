from tkinter import *
from tkinter.filedialog import askopenfilename

import myParser
import Drawer

Files = [0, 0]
writer = []
scale = 1


def openCorrectFile():
    file = askopenfilename(title='Choose GraphML')
    if file:
        Files.insert(0, file)


def openStudentFile():
    file = askopenfilename(title='Choose GraphML')
    if file:
        Files.insert(1, file)


def correct(my_canvas, t, spinbox):
    t.delete(1.0, END)
    writer = []
    if Files[0] != 0 and Files[1] != 0:
        my_canvas.delete("all")
        sElements, cElements = myParser.parse(Files[1], Files[0])
        myParser.correct(sElements, cElements, writer)
        minX, minY, maxX, maxY = myParser.getMinMax(sElements)
        myParser.normaliseCoordinates(sElements, minX, minY, maxX, maxY)
        num = float(spinbox.get())/100
        myParser.scaleCoordinates(sElements, num)
        Drawer.drawER(my_canvas, sElements)
    t.insert(1.0, writer)


class Main(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("ER Model Error Detection")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Please load the model solution before loading the student's model")
        lbl.grid(sticky=W, pady=4, padx=5)

        my_canvas = Canvas(self, width=1600, height=700, bg="white")
        my_canvas.grid(row=1, column=0, columnspan=2, rowspan=4,
                       padx=5, sticky=E + W + S + N)

        opencorrectbtn = Button(self, text="model solution", command=lambda: openCorrectFile())
        opencorrectbtn.grid(row=1, column=3)

        openstudentbtn = Button(self, text="model student", command=lambda: openStudentFile())
        openstudentbtn.grid(row=2, column=3, pady=4)

        t = Text(self, height=6, width=186)
        t.grid(row=5, column=0)
        s = Scrollbar(self)
        t.config(yscrollcommand=s.set)

        spinbox = Spinbox(self, from_=100, to=250, width=15, textvariable=scale)
        spinbox.grid(row=5, column=3)

        scalelbl = Label(self, text="Insert Zoom in %")
        scalelbl.grid(row=4, column=3)

        correctbtn = Button(self, text="Correct", command=lambda: correct(my_canvas, t, spinbox))
        correctbtn.grid(row=3, column=3)


def main():
    root = Tk()
    root.geometry("1600x840+300+300")
    app = Main()
    root.mainloop()


if __name__ == '__main__':
    main()
