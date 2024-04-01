import xml.etree.ElementTree as ET

xml_file = "language.xml"

tree = ET.parse(xml_file)
root = tree.getroot()

for book in root.findall("book"):
    title_attrib = book.find("title").attrib["id"]
    title = book.find("title").text
    author = book.find("author").text
    print(title_attrib, title, author, sep=" - ")