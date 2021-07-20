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
            if (type(i) == model.Relation and type(c) == model.Relation):
                if (i.getLabel() == c.getLabel()):
                    found = True
                    print('relation found', c.getLabel())
        if (found == False and type(c) == model.Node):
            print('class missing ', c.getLabel())
        if (found == False and type(c) == model.Relation):
            print('relationship missing ', c.getLabel())
        found = False


def checkRelationCardinality(graph, correct):
    for c in correct:
        for g in graph:
            if (type(c) == model.Relation and type(g) == model.Relation):
                c1, c2 = getNodesFromRelation(correct, c)
                c1Cardinality = getCardinalityFromEdge(correct, c1, c)
                c2Cardinality = getCardinalityFromEdge(correct, c2, c)
                g1, g2 = getNodesFromRelation(graph, g)
                if (g1.getLabel() == c1.getLabel()):
                    g1Cardinality = getCardinalityFromEdge(graph, g1, g)
                    g2Cardinality = getCardinalityFromEdge(graph, g2, g)
                if (g2.getLabel() == c1.getLabel()):
                    g1Cardinality = getCardinalityFromEdge(graph, g2, g)
                    g2Cardinality = getCardinalityFromEdge(graph, g1, g)
                if (g1Cardinality == c1Cardinality and g2Cardinality == c2Cardinality):
                    print('right cardinality for ', c.getLabel())
                    continue
                if (g1Cardinality != c1Cardinality):
                    print('wrong cardinality for {0} is {1} instead of {2}'.format(c.getLabel(), g1Cardinality,
                                                                                   c1Cardinality))
                if (g2Cardinality != c2Cardinality):
                    print('wrong cardinality for {0} is {1} instead of {2}'.format(c.getLabel(), g2Cardinality,
                                                                                   c2Cardinality))


def getNodesFromRelation(graph, relation):
    e1, e2 = getEdgesFromRelation(graph, relation)
    n1 = 0
    n2 = 0
    if (type(e1.getTarget()) == model.Node):
        n1 = e1.getTarget()
    if (type(e1.getSource()) == model.Node):
        n1 = e1.getSource()
    if (type(e2.getTarget()) == model.Node):
        n2 = e2.getTarget()
    if (type(e1.getSource()) == model.Node):
        n2 = e2.getSource()
    return n1, n2


def getEdgesFromRelation(graph, relation):
    alresult = []
    for i in graph:
        if (type(i) == model.Edge):
            if (i.getTarget() == relation or i.getSource() == relation):
                alresult.append(i)
    if (alresult[0] is not None and alresult[1] is not None):
        return alresult[0], alresult[1]


def getCardinalityFromEdge(graph, n1, n2):
    for i in graph:
        if (type(i) == model.Edge):
            if (i.getTarget() == n1 and i.getSource() == n2) or (
                    i.getTarget() == n2 and i.getSource() == n2):
                return i.getLabel()
