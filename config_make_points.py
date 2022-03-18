import xml.etree.ElementTree as ET
import os

from ppo_objects import PpoPoint, SectionAndIgnoreCondition
from manager import Manager
from constants import INPUT_FOLDER, TECHNOLOGY_FOLDER

points_et = ET.parse(os.path.join(INPUT_FOLDER, TECHNOLOGY_FOLDER, "PpoPoints.xml"))


m = Manager()
for elem in points_et.getroot():

    elem: ET.Element
    new_obj = PpoPoint()

    new_obj.tag = elem.attrib['Tag']
    new_obj.id_ = elem.attrib['Tag']
    new_obj.indent = elem.attrib['Tag']
    new_obj.iObjTag = elem.attrib['Tag']
    if elem.attrib['Tag'] == "24":
        new_obj.type_ = "2"
    new_obj.pointsMonitoring = "STRELKI"
    new_obj.idControlArea = elem.find("RU").attrib['TObj']
    new_obj.section = elem.find("Sek").attrib['TObj']
    new_obj.railFittersWarningArea = elem.find("MP").attrib['TObj']
    pair_point_el = elem.find("St2")
    if not (pair_point_el is None):
        new_obj.pairPoint = pair_point_el.attrib['TObj']
    ohr_plus = elem.find("OP")
    if not (ohr_plus is None):
        posit = ohr_plus.attrib['TObj']
        guard_point = posit[1:]
        if posit[0] == "+":
            new_obj.guardPlusPlus = [guard_point]
        else:
            new_obj.guardPlusMinus = [guard_point]
    ohr_minus = elem.find("OM")
    if not (ohr_minus is None):
        posit = ohr_minus.attrib['TObj']
        guard_point = posit[1:]
        if posit[0] == "+":
            new_obj.guardMinusPlus = [guard_point]
        else:
            new_obj.guardMinusMinus = [guard_point]
    loc_plus = elem.find("ZP")
    if not (loc_plus is None):
        loc_sect = loc_plus.attrib['TObj']
        new_obj.lockingPlus = [loc_sect]
    loc_minus = elem.find("ZM")
    if not (loc_minus is None):
        loc_sect = loc_minus.attrib['TObj']
        new_obj.lockingMinus = [loc_sect]

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
