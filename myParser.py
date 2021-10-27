import xml.etree.ElementTree as ET

import Model
import Corrector


def parse(xmlfile, correctfile, out):
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
        sort = text[39:]  # 39 for the prefix adress
        y = ET.tostring(x)
        y = str(y)
        if (sort == 'edge'):
            Model.createEdge(y, cElements)
        if (sort == 'node'):
            Model.createEntity(y, cElements)

    i = 0
    studentGraph = []
    for x in root.findall('./gr:graph/', ns):
        text = x.tag.__str__()
        sort = text[39:]  # 39 for the prefix adress
        y = ET.tostring(x)
        y = str(y)
        if (sort == 'edge'):
            Model.createEdge(y, studentGraph)
        if (sort == 'node'):
            Model.createEntity(y, studentGraph)

    return studentGraph, cElements


def correct(alElements, cElements, out):
    Corrector.checkEntities(alElements, cElements, out)
    Corrector.checkAttributes(alElements, cElements, out)
    Corrector.checkRelationCardinality(alElements, cElements, out)
    Corrector.checkTernary(alElements, cElements,out)


# Corrector.checkIsRelation(alElements, out)


def getMinMax(studentGraph):
    minX = 0
    minY = 0
    maxX = 0
    maxY = 0
    for i in studentGraph:
        if (type(i) == Model.Edge):
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


def normaliseCoordinates(studentGraph, minX, minY, maxX, maxY):
    canvasWidth = 1540/1.2
    canvasHeight = 680/1.2
    if (minX < 0):
        maxX = abs(minX) + abs(maxX)
    if (minY < 0):
        maxY = abs(minY) + abs(maxY)
    multX = canvasWidth / maxX
    multY = canvasHeight / maxY
    for i in studentGraph:
        if (type(i) == Model.Edge):
            continue
        else:
            x, y = i.getCoordinates()
            normX = (int(float(x)) - minX) * multX
            normY = (int(float(y)) - minY) * multY
            i.setCoordinates(int(normX), int(normY))


def scaleCoordinates(studentGraph, scale):
    for i in studentGraph:
        if (type(i) == Model.Edge):
            continue
        else:
            x, y = i.getCoordinates()
            x = (float(x) * float(scale))
            y = (float(y)) * float(scale)
            i.setCoordinates(int(x), int(y))
