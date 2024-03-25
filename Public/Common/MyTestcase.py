import unittest
from typing import Optional, Union
from unittest.util import safe_repr

from poium.common.logging import logging


class MyTestCase(unittest.TestCase):

    @classmethod
    def init_method(cls, driver):
        cls.driver = driver
        driver.implicitly_wait(6)
        driver.maximize_window()
        # driver.execute_script("document.body.style.zoom='0.75'")

    '''
    '''

    @staticmethod
    def log_pass():
        logging.info("测试通过！！！")

    @staticmethod
    def log_fail():
        logging.error("测试不通过！！！")

    def collect_error(self, msg_list: list) -> str:
        """

        :param msg_list: 异常信息列表
        :return: 返回整理好的异常信息
        """
        self.error_msg = ""
        for idx, value in enumerate(msg_list):
            if idx == 0:
                self.error_msg += "{0}".format(value)
            else:
                self.error_msg += "\n{0}".format(value)
        return self.error_msg

    '''
    '''

    def isError_and_InsertToList(self, msg: Union[str, list]) -> list[Optional[str]]:
        """
        判断是否为
        :param msg: 要判断的参数，支持str和list
        :return: 返回异常信息列表
        """
        self.msg_list = []
        if isinstance(msg, str):
            self.msg_list.append(msg)
            return self.msg_list
        elif isinstance(msg, list):
            for idx, value in enumerate(msg):
                if value != 0:
                    self.msg_list.append(value)
            return self.msg_list
        else:
            return self.msg_list

    def assert_IsEqual_But_NotRaise(self, first, second, isEqual: bool):
        """
        通过first和second断言是否相等，只捕捉异常但不抛出异常
        :param first:   预期
        :param second:  实际
        :param isEqual: true为assertEqual，false为assertNotEqual
        :return: 异常或0
        """
        if isEqual:
            if not first == second:
                self.standardMsg = "{0} != {1}".format(first, second)
                logging.error("In order to 期望与实际相等，but期望值 '{0}' 却与实际值 '{1}' 不相等！".format(first, second))
                return self.standardMsg
            else:
                logging.info("(期望值:'{0}') == (实际值:'{1}')----------断言成功！".format(first, second))
                return 0
        elif not isEqual:
            if not first != second:
                self.standardMsg = "{0} == {1}".format(first, second)
                logging.error("In order to 期望与实际不相等，but期望值 '{0}' 却与实际值 '{1}' 相等！".format(first, second))
                return self.standardMsg
            else:
                logging.info("(期望值:'{0}') != (实际值:'{1}')----------断言成功！".format(first, second))
                return 0

    '''
    '''

    def assert_IsIn_But_NotRaise(self, member, container, isIn: bool):
        """

        :param member:
        :param container:
        :param isIn:
        :return:
        """
        if isIn:
            if member not in container:
                self.standardMsg = '%s not found in %s' % (safe_repr(member),
                                                           safe_repr(container))
                logging.error("'{0}'不符合期望，不存在于源码中！".format(member))
                return self.standardMsg
            else:
                logging.info("'{0}'符合期望，存在于源码中！----------断言成功！".format(member))
                return 0
        elif not isIn:
            if member in container:
                standardMsg = '%s unexpectedly found in %s' % (safe_repr(member),
                                                               safe_repr(container))
                logging.error("'{0}'不符合期望，存在于源码中！".format(member))
                return standardMsg
            else:
                logging.info("'{0}'符合期望，不存在于源码中！----------断言成功！".format(member))
                return 0

    '''
    '''

    def assertIsIn_by_list(self, assert_list: list, all_source, isIn: bool, isRaise: bool):
        """

        :param assert_list: 需要判断的文本列表
        :param all_source:  判断依据
        :param isIn: true为assertIn，false为assertNotIn
        :param isRaise: 存在异常时是否要抛出异常信息
        :return: isRaise为True直接抛出异常信息而不会返回值，isRaise为False才会返回异常信息
        """
        message = []
        for idx, value in enumerate(assert_list):
            standardMsg = self.assert_IsIn_But_NotRaise(value, all_source, isIn)
            temporary_list = self.isError_and_InsertToList(standardMsg)
            message.extend(temporary_list)

        if len(message) != 0:
            error = self.collect_error(message)
            if isRaise:
                self.fail("\n" + error)
            elif not isRaise:
                return error

    '''
    '''

    def assertIsEqual_by_list(self, assert_list, judge_list, isEqual: bool, isRaise: bool):
        """

        :param assert_list:
        :param judge_list:
        :param isEqual:
        :param isRaise:
        :return:
        """
        message = []
        for idx, value in enumerate(assert_list):
            standardMsg = self.assert_IsEqual_But_NotRaise(value, judge_list[idx], isEqual)
            temporary_list = self.isError_and_InsertToList(standardMsg)
            message.extend(temporary_list)

        if len(message) != 0:
            error = self.collect_error(message)
            if isRaise:
                self.fail("\n" + error)
            elif not isRaise:
                return error

    '''
    '''

    def assert_style_isConform(self, element, target_style: str, isEqual: bool):
        """
        通过style属性判断元素格式是否符合预期
        :param element: 要获取style属性的元素
        :param target_style: 元素的目标style属性
        :param isEqual: true为assertEqual，false为assertNotEqual
        :return:

        """

        real_style = element.get_attribute('style')
        error_msg = self.assert_IsEqual_But_NotRaise(target_style, real_style, isEqual)
        if error_msg != 0:
            self.fail(error_msg)

    '''
    '''

    def assert_url(self, target_url: str, title: str = None, text: str = None):
        """
        判断页面是否跳转成功
        :param target_url: 目标页面
        :param title: 目标页面的title
        :param text: 网页存在的文本
        :return:
        """
        msg = []
        m1 = self.assert_IsEqual_But_NotRaise(target_url, self.driver.current_url, isEqual=True)
        msg.extend(self.isError_and_InsertToList(m1))
        if title is not None:
            m2 = self.assert_IsEqual_But_NotRaise(title, self.driver.title, isEqual=True)
            msg.extend(self.isError_and_InsertToList(m2))
        if text is not None:
            m3 = self.assert_IsIn_But_NotRaise(text, self.driver.page_source, isIn=True)
            msg.extend(self.isError_and_InsertToList(m3))

        if len(msg) != 0:
            error_msg = self.collect_error(msg)
            self.fail("\n" + error_msg)

    '''
    '''

    def assert_cookie_IsExist(self, name, value, IsExist: bool):
        """

        :param name: 需要判断的cookie的name
        :param value: 需要判断的cookie的value
        :param IsExist: 目标cookie是否需要存在
        :return:
        """
        Is = 0
        error_msg = ""
        all_cookies = self.driver.get_cookies()
        if len(all_cookies) != 0:
            for idx, val in enumerate(all_cookies):
                if IsExist:
                    if val['name'] == name and val['value'] == value:
                        Is = 1
                        break
                    else:
                        continue
                else:
                    if val['name'] == name and val['value'] == value:
                        Is = 0
                        break
                    else:
                        Is = 1
                        continue
        else:
            error_msg = "The browser did not save cookie."
            if IsExist:
                Is = 0
            else:
                Is = 1

        if Is != 1:
            if IsExist:
                error_msg += "{'name':'%s','value':'%s'} not be saved by the browser." % (name, value)
                logging.error(f"name为{name}，value为{value}的cookie不符合期望，不存在于浏览器中！！！")
            else:
                error_msg += "{'name':'%s','value':'%s'} still exists in the browser." % (name, value)
                logging.error(f"name为{name}，value为{value}的cookie不符合期望，存在于浏览器中！！！")
            self.fail(error_msg)
        else:
            if IsExist:
                logging.info(f"name为{name}，value为{value}的cookie符合期望，存在于浏览器中！！！----------断言成功！！")
            else:
                logging.info(f"name为{name}，value为{value}的cookie符合期望，不存在于浏览器中！！！----------断言成功！！")
