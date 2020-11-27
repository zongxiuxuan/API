#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import xlrd
import xlwt

import Common.getDir
"""
利用xlrd ，xlwt模块操作ecxel表格
"""
proDir = Common.getDir.proDir


class PyExcel:
    """Use the given excel_name and sheet_name, sheet_value, write excel and read excel.
        1. write_excel
        2. read_excel
    """
    TestFile = os.path.join(proDir, "testFile", "case")
    suffix = ".xls"

    def __init__(self, excel_name, sheet_name=None, sheet_value=None):
        """
        initialization parameter
        :param excel_name: The file suffix must be "xls"
        :param sheet_name: set the workbook's sheetName
        :param sheet_value: The type of object must be "list" or "tuple"
        """
        self.excel_name = excel_name
        self.sheet_name = sheet_name
        self.sheet_value = sheet_value

        if not str(self.excel_name).endswith(self.suffix):
            raise Exception('%s suffix is not "%s"' %(self.excel_name, self.suffix))
        self.EXCEL_PATH = os.path.join(self.TestFile, self.excel_name)

# write excel file
    def write_excel(self):
        if self.sheet_name is not None:
            wb = xlwt.Workbook()
            sheet = wb.add_sheet(self.sheet_name)
            for i in range(len(self.sheet_value)):
                for j in range(len(self.sheet_value[i])):
                    sheet.write(i, j, self.sheet_value[i][j])

            wb.save(self.EXCEL_PATH)
            print("write date success!")
        else:
            return False

# read excel file
    def read_excel(self):
        workbook = xlrd.open_workbook(self.EXCEL_PATH)
        if self.sheet_name:
            work_sheet = workbook.sheet_by_name(self.sheet_name)
        else:
            work_sheet = workbook.sheet_by_index(0)

        for i in range(work_sheet.nrows):
            for j in range(work_sheet.ncols):
                print(work_sheet.cell_value(i, j))


# get excel value
def get_excel_value(excel_name, sheet_name):
    """
    get excel value by given excel_name and sheet_name
    :param excel_name:
    :param sheet_name:
    :return: cls
    """
    cls = []
    excel_path = os.path.join(proDir, "testFile", "case", excel_name)
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_name(sheet_name)
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls

# r  = get_excel_value("WebCase.xls", "login")
# print r
# if __name__ == "__main__":
#     # value = (
#     #     ["case_name", "username", "password"],
#     #     ["1", "qiutiandeyanjin@163.com", "efg"],
#     #     ["2", "qiutiandeyanjin@163.com", ""],
#     #     ["3", "", "efg", ]
#     # )
#     # excel = PyExcel(excel_name="WebCase.xls", sheet_name="write_test", sheet_value=value)
#     # excel.write_excel()
#     # excel.read_excel()
#     test = get_excel_value(excel_name="WebCase.xls", sheet_name="login")


if __name__ == '__main__':
    '''
     2 读取XLS,XLSX文件
     3 '''

def readExcelFile(filename = 'protest-原话记录.xlsx'):
    list = []
    workbook = xlrd.open_workbook(filename=filename)
    booksheet = workbook.sheet_by_index(0)
    for i in range(2):
        list.append("".join(booksheet.row_values(i)))
    return list
print(readExcelFile())