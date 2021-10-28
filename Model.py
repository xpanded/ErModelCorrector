class Entity:
    """
    The Entity class represents an Entity in the ER model
    nid represents the node id to distinguish each entity,relationship an attrobute each from another
    """

    def __init__(self, nid, label, x, y):
        self.nid = nid
        self.label = label
        self.attributes = []
        self.x = x
        self.y = y

    def getLabel(self):
        return self.label

    def getId(self):
        return self.nid

    def addAttribute(self, attribute):
        self.attributes.append(attribute)

    def getAttributes(self):
        return self.attributes

    def getCoordinates(self):
        return self.x, self.y

    def setCoordinates(self, x, y):
        self.x = x
        self.y = y


class Relation:
    """
    The Relationship class represents a Relationship in the ER model
    nid represents the node id to distinguish each entity,relationship an attribute each from another
    """

    def __init__(self, nid, label, x, y):
        self.nid = nid
        self.label = label
        self.attributes = []
        self.x = x
        self.y = y
        self.color = 'black'

    def getLabel(self):
        return self.label

    def getId(self):
        return self.nid

    def getCoordinates(self):
        return self.x, self.y

    def addAttribute(self, attribute):
        self.attributes.append(attribute)

    def getAttributes(self):
        return self.attributes

    def setCoordinates(self, x, y):
        self.x = x
        self.y = y

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color


class Attribute:
    """
    The Attribute class represents an Attribute in the ER model
    nid represents the node id to distinguish each entity,relationship an attribute each from another
    """

    def __init__(self, nid, label, primary, x, y):
        self.nid = nid
        self.label = label
        self.primary = primary
        self.x = x
        self.y = y
        self.color = 'black'

    def getId(self):
        return self.nid

    def getLabel(self):
        return self.label

    def setCoordinates(self, x, y):
        self.x = x
        self.y = y

    def getCoordinates(self):
        return self.x, self.y

    def getPrimary(self):
        return self.primary

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color


def findInList(nid, list):
    for i in list:
        if (i.getId() == nid):
            return i


class Edge:
    """
    the edge represents the line between the entities,relations and attributes
    """

    def __init__(self, lid, source, target):
        self.lid = lid
        self.source = source
        self.target = target
        self.label = ''
        self.color = 'black'
        self.arrowSource = False
        self.arrowTarget = False

    def setLabel(self, label):
        self.label = label

    def getLabel(self):
        return self.label

    def getSource(self):
        return self.source

    def getTarget(self):
        return self.target

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setArrowSource(self, arrow):
        self.arrowSource = arrow

    def getArrowSource(self):
        return self.arrowSource

    def setArrowTarget(self, arrow):
        self.arrowTarget = arrow

    def getArrowTarget(self):
        return self.arrowTarget


def createEdge(lines, list):
    """
    The lines are getting split and parsed to gather the required information.
    a Edge with the data of lines is getting created. The list is appended by this edge

    :param lines: a string from the graphml file for this edge
    :param list: a list of the graph which contains all objects of this graph
    """
    res = lines.split('\\n')
    mains = res[0].split(' ')
    sid = mains[3]
    sid = sid[4:-1]
    ssource = mains[4]
    ssource = ssource[8:-1]
    starget = mains[5]
    starget = starget[8:-2]
    slabel = ''
    i = 2

    while ('key=' in res[i]):
        i = i + 1

    if ('EdgeLabel' in res[i + 4]):
        slabels = res[i + 4].split('>')
        slabel = slabels[1]
        slabel = slabel.split('<')[0]
        slabel = umlautHelper(slabel)

    source = findInList(ssource, list)
    target = findInList(starget, list)

    nline = Edge(sid, source, target)
    nline.setLabel(slabel)

    j = i + 1
    while ('Path' in res[j] or 'Point' in res[j]):
        j = j + 1

    allarrows = res[j + 1]
    if ('source="standard' in allarrows or 'source="delta' in allarrows):
        nline.setArrowSource(True)
    if ('target="standard' in allarrows or 'target="delta' in allarrows):
        nline.setArrowTarget(True)

    if (type(source) == Entity and type(target) == Attribute):
        source.addAttribute(target)
    if (type(target) == Entity and type(source) == Attribute):
        target.addAttribute(source)
    if (type(source) == Relation and type(target) == Attribute):
        source.addAttribute(target)
    if (type(target) == Relation and type(source) == Attribute):
        target.addAttribute(source)
    list.append(nline)


def createEntity(lines, list):
    """
    The lines are getting split and parsed to gather the required information.
    a Entity/relation/attribute with the data of lines is getting created. The list is appended by this object

    :param lines: a string from the graphml file for this edge
    :param list: a list of the graph which contains all objects of this graph
    """
    res = lines.split('\\n')
    mains = res[0].split(' ')
    nid = mains[3]
    nid = nid[4:-2]
    i = 2
    nlabel = ''

    while ('key=' in res[i]):
        i = i + 1

    if ('NodeLabel' in res[i + 4]):
        nlabels = res[i + 4].split('>')
        ngeo = res[i + 1].split('=')
        nlabel = nlabels[1]
        nlabel = nlabel.split('<')[0]
        nlabel = umlautHelper(nlabel)

        x = ngeo[3][1:-3]
        y = ngeo[4][1:-4]

    entityType = res[2]
    if ('key' in entityType):
        entityType = res[3]

    if ('.relationship' in entityType):
        createRelation(nid, nlabel, list, x, y)
        return
    if ('attribute' in entityType):
        primary = False
        if ('''underlinedText="true"''' in nlabels[0]):
            primary = True
        createAttribute(nid, nlabel, primary, list, x, y)
        return

    entity = Entity(nid, nlabel, x, y)
    list.append(entity)


def createRelation(rid, rlabel, list, x, y):
    """creates a Relation with the given parameter"""
    relation = Relation(rid, rlabel, x, y)
    list.append(relation)


def createAttribute(nid, label, primary, list, x, y):
    """creates a Attribute with the given parameter"""
    attribute = Attribute(nid, label, primary, x, y)
    list.append(attribute)


def umlautHelper(text):
    """ the xml parser we use can not read umlaute therefore he replace them with html code
    in this method we reserve this process"""
    text = text.replace("&#196;", "Ä")
    text = text.replace("&#214;", "Ö")
    text = text.replace("&#220;", "Ü")
    text = text.replace("&#223;", "ß")
    text = text.replace("&#228;", "ä")
    text = text.replace("&#252;", "ü")
    text = text.replace("&#246;", "ö")

    return text
