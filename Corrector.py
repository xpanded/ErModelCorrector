import model
import re
import Levenshtein as lev

tertary = []


def checkAttributes(studentGraph, modelGraph, out):
    for i in studentGraph:
        if (type(i) == model.Entity):
            studentAttributes = i.getAttributes()
            nodeName = i.getLabel()
            modelAttributes = getCorrectAttributes(nodeName, modelGraph)
            if (modelAttributes is not None):
                controllIfMissing(studentAttributes, modelAttributes, nodeName, out)


def getCorrectAttributes(nodeName, modelGraph):
    for y in modelGraph:
        if (y.getLabel() == nodeName and type(y) == model.Entity):
            return y.getAttributes()


def controllIfMissing(studentAttributes, modelAttributes, nodeName, out):
    if (type(studentAttributes) is None) or (type(modelAttributes) is None):
        return
    if (len(studentAttributes) > len(modelAttributes)):
        out += 'too many attributes \n'
    # hasPrimary = False
    for c in modelAttributes:
        found = False
        for n in studentAttributes:
            ratio = lev.ratio(c.getLabel().upper(), n.getLabel().upper())
            if (ratio > 0.75):
                if (c.getPrimary() != n.getPrimary()):  # and hasPrimary == False
                    if (c.getPrimary()):
                        temp = '{0} is a primary key for the entity {1} \n'.format(c.getLabel(), nodeName)
                        n.setColor('red')
                    else:
                        temp = '{0} is not a primary key for the entity {1} \n'.format(c.getLabel(), nodeName)
                        n.setColor('red')
                    out.append(temp)
            found = True
        if (found == False):
            out.append('attribute missing {0} for the entity {1} \n'.format(c.getLabel(), nodeName))


def checkEntities(studentGraph, modelGraph, out):
    for c in modelGraph:
        found = False
        for i in studentGraph:
            if (type(i) == model.Entity and type(c) == model.Entity or (
                    type(i) == model.Relation and type(c) == model.Relation)):
                ratio = lev.ratio(c.getLabel().upper(), i.getLabel().upper())
                if (ratio > 0.75):
                    found = True
        if (found == False and type(c) == model.Entity):
            txt = 'entity missing ' + str(c.getLabel()) + '\n'
            out.append(txt)
        if (found == False and type(c) == model.Relation and (
                c.getLabel().upper() != 'IST' and c.getLabel().upper() != 'IS')):
            entity1, entity2 = getEntitiesFromRelation(modelGraph, c)
            txt = 'relationship missing: "' + str(
                c.getLabel()) + '" between ' + entity1.getLabel() + ' and ' + entity2.getLabel() + '\n'
            out.append(txt)


def checkRelationCardinality(studentGraph, modelGraph, out):
    for c in modelGraph:
        for i in studentGraph:
            if (type(c) == model.Relation and type(i) == model.Relation):
                if (checkTernary(studentGraph, i, out) == False):
                    c1, c2 = getEntitiesFromRelation(modelGraph, c)
                    c1Cardinality = getCardinalityFromEdge(modelGraph, c1, c)
                    c2Cardinality = getCardinalityFromEdge(modelGraph, c2, c)
                    i1, i2 = getEntitiesFromRelation(studentGraph, i)
                    if (c1Cardinality != '' and c2Cardinality != ''):
                        ratio1 = lev.ratio(c1.getLabel().upper(), i1.getLabel().upper())
                        ratio2 = lev.ratio(c2.getLabel().upper(), i2.getLabel().upper())
                        ratio3 = lev.ratio(c1.getLabel().upper(), i2.getLabel().upper())
                        ratio4 = lev.ratio(c2.getLabel().upper(), i1.getLabel().upper())
                        if (ratio1 > 0.75 and ratio2 > 0.75):
                            g1Cardinality = getCardinalityFromEdge(studentGraph, i1, i)
                            g2Cardinality = getCardinalityFromEdge(studentGraph, i2, i)
                            checkCarnality(i, i1, i2, g1Cardinality, g2Cardinality, c1Cardinality, c2Cardinality, out,
                                           studentGraph)
                        if (ratio3 > 0.75 and ratio4 > 0.75):
                            g1Cardinality = getCardinalityFromEdge(studentGraph, i2, i)
                            g2Cardinality = getCardinalityFromEdge(studentGraph, i1, i)
                            checkCarnality(i, i1, i2, g1Cardinality, g2Cardinality, c1Cardinality, c2Cardinality, out,
                                           studentGraph)


def checkCarnality(relation, g1, g2, g1Cardinality, g2Cardinality, c1Cardinality, c2Cardinality, out, graph):
    if (g1Cardinality == '[1,1]' and g2Cardinality == '[1,1]'):
        out.append('Relationship {0} superfluous two times {1} !    \n'.format(relation.getLabel(), g2Cardinality))
        edge = getEdgeBetweenEntityAndRelation(graph, g1, relation)
        edge.setColor('red')
        edge = getEdgeBetweenEntityAndRelation(graph, g2, relation)
        edge.setColor('red')
    if (g1Cardinality != c1Cardinality):
        out.append('wrong cardinality for {0} related to {1} is {2} but should be {3} \n'.format(relation.getLabel(),
                                                                                                 g1.getLabel(),
                                                                                                 g1Cardinality,
                                                                                                 c1Cardinality))
        edge = getEdgeBetweenEntityAndRelation(graph, g1, relation)
        edge.setColor('red')
    if (g2Cardinality != c2Cardinality):
        out.append('wrong cardinality for {0} related to {1} is {2} instead of {3} \n'.format(relation.getLabel(),
                                                                                              g2.getLabel(),
                                                                                              g2Cardinality,
                                                                                              c2Cardinality))
        edge = getEdgeBetweenEntityAndRelation(graph, g2, relation)
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


def checkTernary(graph, relation, out):
    edgeList = getEdgesFromRelation(graph, relation)
    if (len(edgeList) == 3 and relation not in tertary):
        relation.setColor('red')
        tertary.append(relation)
        out.append('{0} is a ternary realtionship \n'.format(relation.getLabel()))
        return True
    return False


def getEntitiesFromRelation(graph, relation):
    edgeList = getEdgesFromRelation(graph, relation)
    if (edgeList[0] is not None and edgeList[1] is not None):
        e1, e2 = edgeList[0], edgeList[1]
        n1 = 0
        n2 = 0
        if (type(e1.getTarget()) == model.Entity):
            n1 = e1.getTarget()
        if (type(e1.getSource()) == model.Entity):
            n1 = e1.getSource()
        if (type(e2.getTarget()) == model.Entity):
            n2 = e2.getTarget()
        if (type(e2.getSource()) == model.Entity):
            n2 = e2.getSource()
        return n1, n2


def getEdgesFromRelation(graph, relation):
    alresult = []
    for i in graph:
        if (type(i) == model.Edge):
            if (i.getTarget() == relation and type(i.getSource()) == model.Entity) or (
                    i.getSource() == relation and type(i.getTarget()) == model.Entity):
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


def getEdgeBetweenEntityAndRelation(graph, node, r):
    for i in graph:
        if (type(i) == model.Edge):
            if (i.getTarget() == node and i.getSource() == r) or (
                    i.getTarget() == r and i.getSource() == node):
                return i
