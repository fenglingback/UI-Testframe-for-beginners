import os

from Config.global_config import data_path
from Public.Common.ReadExcel import readExcel
from Public.Common.readYaml import readYaml
from Public.Pages.BasePage import basePage

from poium import Element, Elements


class login:
    #  测试数据文件
    data_file = "login.xlsx"

    # 页面错误截图文件夹名
    folder_name = "登录页"
    powerpoint = ['登录']

    # 涉及网址列表
    login_url = "https://www.saucedemo.com/"

    # 页面元素
    loc = readExcel(basePage.element_file, "login").read_excel_by_col(1)[0]
    name_loc = Element(xpath=loc[0], describe="用户名输入框")
    password_loc = Element(xpath=loc[1], describe="密码输入框")
    login_button_loc = Element(xpath=loc[2], describe="登录按钮")
    # loginOut_button_loc = Element(xpath=loc[3], describe="登出按钮")

    # 测试数据
    right = readExcel(data_file, "user").read_excel_every_row()
    fail = readExcel(data_file, "fail").read_excel_every_row()


'''
------------------------------------------------------------------------------------------------------------------------------------------
'''


class sidebar:
    # 页面错误截图文件夹名
    folder_name = "侧边栏错误截图"
    powerpoint = ['侧边栏开关', '点击AllItem', '点击About', '点击Reset', '点击Logout']

    # 涉及网址列表
    home_url = "https://www.saucedemo.com/inventory.html"
    login_url = "https://www.saucedemo.com/"
    about_url = "https://saucelabs.com/"

    loc = readExcel(basePage.element_file, 'sidebar').read_excel_by_col(1)[0]

    sidebar_location = {
        '打开侧边栏按钮': Element(xpath=loc[0]),
        '关闭侧边栏按钮': Element(xpath=loc[1]),
        'All Items': Element(xpath=loc[2]),
        'About': Element(xpath=loc[3]),
        'Logout': Element(xpath=loc[4]),
        'Reset App State': Element(xpath=loc[5]),
        '侧边栏': Element(xpath=loc[6])
    }


class home:
    # 测试数据文件
    # filename = "serverManage.xlsx"

    # 页面错误截图文件夹名
    folder_name = "首页错误截图"

    # 元素定位
    loc = readExcel(basePage.element_file, 'home').read_excel_by_col(1)[0]

    range_loc = Element(xpath=loc[0], describe="排序选择框")
    name_a = Elements(xpath=loc[1], describe="名称处商品链接")
    img_a = Elements(xpath=loc[2], describe="图片处商品链接")
    img = Elements(xpath=loc[3], describe="商品图片")
    name = Elements(xpath=loc[4], describe="商品名称")
    describe = Elements(xpath=loc[5], describe="商品描述")
    price = Elements(xpath=loc[6], describe="商品价格")
    add_and_remove_button = Elements(xpath=loc[7], describe="添加||移除购物车按钮")

    product_filepath = os.path.join(data_path, "products.yml")
    product_readyaml = readYaml(product_filepath)
    product_data = product_readyaml.read_all_data()


class introduction:
    # 测试数据文件
    # filename = "serverManage.xlsx"

    # 页面错误截图文件夹名
    folder_name = "商品详情页错误截图"

    # 元素定位
    loc = readExcel(basePage.element_file, 'introduction').read_excel_by_col(1)[0]

    introduction_loc = {
        '商品详情': {
            '商品图片': Element(xpath=loc[0]),
            '商品名称': Element(xpath=loc[1]),
            '商品描述': Element(xpath=loc[2]),
            '商品价格': Element(xpath=loc[3])
        },
        '返回首页': Element(xpath=loc[4]),
        '添加至购物车': Element(xpath=loc[5]),
        '从购物车移除': Element(xpath=loc[6])
    }


class shopcart:
    # 测试数据文件
    # filename = "serverManage.xlsx"

    # 涉及网址列表
    shopcart_url = "https://www.saucedemo.com/cart.html"

    # 页面错误截图文件夹名
    folder_name = "购物车错误截图"

    # 元素定位
    loc = readExcel(basePage.element_file, 'shopcart').read_excel_by_col(1)[0]

    name = Elements(xpath=loc[0])
    describe = Elements(xpath=loc[1])
    price = Elements(xpath=loc[2])

    remove_bt = Elements(xpath=loc[3])
    backhome = Element(xpath=loc[4])
    nextpage = Element(xpath=loc[5])
    shopcart_num = Element(xpath=loc[6])
#
#
# class information:
#     # 测试数据文件
#     # filename = "serverManage.xlsx"
#
#     # 页面错误截图文件夹名
#     folder_name = "个人信息页错误截图"
#
#     # 元素定位
#     loc = readExcel(basePage.element_file, 'information').read_excel_by_col(1)[0]
#
#     information_loc = {
#         'first_name': Element(xpath=loc[0]),
#         'last_name': Element(xpath=loc[1]),
#         'postal_code': Element(xpath=loc[2]),
#         'cancel': Element(xpath=loc[3]),
#         'continue': Element(xpath=loc[4])
#     }
#
#
# class settle:
#     # 测试数据文件
#     # filename = "serverManage.xlsx"
#
#     # 页面错误截图文件夹名
#     folder_name = "结算页错误截图"
#
#     # 元素定位
#     loc = readExcel(basePage.element_file, 'settle').read_excel_by_col(1)[0]
#
#     products_name = Elements(xpath=loc[0])
#     products_describe = Elements(xpath=loc[1])
#     products_price = Elements(xpath=loc[2])
#
#     card = Element()
#     kuaidi = Element()
#     price_total = Element()
#     tax_total = Element()
#     all_total = Element()
#
#     backhome = Element()
#     settle_btn = Element()
#
#
# class finish:
#     # 测试数据文件
#     # filename = "serverManage.xlsx"
#
#     # 页面错误截图文件夹名
#     folder_name = "完成页错误截图"
#
#     # 元素定位
#     loc = readExcel(basePage.element_file, 'finish').read_excel_by_col(1)[0]
#
#     finish_msg = Element(xpath=loc[0])
#     backhome = Element(xpath=loc[1])
#
#
# class bottom:
#     # 测试数据文件
#     # filename = "serverManage.xlsx"
#
#     # 页面错误截图文件夹名
#     folder_name = "联系我们错误截图"
#
#     # 元素定位
#     loc = readExcel(basePage.element_file, 'bottom').read_excel_by_col(1)[0]
#
#     twitter_a = Element(xpath=loc[0])
#     facebook_a = Element(xpath=loc[1])
#     linkedin_a = Element(xpath=loc[2])
