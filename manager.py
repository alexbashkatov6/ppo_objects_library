from collections import OrderedDict
from typing import Union
import json
import os
import xlwt
import xlrd

from descriptors import IndexManagementCommand, CommandType
from ppo_objects import PpoObject, PpoRoutePointer, PpoRoutePointerRi, PpoTrainSignal, PpoShuntingSignal, \
    PpoShuntingSignalWithTrackAnD, PpoLightSignalCi, PpoAnDtrack, PpoTrackAnDwithPoint, PpoLineEnd, PpoPointSection, \
    PpoTrackSection, AdditionalSwitch, SectionAndIgnoreCondition, NotificationPoint, PpoPoint, PpoControlAreaBorder, \
    PpoSemiAutomaticBlockingSystem, PpoSemiAutomaticBlockingSystemRi, PpoAutomaticBlockingSystem, \
    PpoAutomaticBlockingSystemRi, PpoTrackCrossroad, PpoTrainNotificationRi, PpoRailCrossingRi, PpoRailCrossing, \
    PpoControlDeviceDerailmentStock, PpoControlDeviceDerailmentStockCi, PpoTrackUnit, PpoTrackReceiverRi, \
    PpoLightSignalRi, PpoRepeatSignal, PpoPointMachineCi, PpoAxisCountingCi, PpoGroupRailFittersWarningArea, \
    PpoRailFittersWarningAreaRi, PpoRailFittersWarningArea, PpoCabinetUsoBk, PpoInsulationResistanceMonitoring, \
    PpoPointMachinesCurrentMonitoring, PpoTelesignalization, PpoPointsMonitoring, PpoLightModeRi, PpoLightMode, \
    PpoFireAndSecurityAlarm, PpoGeneralPurposeRelayInput, PpoGeneralPurposeRelayOutput, StartWarningArea
from constants import INPUT_FOLDER, OUTPUT_FOLDER, INTERMEDIATE_IN_FOLDER, INTERMEDIATE_OUT_FOLDER, \
    PYTHON_KEYWORD_REPLACES


class Manager:
    def __init__(self):
        self.refresh_odict()

    def refresh_odict(self):
        self.ppo_objs = OrderedDict()
        for sbcls in PpoObject.__subclasses__():
            self.ppo_objs[sbcls.__name__] = OrderedDict()

    def append_obj(self, obj: PpoObject):
        self.ppo_objs[obj.__class__.__name__][obj.tag] = obj

    def get_attrib_names(self, cls_name: str) -> list[str]:
        cls = eval(cls_name)
        return [attr_name for attr_name in cls.__dict__ if not attr_name.startswith("__")]

    def value_is_meaningful(self, value):
        if isinstance(value, str):
            if value and not value.isspace():
                return True
        elif isinstance(value, list):
            if value:
                return True
        else:
            return True
        return False

    def extract_obj_attribs(self, obj: PpoObject) -> OrderedDict:
        cls = obj.__class__
        cls_name = cls.__name__
        attr_names = self.get_attrib_names(cls_name)  # [attr_name for attr_name in cls.__dict__ if not attr_name.startswith("__")]
        attr_odict = OrderedDict()
        for attr_name in attr_names:
            in_dict_attr_name = attr_name
            if attr_name in PYTHON_KEYWORD_REPLACES:
                in_dict_attr_name = PYTHON_KEYWORD_REPLACES[attr_name]
            descr = getattr(cls, attr_name)
            value = getattr(obj, attr_name)
            # if (not descr.value_set) and (not descr.is_required):
            if (not self.value_is_meaningful(value)) and (not descr.is_required):
                continue
            if descr.is_object:
                if descr.is_list:
                    attr_odict[in_dict_attr_name] = [self.extract_obj_attribs(internal_obj) for internal_obj in getattr(obj, attr_name)]
                else:
                    attr_odict[in_dict_attr_name] = self.extract_obj_attribs(getattr(obj, attr_name))
            else:
                attr_odict[in_dict_attr_name] = getattr(obj, attr_name)
        return attr_odict

    # def make_objs_attr_odict(self, cls_name: str) -> :

    def write_objs_json(self, cls_names: Union[str, list[str]], file_name: str = ""):
        if isinstance(cls_names, str):
            cls_names = [cls_names]
        if not file_name:
            file_name = cls_names[0]
        obj_jsons = []
        for cls_name in cls_names:
            objs = self.ppo_objs[cls_name].values()
            for obj in objs:
                attr_odict = OrderedDict()
                attr_odict["class"] = cls_name
                attr_odict["tag"] = obj.tag
                attr_odict["data"] = self.extract_obj_attribs(obj)
                obj_jsons.append(attr_odict)
        with open(os.path.join(OUTPUT_FOLDER, "{}.json".format(file_name)), "w") as write_file:
            json.dump(obj_jsons, write_file, indent=4)

    def write_objs_intermediate_excel(self, cls_name: str, file_name: str = ""):
        """ not implemented if triple object nesting """
        if not file_name:
            file_name = cls_name
        objs = self.ppo_objs[cls_name].values()

        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet("Лист 1")

        """ 01. Generate header """
        headers = ["tag"]
        cls = eval(cls_name)
        attr_names = self.get_attrib_names(cls_name)
        for attr_name in attr_names:
            descr = getattr(cls, attr_name)
            if descr.is_object:
                attr_cls = eval(descr.internal_obj_type)
                internal_attr_names = self.get_attrib_names(attr_cls.__name__)
                if descr.count_generate_to_excel == 1:
                    for internal_attr_name in internal_attr_names:
                        headers.append("{}_{}".format(attr_name, internal_attr_name))
                else:
                    for i in range(descr.count_generate_to_excel):
                        for internal_attr_name in internal_attr_names:
                            headers.append("{}_{}_{}".format(attr_name, internal_attr_name, i+1))
            else:
                headers.append(attr_name)

        for j, attr_name in enumerate(headers):
            worksheet.write(0, j, attr_name)

        """ 02. Generate rows """
        for i, obj in enumerate(objs):
            for j, attr_name in enumerate(headers):
                if ("_" not in attr_name) or (attr_name in PYTHON_KEYWORD_REPLACES):
                    worksheet.write(i+1, j, getattr(obj, attr_name))
                else:  # internal object
                    params = attr_name.split("_")
                    if len(params) == 2:
                        index = 0
                    else:
                        index = int(params[2]) - 1
                    attr_name = params[0]
                    internal_attr_name = params[1]
                    internal_obj_list = getattr(obj, attr_name)
                    if index < len(internal_obj_list):
                        internal_obj = internal_obj_list[index]
                        worksheet.write(i + 1, j, getattr(internal_obj, internal_attr_name))

        workbook.save(os.path.join(INTERMEDIATE_OUT_FOLDER, "{}.xls".format(file_name)))

    def read_objs_intermediate_excel(self, cls_name: str, file_name: str = ""):
        assert cls_name in self.ppo_objs
        cls = eval(cls_name)
        self.ppo_objs[cls_name] = OrderedDict()
        if not file_name:
            file_name = cls_name
        rb = xlrd.open_workbook(os.path.join(INTERMEDIATE_IN_FOLDER, "{}.xls".format(file_name)), formatting_info=True)
        worksheet = rb.sheet_by_index(0)
        attr_names = worksheet.row_values(0)
        for rownum in range(1, worksheet.nrows):
            new_obj = cls()
            attr_str_values = worksheet.row_values(rownum)
            assert attr_str_values[0]  # tag
            for i, attr_str_value in enumerate(attr_str_values):
                attr_name = attr_names[i]
                if ("_" not in attr_name) or (attr_name in PYTHON_KEYWORD_REPLACES):
                    descr = getattr(cls, attr_name)
                    if descr.is_list:
                        if attr_str_value and not attr_str_value.isspace():
                            setattr(new_obj, attr_name, attr_str_value.split(" "))
                        else:
                            setattr(new_obj, attr_name, [])
                    else:
                        setattr(new_obj, attr_name, attr_str_value)
                else:  # internal object
                    params = attr_name.split("_")
                    if len(params) == 2:
                        index = 0
                    else:
                        index = int(params[2]) - 1
                    attr_name = params[0]
                    internal_attr_name = params[1]

                    if attr_str_value and not attr_str_value.isspace():
                        old_internal_objs_list = getattr(new_obj, attr_name)
                        if len(old_internal_objs_list) < index+1:
                            descr = getattr(cls, attr_name)
                            internal_attr_cls = eval(descr.internal_obj_type)
                            internal_obj = internal_attr_cls()
                            setattr(new_obj, attr_name, (internal_obj, IndexManagementCommand(CommandType(CommandType.set_index), index)))
                        setattr(old_internal_objs_list[index], internal_attr_name, attr_str_value)
            self.ppo_objs[cls_name][new_obj.tag] = new_obj


if __name__ == "__main__":
    test_1 = False
    if test_1:
        m = Manager()
        print(m.ppo_objs)
        pss = PpoShuntingSignal("M1")
        m.append_obj(pss)
        m.write_objs_json("PpoShuntingSignal")
        m.write_objs_intermediate_excel("PpoPoint")
        m.read_objs_intermediate_excel("PpoPoint")
        m.write_objs_json("PpoPoint")

    test_2 = True
    if test_2:
        m = Manager()
        m.write_objs_intermediate_excel("PpoAutomaticBlockingSystemRi")
