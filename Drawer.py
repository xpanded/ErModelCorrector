import model


def drawNode(my_canvas, attribute):
    x, y = attribute.getCoordinates()
    text = attribute.getLabel()
    my_canvas.create_rectangle(x, y, x + 75, y + 20, fill='#ccffff')
    my_canvas.create_text(x + 2, y + 2, text=text, anchor='nw')


def drawAttribute(my_canvas, attribute):
    x, y = attribute.getCoordinates()
    text = attribute.getLabel()
    underline = attribute.getPrimary()
    my_canvas.create_oval(x, y, x + 86, y + 30, fill='#ccffff')
    my_canvas.create_text(x + 10, y + 9, text=text, anchor='nw')
    if (underline):
        my_canvas.create_line(x + 8, y + 22, x + 78, y+22, fill='black')


def drawRelation(my_canvas, relation):
    x, y = relation.getCoordinates()
    text = relation.getLabel()

    my_canvas.create_rectangle(x, y + 8, x + 80, y + 24, fill='white', outline='white')
    my_canvas.create_line(x + 28, y, x + 88, y + 15, fill=relation.getColor())
    my_canvas.create_line(x + 88, y + 15, x + 28, y + 30, fill=relation.getColor())
    my_canvas.create_line(x + 28, y + 30, x - 32, y + 15, fill=relation.getColor())
    my_canvas.create_line(x - 32, y + 15, x + 28, y, fill=relation.getColor())

    my_canvas.create_text(x, y + 8, text=text, anchor='nw')


def drawEdge(my_canvas, edge):
    x1, y1 = edge.getTarget().getCoordinates()
    x2, y2 = edge.getSource().getCoordinates()

    my_canvas.create_line(x1 + 20, y1 + 20, x2 + 20, y2 + 20, fill=edge.getColor())

    if (edge.getLabel() != ''):
        helperCardinality(my_canvas, edge)
    if (edge.getArrowTarget()):
        helperArrow(my_canvas, edge, target=True)
    if (edge.getArrowSource()):
        helperArrow(my_canvas, edge, target=False)


def drawER(my_canvas, alElements):
    for i in reversed(alElements):
        if (type(i) == model.Node):
            drawNode(my_canvas, i)
        elif (type(i) == model.Attribute):
            drawAttribute(my_canvas, i)
        elif (type(i) == model.Relation):
            drawRelation(my_canvas, i)
        elif (type(i) == model.Edge):
            drawEdge(my_canvas, i)


def helperArrow(my_canvas, edge, target):
    x1, y1 = edge.getTarget().getCoordinates()
    x2, y2 = edge.getSource().getCoordinates()
    if (target != True):
        x1, y1 = edge.getSource().getCoordinates()
        x2, y2 = edge.getTarget().getCoordinates()
    xm, ym = x2, y2
    m, p = calculateLine(edge)

    if (m == None and y2 > y1):
        ym = ym - ((y2 - y1) / 2) - 20
        my_canvas.create_line(xm + 20, ym + 20, x2 + 20, y2 + 20, fill=edge.getColor(), arrow='first')
    elif (m == None and y2 < y1):
        ym = ym + ((y2 - y1) / 2) + 20
        my_canvas.create_line(xm + 20, ym + 20, x1 + 20, y1 + 20, fill=edge.getColor(), arrow='first')
    elif (m == 0 and x1 < x2):
        xm = xm - 50
        my_canvas.create_line(xm + 20, ym + 20, x1 + 20, y1 + 20, fill=edge.getColor(), arrow='first')
    elif (m == 0 and x1 > x2):
        xm = x1 - 50
        my_canvas.create_line(xm + 20, ym + 20, x2 + 20, y2 + 20, fill=edge.getColor(), arrow='first')
    else:
        if (x1 > x2):
            while (calculateDisctance(x2, y2, xm, ym) < 50):
                xm = xm * 1.001
                ym = m * xm + p
            my_canvas.create_line(xm + 20, ym + 20, x2 + 20, y2 + 20, fill=edge.getColor(), arrow='first')
        else:
            while (calculateDisctance(x2, y2, xm, ym) < 50):
                xm = xm * 0.999
                ym = m * xm + p
            my_canvas.create_line(xm + 20, ym + 20, x2 + 20, y2 + 20, fill=edge.getColor(), arrow='first')


def calculateDisctance(x, y, x2, y2):
    helper = pow((x - x2), 2) + pow((y - y2), 2)
    distance = pow(helper, 0.5)
    return distance


def calculateLine(edge):
    x1, y1 = edge.getTarget().getCoordinates()
    x2, y2 = edge.getSource().getCoordinates()

    xm = x2 - x1
    ym = y2 - y1
    m = None
    p = None
    if (xm != 0):
        m = ym / xm
        p = (-1 * x1 * m) + y1
    return m, p


def helperCardinality(my_canvas, edge):
    x1, y1 = edge.getTarget().getCoordinates()
    x2, y2 = edge.getSource().getCoordinates()

    xm = x2 - x1
    m, p = calculateLine(edge)
    xcardinality = x1 + xm / 2
    ycardinality = xcardinality * m + p
    my_canvas.create_rectangle(xcardinality + 10, ycardinality + 10, xcardinality + 38, ycardinality + 24, fill='white',
                               outline='white')
    my_canvas.create_text(xcardinality + 10, ycardinality + 10, text=edge.getLabel(), anchor='nw', fill=edge.getColor())
