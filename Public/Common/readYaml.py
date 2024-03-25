from ruamel.yaml import YAML
import copy

class readYaml:

    def __init__(self, file_path):
        yaml = YAML(typ='safe')
        with open(file_path, encoding='utf-8') as file:
            self.data = yaml.load(file)

    def read_all_data(self):
        """
        返回读取的yaml文件的所有数据
        """
        return self.data

    def read_except_data_by_key(self, key, value) -> dict:
        data = copy.deepcopy(self.data)
        last_data = {}
        if isinstance(data, list):
            for idx, val in enumerate(data):
                if key in val:
                    if val[key] == value:
                        last_data = copy.deepcopy(val)
                        last_data.pop(key)
                    else:
                        continue
                else:
                    raise Exception("字典里没有这个key值的键值对！！")
        return last_data
