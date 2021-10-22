import xml.etree.cElementTree as et
from xml.etree.ElementTree import SubElement, parse

xml_file = parse('registro.xml')

root = et.Element("Alumno")

xmlRoot = xml_file.getroot()



se = et.SubElement(root,"Alumno16")
et.SubElement(se, "Matricula").text = "18040099"
et.SubElement(se, "Carrera").text = "Infraestructura_de_Redes Digitales"
et.SubElement(se, "Nombre").text = "Simon_Eduardo_Hernandez"
xmlRoot.append(se)


xml_file.write("Alumno16.xml",xml_declaration=True)
