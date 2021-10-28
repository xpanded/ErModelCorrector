import unittest

import os

import Corrector
import myParser


class Test(unittest.TestCase):
    dirname = os.path.dirname(__file__)
    deliverySolution = os.path.join(dirname, 'test_ressources/delivery.graphml')
    deliveryWrong = os.path.join(dirname, 'test_ressources/delivery-wrong.graphml')
    out = ''

    def testCheckParsingStudentModel(self):
        self.assertNotEqual(self.deliverySolution, None)

        sElements, cElements = myParser.parse(self.deliveryWrong, self.deliverySolution)
        self.assertNotEqual(self.deliveryWrong, False)
        self.assertNotEqual(sElements[0], None)
        self.assertEqual(sElements[0].getLabel(), 'Order')
        x, y = sElements[0].getCoordinates()
        self.assertEqual(x, '569.0')

    def testCheckParsingSolutionModel(self):
        self.assertNotEqual(self.deliverySolution, None)

        sElements, cElements = myParser.parse(self.deliveryWrong, self.deliverySolution)
        self.assertNotEqual(self.deliveryWrong, False)
        self.assertNotEqual(sElements[21], None)
        self.assertEqual(sElements[21].getLabel(), 'paid')
        self.assertEqual(sElements[21].getColor(), 'black')
        x, y = sElements[21].getCoordinates()
        self.assertEqual(int(float(y)), 242)

    def testCheckRelationCardinality(self):
        self.assertNotEqual(self.deliveryWrong, False)

    def testGetMinMax(self):
        sElements, cElements = myParser.parse(self.deliveryWrong, self.deliverySolution)
        minX, minY, maxX, maxY = myParser.getMinMax(sElements)
        self.assertEqual(minX, 0)
        self.assertEqual(minY, 0)
        self.assertEqual(maxX, 1322)
        self.assertEqual(maxY, 812)

    def testNormaliseCoordinates(self):
        sElements, cElements = myParser.parse(self.deliveryWrong, self.deliverySolution)
        minX, minY, maxX, maxY = myParser.getMinMax(sElements)
        myParser.normaliseCoordinates(sElements, minX, minY, maxX, maxY)
        tmpX, tmpY = sElements[1].getCoordinates()
        self.assertEqual(tmpX, 1081)
        self.assertEqual(tmpY, 233)

    def testScaleCoordinates(self):
        sElements, cElements = myParser.parse(self.deliveryWrong, self.deliverySolution)
        minX, minY, maxX, maxY = myParser.getMinMax(sElements)
        myParser.normaliseCoordinates(sElements, minX, minY, maxX, maxY)
        myParser.scaleCoordinates(sElements, 1.10)
        tmpX, tmpY = sElements[1].getCoordinates()
        self.assertEqual(tmpX, 1189)
        self.assertEqual(tmpY, 256)


if __name__ == '__main__':
    unittest.main()
