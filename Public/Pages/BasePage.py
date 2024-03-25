# 页面基类

from poium import Page, Element
from selenium.webdriver.remote.webelement import WebElement
import time
from datetime import datetime


class basePage(Page):
    # 元素文件
    element_file = "elements_xpath_loc.xlsx"

    # 获取该元素的文本
    @staticmethod
    def get_element_text(tag, attribute, value, num, *children):
        start_xpath = '//{0}[@{1}=\"{2}\"][{3}] '.format('{0}'.format(tag), '{0}'.format(attribute),
                                                         '{0}'.format(value), '{0}'.format(num))
        if children is None:
            x_path = start_xpath
            elem = Element(xpath=x_path)
            print("该元素为：" + x_path)
            print("该元素的文本为：" + elem.text)
            return elem.text
        for i in range(len(children)):
            start_xpath += '/{0}'.format(children[i])
        x_path = start_xpath
        elem = Element(xpath=x_path)
        print("该元素为：" + x_path)
        print("该元素的文本为：" + elem.text)
        return elem.text

    # 实现某元素下的再次寻找元素
    def element_to_element(self, father_elem: tuple, father_index: int, child_elem: tuple, child_index: int) -> WebElement:
        driver = self.driver
        try:
            fr = driver.find_elements(*father_elem)
            if len(fr) != 0:
                cd = fr[father_index].find_elements(*child_elem)
                if len(cd) != 0:
                    return cd[child_index]
        except Exception as e:
            raise e

    # 判断元素是否存在
    @staticmethod
    def isElementExist(elem):
        flag = True
        if len(elem) == 0:
            flag = False
            return flag
        elif len(elem) >= 1:
            return flag



