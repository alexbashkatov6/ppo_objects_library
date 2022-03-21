import xml.etree.ElementTree as ET
import os

from ppo_objects import PpoPointMachineCi
from manager import Manager
from constants import INPUT_FOLDER, INTERFACE_FOLDER

points_et = ET.parse(os.path.join(INPUT_FOLDER, INTERFACE_FOLDER, "PpoPointMachines.xml"))


m = Manager()
for elem in points_et.getroot():

    elem: ET.Element
    new_obj = PpoPointMachineCi()
    new_obj.tag = elem.attrib['Tag']
    new_obj.addrKi = int(elem.find("Addr").attrib['KI'])
    new_obj.addrUi = int(elem.find("Addr").attrib['UI'])

    m.append_obj(new_obj)

m.write_objs_json("PpoPointMachineCi", "IObjectsPoint")
