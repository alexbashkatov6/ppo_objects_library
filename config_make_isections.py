import xml.etree.ElementTree as ET
import os

from ppo_objects import PpoAxisCountingCi, PpoTrackUnit
from manager import Manager
from constants import INPUT_FOLDER, INTERFACE_FOLDER

track_et = ET.parse(os.path.join(INPUT_FOLDER, INTERFACE_FOLDER, "PpoTrackSensors.xml"))


m = Manager()
for elem in track_et.getroot():

    elem: ET.Element
    new_obj = PpoAxisCountingCi()
    ci_tag = elem.attrib['Tag']
    new_obj.tag = ci_tag
    new_obj.receiverAddr = int(elem.find("Addr").attrib['KI'])
    m.append_obj(new_obj)

    new_obj = PpoTrackUnit()
    new_obj.tag = "track_{}".format(elem.attrib['Tag'])
    new_obj.iObjsTag = [ci_tag]
    m.append_obj(new_obj)

m.write_objs_json(["PpoAxisCountingCi",
                   "PpoTrackUnit"], "IObjectsTrack")