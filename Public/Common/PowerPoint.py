from time import sleep

from func_timeout import func_set_timeout
from func_timeout.exceptions import FunctionTimedOut
from poium import Elements
from poium.common import logging
from poium.common.exceptions import PageElementError


class PowerPoint:

    def __init__(self, page: dict, module):
        """

        :param page: 元素集合
        :param module: 功能模块
        """
        self.power_point = page[module]

    def Input(self, describe, input_str):
        el = self.power_point[describe]
        el.send_keys(input_str)

    def Click(self, describe):
        el = self.power_point[describe]
        el.click()

    def Text(self, describe):
        el = self.power_point[describe]
        text = el.text()
        return text

    def __getitem__(self, item):
        return self.power_point[item]



