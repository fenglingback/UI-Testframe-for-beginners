import os
from Config.global_config import last_log_path, log_path
from loguru import logger
from Public.Common.CommonConfig import CurrentTime_format_all
import zipfile


def makeLogFile(name):
    """
    :param name: log名(不用带.log)
    :return:
    """
    filename = os.path.join(last_log_path, '{0}.log'.format(name))
    logger.add(filename)
    return filename


# def get_All_log():
#     everything = os.listdir(log_path)
#     log_list = []
#     for idx, value in enumerate(everything):
#         path = os.path.join(log_path, value)
#         if os.path.isfile(path):
#             log_list.append(path)
#     return log_list


def Zip_LogDir(dir_path):
    """
    :param dir_path: 目录路径
    :return: zip包的路径
    """
    output_path = os.path.join(log_path, "last.zip")
    zip = zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dir_path):
        for log_name in filenames:
            zip.write(os.path.join(path, log_name), os.path.join('', log_name))
    zip.close()
    return output_path


def delete_zip_and_rename_last(file_name):
    """

    :param file_name: zip名
    :return:
    """
    zip_path = log_path + r"\\{0}".format(file_name)
    if os.path.exists(zip_path):
        os.remove(zip_path)
    if os.path.exists(last_log_path):
        new_path = log_path + r"\\{0}".format(CurrentTime_format_all())
        os.rename(last_log_path, new_path)
