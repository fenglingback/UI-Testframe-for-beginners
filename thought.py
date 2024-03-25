import os

from ruamel.yaml import YAML

from Config.global_config import data_path
from Public.Common.readYaml import readYaml


class learn:

    @staticmethod
    def my_1(**kwargs):
        """
        展示next(iter(kwargs.items()))的用法
        :param kwargs:
        :return:
        """

        k, v = next(iter(kwargs.items()))
        print(k)
        print(v)

    @staticmethod
    def my_2(path):
        """

        :param path:
        :return:
        """
        yaml = YAML(typ='safe')
        with open(path, encoding='utf-8') as file:
            data = yaml.load(file)
        print(f"data:\n{data}")

    @staticmethod
    def my_3():
        product_filepath = os.path.join(data_path, "products.yml")
        r1 = readYaml(product_filepath)
        product_data = r1.read_except_data_by_key('name', 'Sauce Labs Bike Light')
        # xx = sorted(product_data, key=lambda x: x['price'], reverse=True)
        print(product_data)

    @staticmethod
    def my_4():
        hh = {
            'Y': {
                'y': test_item()
            }
        }
        print(hh['Y']['y'][1])



class test_item(object):
    """
    类比Elements类
    """

    def __init__(self):
        self.it_1 = ['a', 'b']

    def __getitem__(self, item):
        return self.it_1[item]


class jicheng:
    """
    类比元素类
    """
    hh = {
        'Y': {
            'y': test_item()
        }
    }


class xxxxx(jicheng):
    """
    类比page层的类
    """

    def xx(self):
        print(self.hh['Y']['y'][1])


whj = learn()
# whj.my_1(xpath="sdajf")
# whj.my_2('C:/Users/WHJ/Desktop/TestFrame/Data/products.yml')
whj.my_3()
# xxxxx().xx()
