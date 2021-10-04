import model
import re
import Levenshtein as lev

tertary = []


def checkAttributes(graph, correct, out):
    for i in graph:
        if (type(i) == model.Node):
            nodeAttributes = i.getAttributes()
            nodename = i.getLabel()
            correctAttributes = getCorrectAttributes(nodename, correct)
            if (correctAttributes is not None):
                controllIfMissing(nodeAttributes, correctAttributes, nodename, out)


def getCorrectAttributes(nodename, correct):
    for y in correct:
        if (y.getLabel() == nodename and type(y) == model.Node):
            return y.getAttributes()


def controllIfMissing(nodeAttributes, correctAttributes, nodename, out):
    if (type(nodeAttributes) is None) or (type(correctAttributes) is None):
        return
    if (len(nodeAttributes) > len(correctAttributes)):
        print('too many attributes')
        out += 'too many attributes \n'

    elif (len(nodeAttributes) < len(correctAttributes)):
        print('attributes missing')

    found = False
    hasprimary = False
    for c in correctAttributes:
        for n in nodeAttributes:
            ratio = lev.ratio(c.getLabel().upper(), n.getLabel().upper())
            if (c.getLabel() == n.getLabel() or ratio > 0.75):
                if (c.getPrimary() != n.getPrimary() and hasprimary == False):
                    temp = '{0} is not a primary key \n'.format(c.getLabel())
                    hasprimary = True
                    print(temp)
                    out.append(temp)
                found = True
        if (found == False):
            print('attribute missing {0} for entity {1}'.format(c.getLabel(), nodename))
            out.append('attribute missing {0} for entity {1} \n'.format(c.getLabel(), nodename))
        found = False


def checkClasses(graph, correct, out):
    found = False
    for c in correct:
        for i in graph:
            if (type(i) == model.Node and type(c) == model.Node):
                ratio = lev.ratio(c.getLabel().upper(), i.getLabel().upper())
                if (i.getLabel() == c.getLabel() or ratio>0.75):
                    found = True
                # print('class found', c.getLabel())
            if (type(i) == model.Relation and type(c) == model.Relation):
                ratio = lev.ratio(c.getLabel().upper(), i.getLabel().upper())
                if (i.getLabel() == c.getLabel() or ratio >0.75):
                    found = True
                # print('relation found', c.getLabel())
        if (found == False and type(c) == model.Node):
            txt = 'class missing ' + str(c.getLabel()) + '\n'
            print(txt)
            out.append(txt)
        if (found == False and type(c) == model.Relation):
            txt = 'relationship missing ' + str(c.getLabel()) + '\n'
            print(txt)
            out.append(txt)
        found = False


def checkRelationCardinality(graph, correct, out):
    for c in correct:
        for g in graph:
            if (type(c) == model.Relation and type(g) == model.Relation):
                c1, c2 = getNodesFromRelation(correct, c, out)
                c1Cardinality = getCardinalityFromEdge(correct, c1, c)
                c2Cardinality = getCardinalityFromEdge(correct, c2, c)
                g1, g2 = getNodesFromRelation(graph, g, out)
                if (c1Cardinality != '' and c2Cardinality != ''):
                    if (g1.getLabel() == c1.getLabel()) and (g2.getLabel() == c2.getLabel()):
                        g1Cardinality = getCardinalityFromEdge(graph, g1, g)
                        g2Cardinality = getCardinalityFromEdge(graph, g2, g)
                        checkCarnality(g, g1, g2, g1Cardinality, g2Cardinality, c1Cardinality, c2Cardinality, out,
                                       graph)
                    if (g2.getLabel() == c1.getLabel()) and (g1.getLabel() == c2.getLabel()):
                        g1Cardinality = getCardinalityFromEdge(graph, g2, g)
                        g2Cardinality = getCardinalityFromEdge(graph, g1, g)
                        checkCarnality(g, g1, g2, g1Cardinality, g2Cardinality, c1Cardinality, c2Cardinality, out,
                                       graph)


def checkCarnality(relation, g1, g2, g1Cardinality, g2Cardinality, c1Cardinality, c2Cardinality, out, graph):
    # if (g1Cardinality == c1Cardinality and g2Cardinality == c2Cardinality):
    #   print('right cardinalities for ', c.getLabel())
    if (g1Cardinality != c1Cardinality):
        print('wrong cardinality for {0} related to {1} is {2} but should be {3}'.format(relation.getLabel(),
                                                                                         g1.getLabel(),
                                                                                         g1Cardinality,
                                                                                         c1Cardinality))
        out.append('wrong cardinality for {0} related to {1} is {2} but should be {3} \n'.format(relation.getLabel(),
                                                                                                 g1.getLabel(),
                                                                                                 g1Cardinality,
                                                                                                 c1Cardinality))
        edge = getEdgeBetweenNodeAndRelation(graph, g1, relation)
        edge.setColor('red')
    if (g2Cardinality != c2Cardinality):
        print('wrong cardinality for {0} related to {1} is {2} instead of {3}'.format(relation.getLabel(),
                                                                                      g2.getLabel(),
                                                                                      g2Cardinality,
                                                                                      c2Cardinality))
        out.append('wrong cardinality for {0} related to {1} is {2} instead of {3} \n'.format(relation.getLabel(),
                                                                                              g2.getLabel(),
                                                                                              g2Cardinality,
                                                                                              c2Cardinality))
        edge = getEdgeBetweenNodeAndRelation(graph, g2, relation)
        edge.setColor('red')


def checkIsRelation(graph, out):
    for i in graph:
        if (type(i) == model.Edge):
            if (i.getArrowSource() == True):
                if (type(i.getTarget()) == model.Relation):
                    if (i.getTarget().getLabel() == 'IST' or i.getTarget().getLabel() == 'IS'):
                        continue
                else:
                    out.append('{} is not a related to an IS relation'.format(i.getSource().getLabel()))
                    i.setColor('red')
            elif (i.getArrowTarget() == True):
                if (type(i.getSource()) == model.Relation):
                    if (i.getSource().getLabel().upper() == 'IST' or i.getSource().getLabel().upper() == 'IS'):
                        continue
                else:
                    out.append('{} is not a related to an IS relation'.format(i.getTarget().getLabel()))
                    i.setColor('red')


def getNodesFromRelation(graph, relation, out):
    edgeList = getEdgesFromRelation(graph, relation)
    if (len(edgeList) == 3 and relation not in tertary):
        relation.setColor('red')
        tertary.append(relation)
        out.append('{0} is a ternary realtionship \n'.format(relation.getLabel()))
    if (edgeList[0] is not None and edgeList[1] is not None):
        e1, e2 = edgeList[0], edgeList[1]
        n1 = 0
        n2 = 0
        if (type(e1.getTarget()) == model.Node):
            n1 = e1.getTarget()
        if (type(e1.getSource()) == model.Node):
            n1 = e1.getSource()
        if (type(e2.getTarget()) == model.Node):
            n2 = e2.getTarget()
        if (type(e2.getSource()) == model.Node):
            n2 = e2.getSource()
        return n1, n2


def getEdgesFromRelation(graph, relation):
    alresult = []
    for i in graph:
        if (type(i) == model.Edge):
            if (i.getTarget() == relation and type(i.getSource()) == model.Node) or (
                    i.getSource() == relation and type(i.getTarget()) == model.Node):
                alresult.append(i)
    if (alresult[0] is not None and alresult[1] is not None):
        return alresult


def getCardinalityFromEdge(graph, n1, n2):
    for i in graph:
        if (type(i) == model.Edge):
            if (i.getTarget() == n1 and i.getSource() == n2) or (
                    i.getTarget() == n2 and i.getSource() == n1):
                label = str(i.getLabel())
                pattern = re.compile(r'\s+')
                label = re.sub(pattern, '', label)
                return label


def getEdgeBetweenNodeAndRelation(graph, node, r):
    for i in graph:
        if (type(i) == model.Edge):
            if (i.getTarget() == node and i.getSource() == r) or (
                    i.getTarget() == r and i.getSource() == node):
                return i
