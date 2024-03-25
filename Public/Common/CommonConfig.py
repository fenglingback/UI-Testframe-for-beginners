import os
import time
from datetime import datetime


def getCurrentTime():
    format = "%a %b %d %H:%M:%S %Y"
    return datetime.now().strftime(format)


def CurrentTime_format_ymd():
    format = "%Y-%m-%d"
    return time.strftime(format)


def CurrentTime_format_all():
    format = "%Y_%m_%d~%H-%M-%S"
    return time.strftime(format)


def make_a_directory(path: str, *directory: str):
    """
    在path路径下创建目录
    :param path:
    :param directory:
    :return:
    """
    temp_path = path
    for i in directory:
        if i not in os.listdir(temp_path):
            temp_path += '/' + i
            os.mkdir(temp_path)
        else:
            temp_path += '/' + i
            continue
    return temp_path


def make_price_standard(alist: list) -> list:
    """
    使价格变得规范
    :param alist:
    :return:
    """
    dolla = "$"
    for i, v in enumerate(alist):
        v['price'] = dolla + str(v['price'])

    return alist
