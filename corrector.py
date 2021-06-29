import model


def checkAttributes(graph, correct):
    for i in graph:
        if (type(i) == model.Node):
            nodeAttributes = i.getAttributes()
            nodename = i.getLabel()
            correctAttributes = getCorrectAttributes(nodename, correct)

            controllIfMissing(nodeAttributes, correctAttributes)


def getCorrectAttributes(nodename, correct):
    for y in correct:
        if (y.getLabel() == nodename):
            return y.getAttributes()


def controllIfMissing(nodeAttributes, correctAttributes):
    if (len(nodeAttributes) > len(correctAttributes)):
        print('too many attributes')

    if (len(nodeAttributes) < len(correctAttributes)):
        print('attributes missing')

    found = False
    for c in correctAttributes:
        for n in nodeAttributes:
            if (c.getLabel() == n.getLabel()):
                found = True
                print('found', c.getLabel())
        if (found == False):
            found = False
            print('attribute missing ', c.getLabel())
        found = False

