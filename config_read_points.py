import xml.etree.ElementTree as ET
import os

from ppo_objects import PpoPoint, SectionAndIgnoreCondition, AdditionalSwitch
from manager import Manager
from constants import INPUT_FOLDER, TECHNOLOGY_FOLDER, INTERFACE_FOLDER, OUTPUT_FOLDER, PYTHON_KEYWORD_REPLACES

points_et = ET.parse(os.path.join(INPUT_FOLDER, TECHNOLOGY_FOLDER, "PpoPoints.xml"))


for elem in points_et.getroot():
    elem: ET.Element
    tag = elem.attrib['Tag']
    end = elem.find("End")

m = Manager()
point = PpoPoint("1")
point.indent = "34"

saic = SectionAndIgnoreCondition()
saic.section = "1SP"
saic.point = "3"
saic.position = "+"

as_1 = AdditionalSwitch()
as_1.point = "1"
as_1.selfPosition = "+"
as_1.dependencePosition = "+"

as_2 = AdditionalSwitch()
as_2.point = "3"
as_2.selfPosition = "-"
as_2.dependencePosition = "-"

point.additionalGuardLock = [saic]
point.additionalSwitch = [as_1, as_2]
m.append_obj(point)
m.write_objs_json("PpoPoint", "TObjectsPoint")
m.write_objs_intermediate_excel("PpoPoint")
