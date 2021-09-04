from tkinter.filedialog import askopenfilename
from tkinter import *

import myParser
import Drawer

Files = [0, 0]
writer = []


def drawH(my_canvas, alElements):
    my_canvas.delete("all")
    minX, minY, maxX, maxY = myParser.getMinMax(alElements)
    myParser.normaliseCoordinates(alElements, minX, minY, maxX, maxY)
    Drawer.drawER(my_canvas, alElements)



def openCorrectFile():
    file = askopenfilename(title='Choose GraphML', filetype=[("GraphML File", "*.graphml")])
    if file:
        Files.insert(0, file)


def openStudentFile():
    file = askopenfilename(title='Choose GraphML', filetype=[("GraphML File", "*.graphml")])
    if file:
        Files.insert(1, file)


def correct(my_canvas,t):
    print(Files[0])
    print(Files[1])
    if Files[0] != 0:
        alElements, cElements = myParser.correct(Files[1], Files[0], writer)
        drawH(my_canvas, alElements)
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

        lbl = Label(self, text="Name des Studenten")
        lbl.grid(sticky=W, pady=4, padx=5)

        my_canvas = Canvas(self, width=1600, height=700, bg="white")
        my_canvas.grid(row=1, column=0, columnspan=2, rowspan=4,
                       padx=5, sticky=E + W + S + N)

        abtn = Button(self, text="model solution", command=lambda: openCorrectFile())
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text="model student", command=lambda: openStudentFile())
        cbtn.grid(row=2, column=3, pady=4)

        t = Text(self, height=6, width=186)
        t.grid(row=5, column=0)
        s = Scrollbar(self)
        t.config(yscrollcommand=s.set)

        hbtn = Button(self, text="Correct", command=lambda: correct(my_canvas,t))
        hbtn.grid(row=3, column=3)




def main():
    root = Tk()
    root.geometry("1600x840+300+300")
    app = Main()
    root.mainloop()


if __name__ == '__main__':
    main()
