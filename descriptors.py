from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Type, Union, Iterable, Any, Optional
from dataclasses import dataclass

from custom_enum import CustomEnum


class AttributeEvaluateError(Exception):
    pass


class NameEvaluateError(AttributeEvaluateError):
    pass


class AENameRepeatingError(NameEvaluateError):
    pass


class AENameNotIdentifierError(NameEvaluateError):
    pass


class AENameEmptyError(NameEvaluateError):
    pass


class AEEnumValueAttributeError(AttributeEvaluateError):
    pass


class AEObjectNotFoundError(AttributeEvaluateError):
    pass


class AERequiredAttributeError(AttributeEvaluateError):
    pass


class AETypeAttributeError(AttributeEvaluateError):
    pass


class CommandType(CustomEnum):
    set_index = 0
    remove_index = 1


@dataclass
class IndexManagementCommand:
    command: CommandType
    index: int


class UniversalDescriptor(ABC):

    def __init__(self, *, is_required: bool = True, is_list: bool = False,
                 min_count: int = -1, exact_count: int = -1, immutable: bool = False,
                 internal_obj_type: str = "", default_value: Any = None, count_generate_to_excel: int = 1):
        self.is_required = is_required
        self.is_list = is_list
        assert (min_count == -1) or (exact_count == -1)
        self.min_count = min_count
        self.exact_count = exact_count
        self.immutable = immutable
        self.internal_obj_type = internal_obj_type
        self.default_value = default_value
        self.count_generate_to_excel = count_generate_to_excel
        # self.value_set = False

    @property
    def is_object(self) -> bool:
        return bool(self.internal_obj_type)

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if not instance:
            return self
        if not hasattr(instance, "_{}".format(self.name)):
            if self.default_value:
                setattr(instance, "_{}".format(self.name), self.default_value)
            elif self.is_list:
                setattr(instance, "_{}".format(self.name), [])
            else:
                setattr(instance, "_{}".format(self.name), "")
        return getattr(instance, "_{}".format(self.name))

    def __set__(self, instance, value: Union[str, tuple[Union[str, list[str]], Optional[IndexManagementCommand]]]):
        # if isinstance(value, str):
        #     if value and not value.isspace():
        #         self.value_set = True
        # elif isinstance(value, list):
        #     if value:
        #         self.value_set = True
        # else:
        #     self.value_set = True
        if not self.is_list:
            if isinstance(value, str):
                str_value = value.strip()
                setattr(instance, "_{}".format(self.name), self.handling_ap(str_value))
            else:
                setattr(instance, "_{}".format(self.name), self.handling_ap(value))
        else:  # self.is_list = True
            if not hasattr(instance, "_{}".format(self.name)):
                setattr(instance, "_{}".format(self.name), [])
            confirmed_values_list: list = getattr(instance, "_{}".format(self.name))
            if isinstance(value, tuple):
                assert len(value) == 2
                command = value[1].command
                index = value[1].index
                if command == "remove_index":
                    confirmed_values_list.pop(index)
                elif command == "set_index":
                    str_value = value[0]
                    if isinstance(str_value, str):
                        str_value = str_value.strip()
                    assert index <= len(confirmed_values_list)
                    if index == len(confirmed_values_list):
                        confirmed_values_list.append(self.handling_ap(str_value))
                    else:
                        confirmed_values_list[index] = self.handling_ap(str_value)
            else:  # assign command
                assert isinstance(value, list)
                confirmed_values_list.clear()
                for str_value in value:
                    confirmed_values_list.append(self.handling_ap(str_value))

    @abstractmethod
    def handling_ap(self, new_str_value: Any) -> Any:
        pass


class AnyDescriptor(UniversalDescriptor):
    def handling_ap(self, new_value: Any) -> Any:
        return new_value


class EnumDescriptor(UniversalDescriptor):

    def __init__(self, possible_values: list[str] = None, *, is_required: bool = True, is_list: bool = False,
                 min_count: int = -1, exact_count: int = -1, immutable: bool = False):
        super().__init__(is_required=is_required, is_list=is_list, min_count=min_count, exact_count=exact_count,
                         immutable=immutable)
        if not possible_values:
            self._possible_values = []
        else:
            self._possible_values = possible_values

    @property
    def possible_values(self) -> list[str]:
        return self._possible_values

    @possible_values.setter
    def possible_values(self, values: Iterable[str]):
        self._possible_values = list(values)

    def handling_ap(self, new_str_value: str) -> str:
        if new_str_value not in self.possible_values:
            raise AEEnumValueAttributeError("Value '{}' not in possible list: '{}'".format(new_str_value,
                                                                                           self.possible_values))
        return new_str_value


if __name__ == "__main__":
    class CELightColor(CustomEnum):
        dark = 0
        red = 1
        blue = 2
        white = 3
        yellow = 4
        green = 5

    class TestObject:
        test_enum = EnumDescriptor(CELightColor.possible_values)
        test_enum_list = EnumDescriptor(CELightColor.possible_values, is_list=True)
        test_any = AnyDescriptor()

    class TestAny:
        pass

    to = TestObject()
    to.test_enum = "dark"
    print(to.test_enum)
    to.test_enum_list = ["dark", "red", "red"]
    print(to.test_enum_list)
    to.test_enum_list = ("green", IndexManagementCommand(CommandType(CommandType.set_index), 1))
    print(to.test_enum_list)
    to.test_enum_list = ("green", IndexManagementCommand(CommandType(CommandType.set_index), 3))
    print(to.test_enum_list)
    to.test_enum_list = ("", IndexManagementCommand(CommandType(CommandType.remove_index), 3))
    print(to.test_enum_list)
    to.test_enum_list = ("", IndexManagementCommand(CommandType(CommandType.remove_index), 0))
    print(to.test_enum_list)
    to.test_any = TestAny()
    print(to.test_any)

    to.test_enum_list = []
    print(to.test_enum_list)
    to.test_enum_list = ("green", IndexManagementCommand(CommandType(CommandType.set_index), 0))
    print(to.test_enum_list)
