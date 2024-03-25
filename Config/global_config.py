import os.path

from Public.Common.ReadConfigini import ReadConfigIni

file_path = os.path.split(os.path.realpath(__file__))[0]
# print(file_path)

read_config = ReadConfigIni(os.path.join(file_path, "config.ini"))
# print(read_config)

project_path = read_config.getConfigValue("project", "project_path")
# print(project_path)

log_path = os.path.join(project_path, "Report", "Log")
# print(log_path)

last_log_path = os.path.join(log_path, "last")

report_path = os.path.join(project_path, "Report", "TestReport")
# print(report_path)

data_path = os.path.join(project_path, "Data")
# print(data_path)

testcase_path = os.path.join(project_path, "TestCase")
# print(testcase_path)

error_screenshot_path = os.path.join(project_path, "Report", "ErrorScreenShot")
# print(error_screenshot_path)

browser = read_config.getConfigValue("browser", "browser_name")
# print(browser)
