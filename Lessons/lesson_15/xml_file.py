import xml.etree.ElementTree as ET

# Завантаження XML-файлу
tree = ET.parse('output.xml')
root = tree.getroot()

# Читання та виведення даних з елементів XML-документу
for child in root:
    print(child.tag, child.attrib)
    print(child.find('number').text)
    for subchild in child:
        # print(subchild.tag, subchild.text)
        if subchild.tag == 'timingExbytes':
            for micro_child in subchild:
                print(f'TAG: {micro_child.tag} Value: {micro_child.text}')