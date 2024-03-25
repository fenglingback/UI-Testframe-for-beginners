from time import sleep

from Public.Common.father import driver
from Public.Pages.BasePage import basePage
from Data.Elements_and_Data import login


class Login(basePage, login):

    # 输入name、password
    def input_str(self, name, password):
        # self.switch_to_frame(self.frame_name)
        self.name_loc.send_keys(name)
        self.password_loc.send_keys(password)

    # 打开登录页
    def open_login_url(self):
        self.open(self.login_url)

    # 点击登录按钮
    def click_login_button(self):
        self.login_button_loc.click()

    def set_long_cookies(self):
        cookie = self.get_cookie('session-username')
        self.delete_cookie('session-username')
        if cookie['value'] == 'standard_user':
            self.add_cookie({'name': 'session-username', 'value': 'standard_user', 'expiry': 1716783170})
        elif cookie['value'] == 'problem_user':
            self.add_cookie({'name': 'session-username', 'value': 'problem_user', 'expiry': 1716783170})

    # 登录操作
    def login(self, name, password, isSetLong: bool = False):
        self.open_login_url()
        self.input_str(name, password)
        sleep(0.5)
        self.click_login_button()
        sleep(0.5)
        if isSetLong:
            self.set_long_cookies()


mylogin = Login(driver)
