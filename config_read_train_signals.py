import xml.etree.ElementTree as ET
import os

from ppo_objects import PpoTrainSignal, PpoRepeatSignal
from manager import Manager
from constants import INPUT_FOLDER, TECHNOLOGY_FOLDER

input_et = ET.parse(os.path.join(INPUT_FOLDER, TECHNOLOGY_FOLDER, "PpoTrainSignals.xml"))

m = Manager()
for elem in input_et.getroot():

    elem: ET.Element
    if elem.attrib['Type'] in {"SvEnt", "SvOut"}:
        new_obj = PpoTrainSignal()
    elif elem.attrib['Type'] == "SvPv":
        new_obj = PpoRepeatSignal()
        new_obj.signalTag = elem.find("MainSv").attrib['TObj']
    else:
        # print(elem.attrib['Type'])
        assert False

    new_obj.tag = elem.attrib['Tag']
    new_obj.id_ = elem.attrib['Tag']
    new_obj.indent = elem.attrib['Tag']
    new_obj.iObjTag = elem.attrib['Tag']
    new_obj.idControlArea = "ULTRAMAR"  # elem.find("RU").attrib['TObj']

    m.append_obj(new_obj)

m.write_objs_json(["PpoTrainSignal", "PpoRepeatSignal"], "TObjectsSignal")

