##  created XML file, info writeln  ##

import xml.etree.cElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "field1", name="Name").text = "Max"
ET.SubElement(doc, "field2", name="E-mail").text = "123@gmail.com"

tree = ET.ElementTree(root)
tree.write("file.xml")

##  get location (works)  ##

import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('file.xml').getroot()
print (e)

##  print (doesn't work)  ##
for field in e.findall('field1'):
    print(field1.get('name'))