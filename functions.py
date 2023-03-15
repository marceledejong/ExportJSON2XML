import xml.etree.ElementTree as ET

def traverse(obj, parent):
    if isinstance(obj, dict):
        for key, value in obj.items():
            element = ET.SubElement(parent, key)
            traverse(value, element)
    elif isinstance(obj, list):
        for item in obj:
            element = ET.SubElement(parent, 'item')
            traverse(item, element)
    else:
        parent.text = str(obj)