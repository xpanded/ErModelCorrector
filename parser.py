import xml.etree.ElementTree as ET
from io import StringIO
import substring
from xml.parsers import expat

import model
import corrector

xmlfile = 'xmls/test2.graphml'
correctfile = 'xmls/test3.graphml'

ns = {"y": "https://www.yworks.com/xml/graphml", "gr": "http://graphml.graphdrawing.org/xmlns"}
ET.register_namespace('gr', 'http://graphml.graphdrawing.org/xmlns')
ET.register_namespace('y', 'https://www.yworks.com/xml/graphml')

tree = ET.parse(xmlfile)
root = tree.getroot()

ctree = ET.parse(correctfile)
croot = ctree.getroot()

for elm in root.iterfind("./{http://graphml.graphdrawing.org/xmlns}graph"):
    alElements = elm

ET.dump(alElements)

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

corrector.checkAttributes(alElements, cElements)
