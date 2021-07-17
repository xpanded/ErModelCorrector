import model


def checkAttributes(graph, correct):
    for i in graph:
        if (type(i) == model.Node):
            nodeAttributes = i.getAttributes()
            nodename = i.getLabel()
            correctAttributes = getCorrectAttributes(nodename, correct)
            if (correctAttributes is not None):
                controllIfMissing(nodeAttributes, correctAttributes)


def getCorrectAttributes(nodename, correct):
    for y in correct:
        if (y.getLabel() == nodename):
            return y.getAttributes()


def controllIfMissing(nodeAttributes, correctAttributes):
    if (type(nodeAttributes) is None) or (type(correctAttributes) is None):
        return
    if (len(nodeAttributes) > len(correctAttributes)):
        print('too many attributes')

    elif (len(nodeAttributes) < len(correctAttributes)):
        print('attributes missing')

    found = False
    for c in correctAttributes:
        for n in nodeAttributes:
            if (c.getLabel() == n.getLabel()):
                found = True
                print('found', c.getLabel())
        if (found == False):
            print('attribute missing ', c.getLabel())
        found = False


def checkClasses(graph, correct):
    found = False
    for c in correct:
        for i in graph:
            if (type(i) == model.Node and type(c) == model.Node):
                if (i.getLabel() == c.getLabel()):
                    found = True
                    print('class found', c.getLabel())
        if (found == False and type(c) == model.Node ):
            print('class missing ', c.getLabel())
        if (found == False and type(c) == model.Relation):
            print('relationship missing ', c.getLabel())
        found = False
