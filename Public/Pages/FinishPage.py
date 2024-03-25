from Public.Common.father import driver
from Public.Pages.BasePage import basePage
from Data.Elements_and_Data import finish


class Finish(basePage, finish):

    def get_finish_msg(self):
        return self.finish_msg.text

    def back_to_home(self):
        self.backhome.click()


myfinish = Finish(driver)
