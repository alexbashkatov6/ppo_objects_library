import xml.etree.ElementTree as ET
import os

from ppo_objects import PpoElectropneumaticValveRi, PpoPneumaticCleaningCompressorRi, \
    PpoPneumaticCleaningValve, PpoPneumaticCleaningArea
from manager import Manager
from constants import INPUT_FOLDER, INTERFACE_FOLDER, TECHNOLOGY_FOLDER

USO_STR = "USO:{}"

input_tpo_et = ET.parse(os.path.join(INPUT_FOLDER, TECHNOLOGY_FOLDER, "PpoPneumaticCleaning.xml"))
input_interf_et = ET.parse(os.path.join(INPUT_FOLDER, INTERFACE_FOLDER, "PpoPneumaticCleaning.xml"))

m = Manager()
for elem in input_interf_et.getroot():

    elem: ET.Element
    tag = elem.attrib['Tag']
    if tag == "KOS":
        new_obj = PpoPneumaticCleaningCompressorRi()
        new_obj.tag = elem.attrib['Tag']
        new_obj.addrKI_RD = USO_STR.format(elem.find("AddrKI").attrib['RD'])
        new_obj.addrUI_OSV = USO_STR.format(elem.find("AddrUI").attrib['OSV'])
    else:
        new_obj = PpoElectropneumaticValveRi()
        new_obj.tag = elem.attrib['Tag']
        new_obj.addrKI_KEPK = USO_STR.format(elem.find("AddrKI").attrib['KEPK'])
        new_obj.addrUI_OEPK = USO_STR.format(elem.find("AddrUI").attrib['OEPK'])
        for i in range(1, 9):
            if "VS{}".format(i) in elem.find("AddrUI").attrib:
                setattr(new_obj, "addrUI_VS{}".format(i), USO_STR.format(elem.find("AddrUI").attrib["VS{}".format(i)]))

    m.append_obj(new_obj)

for elem in input_tpo_et.getroot():

    elem: ET.Element
    tag = elem.attrib['Tag']
    if tag == "ROS":
        new_obj = PpoPneumaticCleaningArea()
        new_obj.id_ = elem.attrib['Tag']
        new_obj.tag = elem.attrib['Tag']
        new_obj.indent = elem.attrib['Tag']
        new_obj.idControlArea = "ULTRAMAR"
        new_obj.iObjTag = "KOS"
        new_obj.valves = elem.find("EPK").attrib['TObj'].split(" ")
    else:
        new_obj = PpoPneumaticCleaningValve()
        new_obj.id_ = elem.attrib['Tag']
        new_obj.tag = elem.attrib['Tag']
        new_obj.indent = elem.attrib['Tag']
        new_obj.idControlArea = "ULTRAMAR"
        new_obj.iObjTag = new_obj.tag
        new_obj.point = new_obj.tag.replace("EPK_", "")
    m.append_obj(new_obj)


m.write_objs_json(["PpoElectropneumaticValveRi",
                   "PpoPneumaticCleaningCompressorRi",
                   "PpoPneumaticCleaningValve",
                   "PpoPneumaticCleaningArea"], "Equipment")
