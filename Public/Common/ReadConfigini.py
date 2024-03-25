import configparser


class ReadConfigIni:
    def __init__(self, filename):
        self.cf = configparser.ConfigParser()
        # // 读取ini文件
        self.cf.read(filename)

    def getConfigValue(self, section, name):
        value = self.cf.get(section, name)
        return value
