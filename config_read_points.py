import xml.etree.ElementTree as ET
import os

from ppo_objects import PpoPoint, SectionAndIgnoreCondition, AdditionalSwitch
from manager import Manager
from constants import INPUT_FOLDER, TECHNOLOGY_FOLDER, INTERFACE_FOLDER, OUTPUT_FOLDER, PYTHON_KEYWORD_REPLACES

points_et = ET.parse(os.path.join(INPUT_FOLDER, TECHNOLOGY_FOLDER, "PpoPoints.xml"))


m = Manager()
for elem in points_et.getroot():

    elem: ET.Element
    new_obj = PpoPoint()

    new_obj.tag = elem.attrib['Tag']
    new_obj.idControlArea = elem.find("RU").attrib['TObj']
    new_obj.section = elem.find("Sek").attrib['TObj']
    new_obj.railFittersWarningArea = elem.find("MP").attrib['TObj']

    ngp_elem = elem.find("NGP")
    if not (ngp_elem is None):
        ngp_sect_ign_condit = SectionAndIgnoreCondition()
        ngp_sect_ign_condit.section = ngp_elem.attrib['TObjSPU']
        if "TObjStr" in ngp_elem.attrib:
            ngp_sect_ign_condit.point = ngp_elem.attrib['TObjStr']
        if "OffPos" in ngp_elem.attrib:
            if ngp_elem.attrib['OffPos'] == "M":
                ngp_sect_ign_condit.position = "-"
            else:
                ngp_sect_ign_condit.position = "+"
        new_obj.oversizedMinus = [ngp_sect_ign_condit]

    ngm_elem = elem.find("NGM")
    if not (ngm_elem is None):
        ngm_sect_ign_condit = SectionAndIgnoreCondition()
        ngm_sect_ign_condit.section = ngm_elem.attrib['TObjSPU']
        if "TObjStr" in ngm_elem.attrib:
            ngm_sect_ign_condit.point = ngm_elem.attrib['TObjStr']
        if "OffPos" in ngm_elem.attrib:
            if ngm_elem.attrib['OffPos'] == "M":
                ngm_sect_ign_condit.position = "-"
            else:
                ngm_sect_ign_condit.position = "+"
        new_obj.oversizedPlus = [ngm_sect_ign_condit]

    m.append_obj(new_obj)
    # print(tag)
    # end = elem.find("End")

m.write_objs_intermediate_excel("PpoPoint")
m.write_objs_json("PpoPoint", "TObjectsPoint")

# point = PpoPoint("1")
# point.indent = "34"
#
# saic = SectionAndIgnoreCondition()
# saic.section = "1SP"
# saic.point = "3"
# saic.position = "+"
#
# as_1 = AdditionalSwitch()
# as_1.point = "1"
# as_1.selfPosition = "+"
# as_1.dependencePosition = "+"
#
# as_2 = AdditionalSwitch()
# as_2.point = "3"
# as_2.selfPosition = "-"
# as_2.dependencePosition = "-"
#
# point.additionalGuardLock = [saic]
# point.additionalSwitch = [as_1, as_2]
# m.append_obj(point)
# m.write_objs_json("PpoPoint", "TObjectsPoint")
