from Public.Common.father import driver
from Public.Pages.BasePage import basePage
from Data.Elements_and_Data import information


class Information(basePage, information):

    def input_personal_msg(self, f_name, l_name, postal_code):
        self.information_loc['first_name'].send_keys(f_name)
        self.information_loc['last_name'].send_keys(l_name)
        self.information_loc['postal_code'].send_keys(postal_code)

    def back_to_shopcar(self):
        self.information_loc['cancel'].click()

    def enter_to_settle_page(self):
        self.information_loc['continue'].click()


myinformation = Information(driver)
