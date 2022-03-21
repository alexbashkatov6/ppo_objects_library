import xml.etree.ElementTree as ET
import os

from ppo_objects import PpoGroupRailFittersWarningArea, PpoRailFittersWarningAreaRi, PpoRailFittersWarningArea
from manager import Manager
from constants import INPUT_FOLDER, INTERFACE_FOLDER, TECHNOLOGY_FOLDER

to_fitters_et = ET.parse(os.path.join(INPUT_FOLDER, TECHNOLOGY_FOLDER, "PpoRailFittersWarningAreas.xml"))
io_fitters_et = ET.parse(os.path.join(INPUT_FOLDER, INTERFACE_FOLDER, "PpoRailFittersWarningAreas.xml"))

m = Manager()
for elem in to_fitters_et.getroot():

    elem: ET.Element
    tag = elem.attrib['Tag']
    type_ = elem.attrib['Type']
    if type_ == "GroupOM":
        new_obj = PpoGroupRailFittersWarningArea()
    elif type_ == "OM":
        new_obj = PpoRailFittersWarningArea()
        new_obj.id_ = tag
        new_obj.indent = tag
        new_obj.group = elem.find("GroupOM").attrib['TObj']
        new_obj.idControlArea = elem.find("RU").attrib['TObj']
        new_obj.iObjTag = elem.find("OM").attrib['IObj']
        new_obj.points = elem.find("Str").attrib['TObj'].split(" ")
    else:
        assert False
    new_obj.tag = tag

    m.append_obj(new_obj)

for elem in io_fitters_et.getroot():

    elem: ET.Element
    type_ = elem.attrib['Type']
    if type_ == "OM":
        new_obj = PpoRailFittersWarningAreaRi()
        new_obj.tag = elem.attrib['Tag']
        knm = elem.find("AddrKI").attrib['KNM']
        om = elem.find("AddrUI").attrib['OM']
        new_obj.AddrMKI_KNM = "USO:{}".format(knm)
        new_obj.AddrMUI_OM = "USO:{}".format(om)
        # print("om", new_obj.AddrMKI_OM)
    elif type_ == "RRM":
        # print("om2", new_obj.AddrMKI_OM)
        rrm = elem.find("AddrUI").attrib['RRM']
        new_obj.AddrMUI_RRM = "USO:{}".format(rrm)
        # print("om3", new_obj.AddrMKI_OM)
        m.append_obj(new_obj)
    else:
        assert False

# print(m.ppo_objs["PpoRailFittersWarningAreaRi"]['OM1_1'].AddrMKI_OM)

m.write_objs_json(["PpoGroupRailFittersWarningArea", "PpoRailFittersWarningArea", "PpoRailFittersWarningAreaRi"], "RailWarningArea")
