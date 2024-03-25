import time

from Config.global_config import report_path


def makeReport():
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_name = report_path + "\\" + now + "report.html"
    return report_name
