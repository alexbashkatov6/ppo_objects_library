import xml.etree.ElementTree as ET
import os

from ppo_objects import PpoCabinetUsoBk, PpoInsulationResistanceMonitoring, PpoPointMachinesCurrentMonitoring, \
    PpoTelesignalization, PpoPointsMonitoring, PpoLightModeRi, PpoLightMode, PpoFireAndSecurityAlarm, \
    PpoGeneralPurposeRelayInput, PpoGeneralPurposeRelayOutput
from manager import Manager
from constants import INPUT_FOLDER, INTERFACE_FOLDER

input_train_et = ET.parse(os.path.join(INPUT_FOLDER, INTERFACE_FOLDER, "PpoCabinetsUSOBK.xml"))

m = Manager()
cabinets = []
for elem in input_train_et.getroot():

    elem: ET.Element
    tag = elem.attrib['Tag']
    type_ = elem.attrib['Type']
    if "Crate1" in tag:
        new_obj = PpoCabinetUsoBk()
        new_obj.controlDeviceDerailmentStocks = []
        hi_crate = elem.find("BST").attrib['IObj'].split(" ")
        new_obj.hiCratePointMachines = hi_crate
    elif "Crate" in type_:
        lo_crate = elem.find("BST").attrib['IObj'].split(" ")
        new_obj.loCratePointMachines = lo_crate
    elif "Cabinet" in type_:
        usobk_symbol = tag[-1]
        if usobk_symbol == "2":
            new_obj.lightSignals = ["N", "CH1", "PCH1", "CH2", "PCH2", "CH3", "PCH3", "CH4", "PCH4", "CH9", "PCH9",
                                    "CH10", "PCH10", "CH7", "PCH7", "CH8", "PCH8", "M6"]
        elif usobk_symbol == "3":
            new_obj.lightSignals = ["M1", "M3", "M5", "M7", "M9", "M11", "M13", "M15", "M17", "M19", "M21", "M23",
                                    "M25", "M27", "M29", "M31", "M33", "M8", "M2", "M4"]
        elif usobk_symbol == "4":
            new_obj.lightSignals = ["M10", "M12", "M14", "M16", "M18", "M20", "M22", "M26", "M28", "M30", "M32", "M34",
                                    "M36", "M38", "M40", "M42", "M44", "M46", "M48"]
        elif usobk_symbol == "5":
            new_obj.lightSignals = ["CHM23", "M50", "CHM24", "M52", "CHM25", "M54", "CHM26", "M56", "CHM27", "M58",
                                    "CHM28", "M60", "CHM29", "M62", "CHM30", "M64", "NM3", "M66", "NM2", "M68", "NM1",
                                    "M24"]
        else:
            assert False
        new_obj.tag = "UsoBk{}".format(usobk_symbol)
        cabinets.append(new_obj.tag)
        m.append_obj(new_obj)
    else:
        assert False

new_obj = PpoInsulationResistanceMonitoring()
new_obj.tag = "ControlIzolation"
new_obj.cabinets = cabinets
new_obj.addrKI_OK = "USO:1:1:5"
m.append_obj(new_obj)

new_obj = PpoPointMachinesCurrentMonitoring()
new_obj.tag = "KTPS"
new_obj.cabinets = cabinets
new_obj.addrKI_KTPS = "NoAddr"
m.append_obj(new_obj)

new_obj = PpoTelesignalization()
new_obj.tag = "ControlIzolation"
new_obj.id_ = "OSI_KSIZ"
new_obj.indent = "OSI_KSIZ"
new_obj.idControlArea = "ULTRAMAR"
new_obj.iObjTag = "ControlIzolation"
m.append_obj(new_obj)

new_obj = PpoTelesignalization()
new_obj.tag = "KTPS"
new_obj.id_ = "KTPS"
new_obj.indent = "KTPS"
new_obj.idControlArea = "ULTRAMAR"
new_obj.iObjTag = "KTPS"
m.append_obj(new_obj)

new_obj = PpoPointsMonitoring()
new_obj.tag = "STRELKI"
new_obj.id_ = "STRELKI"
new_obj.indent = "STRELKI"
new_obj.idControlArea = "ULTRAMAR"
m.append_obj(new_obj)

new_obj = PpoLightModeRi()
new_obj.tag = "DN"
new_obj.addrKI_DN1 = "NoAddr"
new_obj.addrKI_DN2 = "SPU:1:20"
new_obj.addrKI_DSN = "Fixed_1"
new_obj.addrUI_DN = "USO:1:1:4"
new_obj.addrUI_DSN = "NoAddr"
new_obj.addrUI_ASV = "USO:1:1:5"
m.append_obj(new_obj)

new_obj = PpoLightMode()
new_obj.tag = "DN"
new_obj.id_ = "DN"
new_obj.indent = "DN"
new_obj.idControlArea = "ULTRAMAR"
new_obj.iObjTag = "DN"
m.append_obj(new_obj)

new_obj = PpoFireAndSecurityAlarm()
new_obj.tag = "POS"
new_obj.id_ = "POS"
new_obj.indent = "POS"
new_obj.idControlArea = "ULTRAMAR"
new_obj.iObjTag = "POS"
m.append_obj(new_obj)

for text in ["OSI_KPA", "OSI_APK", "OSI_VZU", "SCHVP", "OSI_APU", "OSI_F1", "OSI_F2"]:
    new_obj = PpoTelesignalization()
    new_obj.tag = text
    new_obj.id_ = text
    new_obj.indent = text
    new_obj.idControlArea = "ULTRAMAR"
    new_obj.iObjTag = text
    m.append_obj(new_obj)

m.write_objs_json(["PpoCabinetUsoBk",
                   "PpoInsulationResistanceMonitoring",
                   "PpoPointMachinesCurrentMonitoring",
                   "PpoTelesignalization",
                   "PpoPointsMonitoring",
                   "PpoLightModeRi",
                   "PpoLightMode",
                   "PpoFireAndSecurityAlarm"], "Telesignalization")

new_obj = PpoGeneralPurposeRelayInput()
new_obj.tag = "OSI_KPA"
new_obj.inputAddr = ["USO:1:1:3"]
m.append_obj(new_obj)

new_obj = PpoGeneralPurposeRelayInput()
new_obj.tag = "OSI_APK"
new_obj.inputAddr = ["USO:1:1:4"]
m.append_obj(new_obj)

new_obj = PpoGeneralPurposeRelayInput()
new_obj.tag = "OSI_VZU"
new_obj.inputAddr = ["USO:1:1:6"]
m.append_obj(new_obj)

new_obj = PpoGeneralPurposeRelayInput()
new_obj.tag = "POS"
new_obj.inputAddr = ["USO:1:1:8", "USO:1:1:7", "USO:1:1:9"]
m.append_obj(new_obj)

new_obj = PpoGeneralPurposeRelayInput()
new_obj.tag = "OSI_F1"
new_obj.inputAddr = ["SPU:1:6", "SPU:1:12"]
m.append_obj(new_obj)

new_obj = PpoGeneralPurposeRelayInput()
new_obj.tag = "OSI_F2"
new_obj.inputAddr = ["SPU:1:8", "SPU:1:14"]
m.append_obj(new_obj)

new_obj = PpoGeneralPurposeRelayInput()
new_obj.tag = "SCHVP"
new_obj.inputAddr = ["SPU:1:2", "SPU:1:4"]
m.append_obj(new_obj)

new_obj = PpoGeneralPurposeRelayInput()
new_obj.tag = "OSI_APU"
new_obj.inputAddr = ["SPU:1:18"]
m.append_obj(new_obj)

new_obj = PpoGeneralPurposeRelayOutput()
new_obj.tag = "SNK_IIGP"
new_obj.addrUI = "USO:1:1:10"
m.append_obj(new_obj)

new_obj = PpoGeneralPurposeRelayOutput()
new_obj.tag = "OV_IIGP"
new_obj.addrUI = "USO:1:1:11"
m.append_obj(new_obj)

new_obj = PpoGeneralPurposeRelayOutput()
new_obj.tag = "PV_IIGP"
new_obj.addrUI = "USO:1:1:12"
m.append_obj(new_obj)

m.write_objs_json(["PpoGeneralPurposeRelayInput",
                   "PpoGeneralPurposeRelayOutput"], "IObjectsRelay")

