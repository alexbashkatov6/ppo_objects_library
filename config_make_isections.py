import xml.etree.ElementTree as ET
import os

from ppo_objects import PpoTrackBSSO
from manager import Manager
from constants import INPUT_FOLDER, INTERFACE_FOLDER

track_et = ET.parse(os.path.join(INPUT_FOLDER, INTERFACE_FOLDER, "PpoTrackSensors.xml"))


m = Manager()
for elem in track_et.getroot():

    elem: ET.Element
    new_obj = PpoTrackBSSO()
    new_obj.tag = "track_{}".format(elem.attrib['Tag'])
    new_obj.addrKi = int(elem.find("Addr").attrib['KI'])
    new_obj.addrUi = int(elem.find("Addr").attrib['UI'])

    m.append_obj(new_obj)

m.write_objs_json("PpoTrackBSSO", "IObjectsTrack")