from Public.Common.father import driver
from Public.Pages.BasePage import basePage
from Data.Elements_and_Data import shopcart


class ShopCart(basePage, shopcart):

    def enter_shopcart(self):
        self.shopcart_num.click()

    def get_shopcart_product_msg(self) -> list:
        temp_list = []
        for i in range(len(self.name)):
            temp_dict = {'name': self.name[i].text, 'describe': self.describe[i].text, 'price': self.price[i].text}
            temp_list.append(temp_dict)

        return temp_list

    def remove_from_car(self, index):
        self.remove_bt[index].click()

    def back_to_home(self):
        self.backhome.click()

    def enter_information_page(self):
        self.nextpage.click()


myshopcart = ShopCart(driver)
