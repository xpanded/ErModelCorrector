class Edge:
    label = ''

    def __init__(self, lid, source, target):
        self.lid = lid
        self.source = source
        self.target = target

    def setLabel(self, label):
        self.label = label

    def getLabel(self):
        return self.label

    def getSource(self):
        return self.source

    def getTarget(self):
        return self.getTarget()


class Node:

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


class Relation:

    def __init__(self, nid, label, x, y):
        self.nid = nid
        self.label = label
        self.x = x
        self.y = y

    def getLabel(self):
        return self.label

    def getId(self):
        return self.nid


class Attribute:
    def __init__(self, nid, label, primary, x, y):
        self.nid = nid
        self.label = label
        self.primary = primary
        self.x = x
        self.y = y

    def getId(self):
        return self.nid

    def getLabel(self):
        return self.label


def findInList(nid, list):
    for i in list:
        if (i.getId() == nid):
            return i


def createEdge(x, list):
    res = x.split('\\n')
    mains = res[0].split(' ')
    sid = mains[3]
    sid = sid[4:-1]
    ssource = mains[4]
    ssource = ssource[8:-1]
    starget = mains[5]
    starget = starget[8:-2]

    slabels = res[6].split('>')
    slabel = slabels[1]
    slabel = slabel.split('<')[0]

    source = findInList(ssource, list)
    target = findInList(starget, list)

    nline = Edge(sid, source, target)
    nline.setLabel(slabel)
    if (type(source) == Node and type(target) == Attribute):
        source.addAttribute(target)
    if (type(target) == Node and type(source) == Attribute):
        target.addAttribute(source)
    list.append(nline)


def createNode(nx, list):
    res = nx.split('\\n')
    mains = res[0].split(' ')
    nid = mains[3]
    nid = nid[4:-2]

    if ('key=' in res[2]):
        nlabels = res[7].split('>')
        ngeo = res[4].split('=')
    else:
        nlabels = res[6].split('>')
        ngeo = res[3].split('=')
    nlabel = nlabels[1]
    nlabel = nlabel.split('<')[0]

    x = ngeo[3][1:-3]
    y = ngeo[4][1:-4]

    nodetype = res[2]
    if ('key' in nodetype):
        nodetype = res[3]

    if ('small_entity' in nodetype):
        print('entity')  # test
    if ('.relationship' in nodetype):
        createRelation(nid, nlabel, list, x, y)
        return
    if ('attribute' in nodetype):
        primary = False
        if ('underlinedText="true"' in nlabels):
            primary = True
        createAttribute(nid, nlabel, primary, list, x, y)
        return

    node = Node(nid, nlabel, x, y)
    list.append(node)


def createRelation(rid, rlabel, list, x, y):
    relation = Relation(rid, rlabel, x, y)
    list.append(relation)


def createAttribute(nid, label, primary, list, x, y):
    attribute = Attribute(nid, label, primary, x, y)
    list.append(attribute)


def printall(list):
    for i in list:
        print(i.getLabel())
