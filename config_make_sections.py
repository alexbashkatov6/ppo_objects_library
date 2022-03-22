import xml.etree.ElementTree as ET
import os

from ppo_objects import PpoLineEnd, PpoTrackSection, PpoPointSection, PpoTrackAnDwithPoint, PpoAnDtrack
from manager import Manager
from constants import INPUT_FOLDER, TECHNOLOGY_FOLDER

input_line_end_et = ET.parse(os.path.join(INPUT_FOLDER, TECHNOLOGY_FOLDER, "PpoLineEnds.xml"))
input_track_ands_et = ET.parse(os.path.join(INPUT_FOLDER, TECHNOLOGY_FOLDER, "PpoTrackAnDs.xml"))
input_point_sect_et = ET.parse(os.path.join(INPUT_FOLDER, TECHNOLOGY_FOLDER, "PpoPointSections.xml"))
input_track_sect_et = ET.parse(os.path.join(INPUT_FOLDER, TECHNOLOGY_FOLDER, "PpoTrackSections.xml"))

m = Manager()
for elem in input_line_end_et.getroot():
    # print(elem)

    elem: ET.Element
    tag = elem.attrib['Tag']
    new_obj = PpoLineEnd()
    new_obj.tag = tag
    new_obj.id_ = tag
    new_obj.indent = tag
    new_obj.idControlArea = "ULTRAMAR"
    track_pu = elem.find("PU")
    if not (track_pu is None):
        new_obj.trackUnit = "track_{}".format(tag)
    else:
        new_obj.id_ = 0
        new_obj.indent = 0


    m.append_obj(new_obj)

for elem in input_track_ands_et.getroot():

    elem: ET.Element
    tag = elem.attrib['Tag']
    if tag == "23AP":
        new_obj = PpoTrackAnDwithPoint()
        new_obj.directionPointAnDTrack = "Direction12"
        new_obj.oppositeTrackAnDwithPoint = "23BP"
    elif tag == "23BP":
        new_obj = PpoTrackAnDwithPoint()
        new_obj.directionPointAnDTrack = "Direction21"
        new_obj.oppositeTrackAnDwithPoint = "23AP"
    else:
        new_obj = PpoAnDtrack()
    new_obj.tag = tag
    new_obj.id_ = tag
    new_obj.indent = tag
    new_obj.idControlArea = "ULTRAMAR"
    new_obj.trackUnit = "track_{}".format(tag)

    m.append_obj(new_obj)

for elem in input_point_sect_et.getroot():
    # print(elem)

    elem: ET.Element
    tag = elem.attrib['Tag']
    new_obj = PpoPointSection()
    new_obj.tag = tag
    new_obj.id_ = tag
    new_obj.indent = tag
    new_obj.idControlArea = "ULTRAMAR"
    new_obj.trackUnit = "track_{}".format(tag)

    m.append_obj(new_obj)

for elem in input_track_sect_et.getroot():
    # print(elem)

    elem: ET.Element
    tag = elem.attrib['Tag']
    new_obj = PpoTrackSection()
    new_obj.tag = tag
    new_obj.id_ = tag
    new_obj.indent = tag
    new_obj.idControlArea = "ULTRAMAR"
    new_obj.trackUnit = "track_{}".format(tag)

    m.append_obj(new_obj)

m.write_objs_json(["PpoLineEnd", "PpoAnDtrack", "PpoTrackAnDwithPoint", "PpoPointSection", "PpoTrackSection"], "TObjectsTrack")

