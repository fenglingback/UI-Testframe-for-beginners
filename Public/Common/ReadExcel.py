import os
import xlrd
from Config.global_config import data_path


class readExcel:
    def __init__(self, filename, sheetname):
        path = os.path.join(data_path, filename)
        self.workbook = xlrd.open_workbook(path)
        self.table = self.workbook.sheet_by_name(sheetname)
        self.tablename = sheetname

    # 读取每一行的数据
    def read_excel_every_row(self):
        rows = self.table.nrows
        list = []
        for i in range(rows):
            if i != 0:
                row_value = self.table.row_values(i)
                # 在末尾插入表名和所在行数
                row_value.append(self.tablename)
                row_value.append(i + 1)
                list.append(row_value)
            i += 1
        return list

    # 读取每一列的数据
    def read_excel_every_col(self):
        cols = self.table.ncols
        list = []
        for i in range(cols):
            col_value = self.table.col_values(i)
            del col_value[0]
            # 在末尾插入表名和所在列数
            # col_value.append(self.tablename)
            # col_value.append(i + 1)
            list.append(col_value)
            i += 1
        return list

    # 读取指定行的数据
    def read_excel_by_row(self, row):
        list = []
        row_value = self.table.row_values(row - 1)
        # 在末尾插入表名和所在行数
        row_value.append(self.tablename)
        row_value.append(row)
        list.append(row_value)
        return list

    # 读取指定列的数据
    def read_excel_by_col(self, col):
        list = []
        col_value = self.table.col_values(col - 1)
        del col_value[0]
        # 在末尾插入表名和所在列数
        # col_value.append(self.tablename)
        # col_value.append(col)
        list.append(col_value)
        return list

    # 读取指定范围行的数据
    def read_excel_between_row(self, start_row, end_row):
        list = []
        for i in range(start_row - 1, end_row):
            row_value = self.table.row_values(i)
            # 在末尾插入表名和所在行数
            row_value.append(self.tablename)
            row_value.append(i + 1)
            list.append(row_value)
            i += 1
        return list

    # 读取指定范围列的数据
    def read_excel_between_col(self, start_col, end_col):
        list = []
        for i in range(start_col - 1, end_col):
            col_value = self.table.col_values(i)
            del col_value[0]
            # 在末尾插入表名和所在列数
            # col_value.append(self.tablename)
            # col_value.append(i + 1)
            list.append(col_value)
        return list

    # 读取指定范围单元格的数据
    def read_excel_between_cell(self, start_row, start_col, end_row, end_col):
        list = []
        for i in range(start_row - 1, end_row):
            for j in range(start_col - 1, end_col):
                value = self.table.cell_value(i, j)
                list.append(value)
        return list

# 测试程序
# if __name__ == '__main__':
#     print(readExcel('login.xlsx', "right").read_excel_every_row())
# print(readExcel('login.xlsx', "email").read_excel_every_col())
# print(readExcel('login.xlsx', "email").read_excel_by_row(2))
# print(readExcel('login.xlsx', "email").read_excel_by_col(2))
# print(readExcel('login.xlsx', "email").read_excel_between_row(2, 3))
#     print(readExcel('userManage.xlsx', "exist_or_not").read_excel_between_col(1, 2))
# print(readExcel('login.xlsx', "email").read_excel_between_cell(2,2,4,4))
