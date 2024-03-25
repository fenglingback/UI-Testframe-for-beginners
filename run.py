import unittest
from loguru import logger
from XTestRunner import HTMLTestRunner
from rich import print as r_print
from Config import global_config
from Public.Common.MyLog import delete_zip_and_rename_last
from Public.Common.father import driver

from Public.Common.makeHtmlReport import makeReport
from Public.Common.sendEmail import EmailManage

report_path = global_config.report_path

TestCase_path = global_config.testcase_path

# # 根据测试用例书写的顺序来执行
# class MyTestLoader(unittest.TestLoader):
#     def getTestCaseNames(self, testcase_class):
#         test_names = super().getTestCaseNames(testcase_class)
#         testcase_methods = list(test_names.__dict__.keys())
#         test_names.sort(Key=testcase_methods.index)
#         return test_names


if __name__ == "__main__":
    bz = r'''
        
  ______ ___   ___  _______  __      
 /      |\  \ /  / |   ____||  |     
|  ,----' \  V  /  |  |__   |  |     
|  |       >   <   |   __|  |  |     
|  `----. /  .  \  |  |     |  `----.
 \______|/__/ \__\ |__|     |_______|
                                     

         '''
    r_print(f'[red]{bz}[/red]')
    delete_zip_and_rename_last("last.zip")
    discover = unittest.defaultTestLoader.discover(TestCase_path, pattern="Test*.py", top_level_dir=None)
    report = makeReport()
    with open(report, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title="自动化测试报告", tester='cxfl',
                                description=['类型：selenium', '操作系统：windows', '浏览器：Chrome'], language="zh-CN")
        runner.run(discover)

    fp.close()
    # logger.stop()
    EM = EmailManage()
    report = EM.return_last_report(report_path)
    EM.sendMail("2360238123@qq.com", "测试邮件", report, isSendLog=False)
    driver.quit()
