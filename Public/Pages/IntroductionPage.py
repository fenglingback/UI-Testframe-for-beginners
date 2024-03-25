from Public.Common.PowerPoint import PowerPoint
from Public.Common.father import driver
from Public.Pages.BasePage import basePage
from Data.Elements_and_Data import introduction


class Introduction(basePage, introduction):

    def get_product_msg(self) -> dict:
        pop = PowerPoint(self.introduction_loc, '商品详情')
        img_url = pop['商品图片'].get_attribute('src')
        name = pop['商品名称'].text
        describe = pop['商品描述'].text
        price = pop['商品价格'].text
        msg = {'name': name, 'img_url': img_url, 'describe': describe, 'price': price}
        return msg

    '''
    '''

    def back_to_home(self):
        self.introduction_loc['返回首页'].click()

    def add_to_car(self):
        self.introduction_loc['添加至购物车'].click()

    def remove_from_car(self):
        self.introduction_loc['从购物车移除'].click()


myintroduction = Introduction(driver)
