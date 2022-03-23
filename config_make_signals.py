import xml.etree.ElementTree as ET
import os

from ppo_objects import PpoTrainSignal, PpoRepeatSignal, PpoShuntingSignal, PpoShuntingSignalWithTrackAnD, StartWarningArea
from manager import Manager
from constants import INPUT_FOLDER, TECHNOLOGY_FOLDER

input_train_et = ET.parse(os.path.join(INPUT_FOLDER, TECHNOLOGY_FOLDER, "PpoTrainSignals.xml"))
input_shunt_et = ET.parse(os.path.join(INPUT_FOLDER, TECHNOLOGY_FOLDER, "PpoShuntingSignals.xml"))

m = Manager()
for elem in input_train_et.getroot():

    elem: ET.Element
    if elem.attrib['Type'] in {"SvEnt", "SvOut"}:
        new_obj = PpoTrainSignal()
    elif elem.attrib['Type'] == "SvPv":
        new_obj = PpoRepeatSignal()
        new_obj.signalTag = elem.find("MainSv").attrib['TObj']
    else:
        assert False

    new_obj.tag = elem.attrib['Tag']
    new_obj.id_ = elem.attrib['Tag']
    new_obj.indent = elem.attrib['Tag']
    new_obj.iObjTag = elem.attrib['Tag']
    if elem.attrib['Tag'] == "CHM23":
        new_obj.startUp = "23BP"
    swa = StartWarningArea()
    if elem.attrib['Tag'] == "N":
        swa.obj = "IIGP"
        swa.point = 1
    else:
        swa.obj = "16P"
        # swa.point = 1
    new_obj.startWarningArea = swa
    new_obj.idControlArea = "ULTRAMAR"  # elem.find("RU").attrib['TObj']

    m.append_obj(new_obj)

for elem in input_shunt_et.getroot():

    elem: ET.Element
    tag = elem.attrib['Tag']
    if tag == "M36":
        new_obj = PpoShuntingSignalWithTrackAnD()
        new_obj.routePullTrain = "M36_M34"
    else:
        new_obj = PpoShuntingSignal()

    new_obj.tag = elem.attrib['Tag']
    new_obj.id_ = elem.attrib['Tag']
    new_obj.indent = elem.attrib['Tag']
    new_obj.iObjTag = elem.attrib['Tag']
    new_obj.idControlArea = "ULTRAMAR"

    m.append_obj(new_obj)

m.write_objs_json(["PpoTrainSignal", "PpoShuntingSignal", "PpoShuntingSignalWithTrackAnD", "PpoRepeatSignal"], "TObjectsSignal")

