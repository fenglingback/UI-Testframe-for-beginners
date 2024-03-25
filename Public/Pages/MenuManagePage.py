from time import sleep

from Data.Elements_and_Data import menu_manage
from Public.Common.father import driver
from Public.Pages.BasePage import basePage
from Public.Pages.LoginPage import login


class MenuManage(basePage, menu_manage):

    def enter_menuManage(self):
        """
        进入菜单管理界面
        """
        self.delete_all_cookies()
        login.login("test1002", "321321", "9876")
        sleep(0.5)
        self.system_manage_loc.click()
        self.menu_manage_loc.click()
        sleep(0.5)

    def open_all_menu(self):
        """
        展开所有菜单
        """
        for i in self.open_all_menu_buttons:
            if i.get_attribute('class') == 'el-table__expand-icon':
                i.click()

    def do_method(self, method):
        """
        :param method:要执行的操作
        :return:
        """
        if method == '确定添加' or method == '确定修改':
            self.sure_add_or_edit_button.click()
        elif method == '确定删除':
            self.sure_del_button.click()
        elif method == '取消添加' or method == '取消修改':
            self.cancel_add_or_edit_button.click()
        elif method == '取消删除':
            self.cancel_del_button.click()
        elif method == '关闭添加' or method == '关闭修改':
            self.close_add_or_edit_button.click()
        elif method == '关闭删除':
            self.close_del_button.click()

    '''
    ----------------------------------------------------------------------------------------------------------------
    '''

    def add_menu(self, F_or_C, open_or_close, father_menu, menu_name, menu_address):
        """
        添加菜单
        :param F_or_C:
        :param open_or_close:
        :param father_menu:
        :param menu_name:
        :param menu_address:
        :return:
        """
        self.add_menu_button.click()

        if F_or_C == '父菜单':
            self.father_or_child[0].click()
        elif F_or_C == '子菜单':
            self.father_or_child[1].click()

        if open_or_close == '启用':
            if 'rgb(19, 206, 102)' not in self.open_or_close_button_in_add.get_attribute('style'):
                self.open_or_close_button_in_add.click()
        elif open_or_close == '停用':
            if 'rgb(255, 73, 73)' not in self.open_or_close_button_in_add.get_attribute('style'):
                self.open_or_close_button_in_add.click()

        if F_or_C == '子菜单' and father_menu != '':
            self.chose_father_button.click()
            for i in self.father_chose_list:
                if father_menu == i.text:
                    i.click()

        self.menu_name_input.send_keys(menu_name)
        self.menu_address_input.send_keys(menu_address)

    '''
    ------------------------------------------------------------------------------------------------------------------
    '''

    def edit_menu(self, F_or_C, start_name, open_or_close, father_menu, end_name, end_address):
        """
        修改菜单
        :param F_or_C:
        :param start_name:
        :param open_or_close:
        :param father_menu:
        :param end_name:
        :param end_address:
        :return:
        """
        self.open_all_menu()
        for idx, value in enumerate(self.menu_tr):
            if start_name in value.text:
                self.edit_menu_buttons[idx].click()

        if open_or_close == '启用':
            if 'rgb(19, 206, 102)' not in self.open_or_close_button_in_edit.get_attribute('style'):
                self.open_or_close_button_in_edit.click()
        elif open_or_close == '停用':
            if 'rgb(255, 73, 73)' not in self.open_or_close_button_in_edit.get_attribute('style'):
                self.open_or_close_button_in_edit.click()

        if F_or_C == '子菜单' and father_menu != '':
            self.chose_father_button.click()
            for i in self.father_chose_list:
                if father_menu == i.text:
                    i.click()

        self.menu_name_input.send_keys(end_name)
        self.menu_address_input.send_keys(end_address)

    '''
    -----------------------------------------------------------------------------------------------------------------------
    '''

    def delete_menu(self, menu_name):
        """
        删除菜单
        :param menu_name:
        :return:
        """
        self.open_all_menu()
        for idx, value in enumerate(self.menu_tr):
            if menu_name in value.text:
                self.del_menu_buttons[idx].click()


menu = MenuManage(driver)
