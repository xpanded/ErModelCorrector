import xml.etree.ElementTree as ET

import Model
import Corrector


def parse(studentfile, modelFile):
    """
    the namespaces need to be need to be defined if the file has got prefixes like our graphml file has.
    we parse the tree and got thorugh every element of a graph and save this in a list for each file.
    depending if it is a edge or an entity(entity,edge,relation), we call the corresponding method

    :param studentfile:  is the xml file that contains the student's graph
    :param modelFile:  is the xml file that contains the model's graph
    :return: 2 lists one for each graph containing every object of their graph
    """
    namespace = {"y": "https://www.yworks.com/xml/graphml", "gr": "http://graphml.graphdrawing.org/xmlns"}
    ET.register_namespace('gr', 'http://graphml.graphdrawing.org/xmlns')
    ET.register_namespace('y', 'https://www.yworks.com/xml/graphml')

    tree = ET.parse(studentfile)
    root = tree.getroot()

    ctree = ET.parse(modelFile)
    croot = ctree.getroot()

    modelElements = []
    for x in croot.findall('./gr:graph/', namespace):
        text = x.tag.__str__()
        sort = text[39:]  # 39 for the prefix adress
        y = ET.tostring(x)
        y = str(y)
        if (sort == 'edge'):
            Model.createEdge(y, modelElements)
        if (sort == 'node'):
            Model.createEntity(y, modelElements)

    i = 0
    studentGraph = []
    for x in root.findall('./gr:graph/', namespace):
        text = x.tag.__str__()
        sort = text[39:]  # 39 for the prefix adress
        y = ET.tostring(x)
        y = str(y)
        if (sort == 'edge'):
            Model.createEdge(y, studentGraph)
        if (sort == 'node'):
            Model.createEntity(y, studentGraph)

    return studentGraph, modelElements


def correct(studentElements, modelElements, out):
    """

    :param studentElements: list of all elements included in the student's file
    :param modelElements: list of all elements included in the model file
    :param out = outputfile with all potential errors
    :return no
    """
    Corrector.checkEntities(studentElements, modelElements, out)
    Corrector.checkAttributes(studentElements, modelElements, out)
    Corrector.checkRelationCardinality(studentElements, modelElements, out)
    Corrector.checkTernary(studentElements, modelElements, out)


def getMinMax(studentGraph):
    """
    The method looks for the minimum and max coordinates in the given list

    :param studentGraph: list of all elements included in the student's file
    :return: minimum x and y , maximum x and y
    """

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
    """
    The method checks if any of the both min values are negative to calculate the propper maximal values
    then the multiplicators for x and y are getting calculated.
    Then every entity(entity,edge,relation) coordinates are gewtting calculated in the coordinate system

    :param studentGraph: list of all elements included in the student's file
    :param minX: minimal value for x
    :param minY: minimal value for y
    :param maxX: maximal value for x
    :param maxY: maximal value for y
    """
    canvasWidth = 1540 / 1.2
    canvasHeight = 680 / 1.2
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
    """

    :param studentGraph: list of all elements included in the student's file
    :param scale: a percentage value with wihich the coordinates are getting scaled like 100% = 1
    """

    for i in studentGraph:
        if (type(i) == Model.Edge):
            continue
        else:
            x, y = i.getCoordinates()
            x = (float(x) * float(scale))
            y = (float(y)) * float(scale)
            i.setCoordinates(int(x), int(y))
