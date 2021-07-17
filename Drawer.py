import model


def drawNode(my_canvas, attribute):
    x, y = attribute.getCoordinates()
    text = attribute.getLabel()
    my_canvas.create_rectangle(x, y, x + 75, y + 20, fill='cyan')
    my_canvas.create_text(x + 2, y + 2, text=text, anchor='nw')


def drawAttribute(my_canvas, attribute):
    x, y = attribute.getCoordinates()
    text = attribute.getLabel()
    my_canvas.create_oval(x, y, x + 86, y + 30, fill='cyan')
    my_canvas.create_text(x + 10, y + 9, text=text, anchor='nw')


def drawRelation(my_canvas, attribute):
    x, y = attribute.getCoordinates()
    text = attribute.getLabel()

    my_canvas.create_line(x + 60, y, x + 120, y + 15, fill='red')
    my_canvas.create_line(x + 120, y + 15, x + 60, y + 30, fill='red')
    my_canvas.create_line(x + 60, y + 30, x, y + 15, fill='red')
    my_canvas.create_line(x, y + 15, x + 60, y, fill='red')

    my_canvas.create_text(x + 12, y + 8, text=text, anchor='nw')


def drawER(my_canvas, alElements):
    for i in alElements:
        if (type(i) == model.Node):
            drawNode(my_canvas, i)
        elif (type(i) == model.Attribute):
            drawAttribute(my_canvas, i)
        elif (type(i) == model.Relation):
            drawRelation(my_canvas, i)
