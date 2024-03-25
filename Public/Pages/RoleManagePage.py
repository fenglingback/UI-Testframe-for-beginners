from time import sleep

from Data.Elements_and_Data import role_manage
from Public.Common.father import driver
from Public.Pages.BasePage import basePage
from Public.Pages.LoginPage import login


class RoleManage(basePage, role_manage):

    def enter_roleManage(self):
        """
        进入菜单管理界面
        :return:
        """
        self.delete_all_cookies()
        login.login("test1002", "321321", "9876")
        sleep(0.5)
        self.system_manage_loc.click()
        self.role_manage_loc.click()
        sleep(0.5)

    '''
    ------------------------------------------------------------------------------------------------------------------------------
    '''

    def do_method(self, method):
        """
        进行的操作
        :param method:
        :return:
        """
        if method == '确定添加':
            self.sure_add_button.click()
        elif method == '取消添加':
            self.cancel_add_button.click()
        elif method == '关闭添加':
            self.close_add_button.click()
        elif method == '确定删除':
            self.sure_del_button.click()
        elif method == '取消删除':
            self.cancel_del_button.click()
        elif method == '关闭删除':
            self.close_del_button.click()

    '''
    ------------------------------------------------------------------------------------------------------------------------------
    '''

    def clear_chosen(self):
        for i in self.role_checkbox:
            if i.is_selected():
                i.click()

    '''
    ------------------------------------------------------------------------------------------------------------------------------
    '''

    def add_role(self, role_name, power_level, open_or_close):
        """
        添加角色
        :param role_name: 角色名称
        :param power_level: 权限等级
        :param open_or_close: 角色的停启用
        :return:
        """
        self.add_role_button.click()
        sleep(0.5)
        self.role_name_input.send_keys(role_name)
        self.power_level_input.send_keys(power_level)
        sleep(0.5)
        if open_or_close == '启用':
            if 'rgb(19, 206, 102)' not in self.open_or_close_button.get_attribute('style'):
                self.open_or_close_button.click()
        elif open_or_close == '停用':
            if 'rgb(255, 73, 73)' not in self.open_or_close_button.get_attribute('style'):
                self.open_or_close_button.click()

    '''
    -----------------------------------------------------------------------------------------------------------------
    '''

    def edit_role(self, start_name, end_name, method):
        """
        修改角色
        :param start_name:
        :param end_name:
        :param method:
        :return:
        """
        for idx, value in enumerate(self.role_names):
            if start_name == value.text:
                self.edit_and_sure_button[idx].click()
                sleep(0.5)
                self.edit_name_input.select_all()
                self.edit_name_input.send_keys(end_name)
                if method == '确定修改':
                    sleep(0.5)
                    self.edit_and_sure_button[idx].click()

    '''
    -------------------------------------------------------------------------------------------------------------------------------
    '''

    def del_role(self, role_name_list: list) -> list:
        self.clear_chosen()
        del_message_list = []
        for idx, value in enumerate(self.role_names):
            if value.text in role_name_list:
                self.role_checkbox[idx].click()
                message = self.role_tr[idx].text
                message = message.splitlines()
                del_message_list.append(message)
                sleep(0.5)

        self.del_role_button.click()
        return del_message_list


role = RoleManage(driver)
