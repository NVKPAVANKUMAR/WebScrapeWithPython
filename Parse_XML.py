import unittest
import xml.etree.cElementTree as Et


class TestParseXml(unittest.TestCase):
    def test_xml_data(self):
        xml_doc = open('data/data.xml', 'r')
        xml_doc_data = xml_doc.read()
        xml_doc_tree = Et.XML(xml_doc_data)
        for i in xml_doc_tree.iter('note'):
            print(i[0].text)
            print(i[1].text)
            print(i[2].text)
            print(i[3].text)
