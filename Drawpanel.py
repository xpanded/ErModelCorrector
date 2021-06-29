from tkinter.filedialog import askopenfilename
from tkinter import *


def draw(my_canvas):
    my_canvas.create_line(0, 0, 300, 200, fill='red')
    my_canvas.create_line(150, 0, 150, 200, fill='red')

    my_canvas.create_rectangle(0, 0, 80, 50, fill='pink')
    my_canvas.create_oval(50, 150, 250, 50, fill='cyan')
    my_canvas.create_text(150, 100, text='Attribute')


def open_file():
    file = askopenfilename(title='Choose GraphML', filetype=[("GraphML File", "*.graphml")])
    if file:
        read_graphML = open(file, 'r')
        out = read_graphML.read()


class Example(Frame):

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
        draw(my_canvas)

        abtn = Button(self, text="Musterlösung", command=lambda: open_file())
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text="Close")
        cbtn.grid(row=2, column=3, pady=4)

        hbtn = Button(self, text="HELP")
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="OK")
        obtn.grid(row=5, column=3)


def main():
    root = Tk()
    root.geometry("1600x840+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
