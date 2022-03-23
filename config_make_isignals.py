import xml.etree.ElementTree as ET
import os

from ppo_objects import PpoLightSignalCi, PpoLightSignalRi
from manager import Manager
from constants import INPUT_FOLDER, INTERFACE_FOLDER

input_train_et = ET.parse(os.path.join(INPUT_FOLDER, INTERFACE_FOLDER, "PpoTrafficLights.xml"))

m = Manager()
for elem in input_train_et.getroot():

    elem: ET.Element
    new_obj = PpoLightSignalCi()
    new_obj.tag = elem.attrib['Tag']
    new_obj.addrKi = int(elem.find("Addr").attrib['KI'])
    new_obj.addrUi = int(elem.find("Addr").attrib['UI'])
    new_obj.addrKa = "Fixed_1"
    new_obj.mode = "DN"
    type_ = elem.attrib['Type']

    if new_obj.tag.startswith("PCH"):
        new_obj.type_ = 7
    elif type_ == "BSWK":
        new_obj.type_ = 1
    elif type_ == "BSWS":
        new_obj.type_ = 2
    else:
        assert False

    m.append_obj(new_obj)

new_obj = PpoLightSignalRi()
new_obj.tag = "luzhskaya_CHU"
new_obj.addrKI_KO = "USO:MAX_UINT"
# new_obj.addrKI_KO = "Fixed_1"
new_obj.addrKI_S = "USO:1:1:19"
# new_obj.addrKI_RU = "USO:1:1:19"
new_obj.addrKI_GM = "USO:1:1:20"
m.append_obj(new_obj)

m.write_objs_json(["PpoLightSignalCi",
                   "PpoLightSignalRi"], "IObjectsSignal")
