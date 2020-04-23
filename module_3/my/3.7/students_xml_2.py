from xml.etree import ElementTree

tree = ElementTree.parse("./files/students.xml")
root = tree.getroot()

greg = root[0]
module1 = next(greg.iter("module1"))
print(module1, module1.text)
module1.text = str(float(module1.text) + 30)

tree.write("./files/students_modifed.xml")

certificate = greg[2]
certificate.set("type", "with distinction")
tree.write("./files/students_modifed.xml")

description = ElementTree.Element("description")
description.text = "Showed excellent skills during the course"
greg.append(description)
tree.write("./files/students_modifed.xml")

description = greg.find("description")
greg.remove(description)
tree.write("./files/students_modifed.xml")




