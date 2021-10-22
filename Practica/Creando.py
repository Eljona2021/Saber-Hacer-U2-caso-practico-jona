import xml.etree.cElementTree as et

root = et.Element("Edificio2.xml")

se = et.SubElement(root,"Alumno1")
et.SubElement(se, "Matricula").text = "18040048"
et.SubElement(se, "Carrera").text = "Infraestructura_de_Redes Digitales"
et.SubElement(se, "Nombre").text = "Jonathan_Hernandez_Rodriguez"

se = et.SubElement(root,"Alumno2")
et.SubElement(se, "Matricula").text = "18040029"
et.SubElement(se, "Carrera").text = "Infraestructura_de_Redes Digitales"
et.SubElement(se, "Nombre").text = "Isidro_Mendez_Zertuche"

se = et.SubElement(root,"Alumno3")
et.SubElement(se, "Matricula").text = "18040007"
et.SubElement(se, "Carrera").text = "Infraestructura_de_Redes Digitales"
et.SubElement(se, "Nombre").text = "Rosa_Ibet_Rodriguez"

se = et.SubElement(root,"Alumno4")
et.SubElement(se, "Matricula").text = "18040091"
et.SubElement(se, "Carrera").text = "Infraestructura_de_Redes Digitales"
et.SubElement(se, "Nombre").text = "Aylin_Arreozola_Sanchez"

se = et.SubElement(root,"Alumno5")
et.SubElement(se, "Matricula").text = "18040008"
et.SubElement(se, "Carrera").text = "Infraestructura_de_Redes Digitales"
et.SubElement(se, "Nombre").text = "Ezequiel_Hernandez_Hidalgo"

se = et.SubElement(root,"Alumno6")
et.SubElement(se, "Matricula").text = "18040012"
et.SubElement(se, "Carrera").text = "Desarollo_y Gestion_De Software"
et.SubElement(se, "Nombre").text = "Albertano_Castillo_Lopez"

se = et.SubElement(root,"Alumno7")
et.SubElement(se, "Matricula").text = "18040100"
et.SubElement(se, "Carrera").text = "Desarollo_y Gestion_De Software"
et.SubElement(se, "Nombre").text = "Estefania_Muñoz_Castro"

se = et.SubElement(root,"Alumno8")
et.SubElement(se, "Matricula").text = "18040020"
et.SubElement(se, "Carrera").text = "Desarollo_y Gestion_De Software"
et.SubElement(se, "Nombre").text = "Angela_Mariana_Gonzales"

se = et.SubElement(root,"Alumno9")
et.SubElement(se, "Matricula").text = "18040113"
et.SubElement(se, "Carrera").text = "Desarollo_y Gestion_De Software"
et.SubElement(se, "Nombre").text = "Alejandro_David_Dominguez"

se = et.SubElement(root,"Alumno10")
et.SubElement(se, "Matricula").text = "18040023"
et.SubElement(se, "Carrera").text = "Desarollo_y Gestion_De Software"
et.SubElement(se, "Nombre").text = "Ezequiel_Esquivel_Coronado"

se = et.SubElement(root,"Alumno11")
et.SubElement(se, "Matricula").text = "18040190"
et.SubElement(se, "Carrera").text = "Entornos_Virtuales_Y Negocios"
et.SubElement(se, "Nombre").text = "Nelson_Cruz_Garcia"

se = et.SubElement(root,"Alumno12")
et.SubElement(se, "Matricula").text = "18040207"
et.SubElement(se, "Carrera").text = "Entornos_Virtuales_Y Negocios"
et.SubElement(se, "Nombre").text = "Andrea_Alvarez_Ruiz"

se = et.SubElement(root,"Alumno13")
et.SubElement(se, "Matricula").text = "18040266"
et.SubElement(se, "Carrera").text = "Entornos_Virtuales_Y Negocios"
et.SubElement(se, "Nombre").text = "Luis_Jaime_Valdez"

se = et.SubElement(root,"Alumno14")
et.SubElement(se, "Matricula").text = "18040078"
et.SubElement(se, "Carrera").text = "Entornos_Virtuales_Y Negocios"
et.SubElement(se, "Nombre").text = "Ximena_Casas_Rodiguez"

se = et.SubElement(root,"Alumno15")
et.SubElement(se, "Matricula").text = "18040302"
et.SubElement(se, "Carrera").text = "Entornos_Virtuales_Y Negocios"
et.SubElement(se, "Nombre").text = "Dayana_Hernandez_DeLaCruz"


tree = et.ElementTree(root)
tree.write("registro.xml", xml_declaration=True)
