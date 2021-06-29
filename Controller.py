import PySimpleGUI as sg
import os

# First the window layout in 2 columns


file_list_column = [
    [
        sg.Text("GraphML Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER1-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(80, 40), key="-FILELIST1-")
    ]
]

# For now will only show the name of the file that was chosen

image_viewer_column = [
    [
        sg.Text("Solution"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER2-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(80, 40), key="-FILELIST2-")
    ]
]

# ----- Full layout -----

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("GraphCorrector", layout)

# Run the Event Loop

while True:

    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # Folder name was filled in, make a list of files in the folder

    if event == "-FOLDER1-":
        folder = values["-FOLDER1-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
               and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILELIST1-"].update(fnames)
    elif event == "-FILELIST1-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER1-"], values["-FILELIST1-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass

window.close()
