from xml.etree.ElementTree import parse, Element

file_name = "registro.xml"
doc_xml = parse(file_name)
root = doc_xml.getroot()

root.remove(root.find("Alumno14"))

new_file = "eliminado.xml"
doc_xml.write(new_file, xml_declaration=True)
