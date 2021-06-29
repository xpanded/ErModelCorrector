import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as ET

root = tk.Tk()

canvas = tk.Canvas(root, width=800, height=600)
canvas.grid(columnspan=2, rowspan=3)

def text2XML(filename):
    tree = ET.parse(filename)
    root =tree.getroot()

    for child in root:
        print(child.tag, child.attrib)


#instructions
inst = tk.Label(root, text="Select a GraphML file ")
inst.grid(columnspan=2, column=0, row=0)

def open_file():
    browse_text.set('loading...')
    file = askopenfilename(parent=root, title='Choose GraphML', filetype=[("GraphML File", "*.graphml")])
    if file:
        text2XML(file)
        read_graphML = open(file,'r')
        out = read_graphML.read()
        text_box = tk.Text(root,height=50,width=80,padx=15,pady=15)
        text_box.insert(1.0, out)
        text_box.tag_add("center",1.0,"end")
        text_box.grid(column=1, row=2)

    browse_text.set('Browse')

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, command=lambda:open_file(), textvariable=browse_text, bg='#20bebe', fg='white', height=2, width=10)
browse_text.set("Browse")
browse_btn.grid(column=1, row=1)



root.mainloop()