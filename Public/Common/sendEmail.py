import os
from XTestRunner import SMTP

from Config.global_config import last_log_path
from Public.Common.MyLog import Zip_LogDir


class EmailManage:

    def sendMail(self, receiver, subject, report_name, isSendLog: bool = False):
        """

        :param receiver: 收件人
        :param subject: 工程名
        :param report_name:
        :param isSendLog: 是否发送日志
        :return:
        """
        smtpserver = "smtp.qq.com"

        username = "2360238123@qq.com"
        password = "kssbzyedkpcrebhf"

        smtp = SMTP(user=username, password=password, host=smtpserver)
        smtp.sender(to=receiver, subject=subject, attachments=report_name)
        if isSendLog:
            zip_path = Zip_LogDir(last_log_path)
            smtp.sender(to=receiver, subject=subject, attachments=zip_path)

    def return_last_report(self, report_dir):
        list = os.listdir(report_dir)
        list1 = sorted(list)
        report_last = os.path.join(report_dir, list1[-1])
        print(report_last)
        return report_last
