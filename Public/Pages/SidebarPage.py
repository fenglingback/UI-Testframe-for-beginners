from time import sleep

from Public.Common.father import driver
from Public.Pages.BasePage import basePage
from Data.Elements_and_Data import sidebar


class SideBar(basePage, sidebar):

    def control_sidebar(self, ctrl):

        if ctrl == 'open':
            self.sidebar_location['打开侧边栏按钮'].click()
        elif ctrl == 'close':
            self.sidebar_location['关闭侧边栏按钮'].click()

    def click_AllItems(self):
        self.sidebar_location['All Items'].click()

    def click_About(self):
        self.sidebar_location['About'].click()

    def click_Logout(self):
        self.sidebar_location['Logout'].click()

    def click_Reset(self):
        self.sidebar_location['Reset App State'].click()


mysidebar = SideBar(driver)
