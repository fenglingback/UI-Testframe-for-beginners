from Public.Common.father import driver
from Public.Pages.BasePage import basePage
from Data.Elements_and_Data import settle


class Settle(basePage, settle):

    def get_bought_product_msg(self) -> list:
        temp_list = []
        for i in range(len(self.products_name)):
            temp_dict = {'name': self.products_name[i].text, 'describe': self.products_describe[i].text, 'price': self.products_price[i].text}
            temp_list.append(temp_dict)
        print(temp_list)
        return temp_list

    def get_pay_msg(self):
        card = self.card.text
        kuaidi = self.kuaidi.text
        price_total = self.price_total.text
        tax_total = self.tax_total.text
        all_total = self.all_total.text
        msg = {'card': card, 'kuaidi': kuaidi, 'price_total': price_total, 'tax_total': tax_total, 'all_total': all_total}
        return msg

    def back_to_home(self):
        self.backhome.click()

    def settle_and_enter_to_finish_page(self):
        self.settle_btn.click()


mysettle = Settle(driver)
