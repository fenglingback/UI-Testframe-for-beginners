# 生成错误截图

from Config.global_config import error_screenshot_path
from Public.Common.CommonConfig import make_a_directory
from Public.Common.father import driver


class makeScreenShot:

    def __init__(self, mydriver, hook_func=None):
        self.driver = mydriver
        self.hook_func = hook_func

    def makeErrorPng(self, DirectoryName, PowerPoint, describe):
        """
        在ErrorScreenShot目录下生成功能模块的测试用例执行错误截图
        :param DirectoryName: 页面名称
        :param PowerPoint: 功能点名称
        :param describe: 错误描述
        :return:
        """
        last_path = make_a_directory(error_screenshot_path, DirectoryName, PowerPoint)
        return self.driver.save_screenshot(last_path + f'/{describe}.png')


err_img = makeScreenShot(driver)
