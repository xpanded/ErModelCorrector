import xml.etree.ElementTree as ET

import model
import Corrector


def correct(xmlfile, correctfile):
    ns = {"y": "https://www.yworks.com/xml/graphml", "gr": "http://graphml.graphdrawing.org/xmlns"}
    ET.register_namespace('gr', 'http://graphml.graphdrawing.org/xmlns')
    ET.register_namespace('y', 'https://www.yworks.com/xml/graphml')

    tree = ET.parse(xmlfile)
    root = tree.getroot()

    ctree = ET.parse(correctfile)
    croot = ctree.getroot()

    cElements = []
    for x in croot.findall('./gr:graph/', ns):
        text = x.tag.__str__()
        sort = text[39:]  # 39 for the prefix ardess
        y = ET.tostring(x)
        y = str(y)
        if (sort == 'edge'):
            model.createEdge(y, cElements)
        if (sort == 'node'):
            model.createNode(y, cElements)

    i = 0
    alElements = []
    for x in root.findall('./gr:graph/', ns):
        text = x.tag.__str__()
        sort = text[39:]  # 39 for the prefix ardess
        y = ET.tostring(x)
        y = str(y)
        if (sort == 'edge'):
            model.createEdge(y, alElements)
        if (sort == 'node'):
            model.createNode(y, alElements)

    model.printall(alElements)
    print('ctree \n')
    model.printall(cElements)

    Corrector.checkAttributes(alElements, cElements)
    Corrector.checkClasses(alElements, cElements)
    Corrector.checkRelationCardinality(alElements, cElements)

    return alElements, cElements


def getMinMax(alElements):
    minX = 0
    minY = 0
    maxX = 0
    maxY = 0
    for i in alElements:
        if (type(i) == model.Edge):
            continue
        else:
            x, y = i.getCoordinates()
            if int(float(x)) < int(float(minX)):
                minX = int(float(x))
            if int(float(x)) > int(float(maxX)):
                maxX = int(float(x))
            if int(float(y)) < int(float(minY)):
                minY = int(float(y))
            if int(float(y)) > int(float(maxY)):
                maxY = int(float(y))
    return minX, minY, maxX, maxY


def normaliseCoordinates(alElements, minX, minY, maxX, maxY):
    multX = 1540 / maxX
    multY = 660 / maxY
    for i in alElements:
        if (type(i) == model.Edge):
            continue
        else:
            x, y = i.getCoordinates()
            x = (int(float(x)) - minX) * multX/2
            y = (int(float(y)) - minY) * multY/2
            i.setCoordinates(int(x), int(y))
