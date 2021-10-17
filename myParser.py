import xml.etree.ElementTree as ET

import model
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
        sort = text[39:]  # 39 for the prefix ardess
        y = ET.tostring(x)
        y = str(y)
        if (sort == 'edge'):
            model.createEdge(y, cElements)
        if (sort == 'node'):
            model.createEntity(y, cElements)

    i = 0
    sElements = []
    for x in root.findall('./gr:graph/', ns):
        text = x.tag.__str__()
        sort = text[39:]  # 39 for the prefix ardess
        y = ET.tostring(x)
        y = str(y)
        if (sort == 'edge'):
            model.createEdge(y, sElements)
        if (sort == 'node'):
            model.createEntity(y, sElements)


    return sElements, cElements


def correct(alElements, cElements, out):
    Corrector.checkEntities(alElements, cElements, out)
    Corrector.checkAttributes(alElements, cElements, out)
    Corrector.checkRelationCardinality(alElements, cElements, out)
   # Corrector.checkIsRelation(alElements, out)


def getMinMax(sElements):
    minX = 0
    minY = 0
    maxX = 0
    maxY = 0
    for i in sElements:
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


def normaliseCoordinates(sElements, minX, minY, maxX, maxY):
    if (minX < 0):
        maxX = abs(minX) + abs(maxX)
    if (minY < 0):
        maxY = abs(minY) + abs(maxY)
    multX = 1540 / maxX
    multY = 680 / maxY
    for i in sElements:
        if (type(i) == model.Edge):
            continue
        else:
            x, y = i.getCoordinates()
            x = (int(float(x)) - minX) * multX / 2
            y = (int(float(y)) - minY) * multY / 2
            i.setCoordinates(int(x), int(y))


def scaleCoordinates(sElements, scale):
    for i in sElements:
        if (type(i) == model.Edge):
            continue
        else:
            x, y = i.getCoordinates()
            x = (float(x) * float(scale))
            y = (float(y)) * float(scale)
            i.setCoordinates(int(x), int(y))
