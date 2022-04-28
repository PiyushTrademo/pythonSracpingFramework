import pandas as pd
import pytest
import xlrd

from Config.Config import TestData
from Pages.SCAC_Code import ScacCode
from TestCases.test_BaseTest import BaseTest

"""File to scrap the SCAC data"""


class Test_GetScacCompName(BaseTest):

    def test_get_name1(self):
        self.getscac = ScacCode(self.driver)
        self.get_data_from_xl("/Users/nikitasaxena/PycharmProjects/POM_Modle/TestCases/XlData/scac_codes_11.xlsx",
                              "write_file11.xlsx")

    def test_get_name2(self):
        self.getscac = ScacCode(self.driver)
        self.get_data_from_xl("/Users/nikitasaxena/PycharmProjects/POM_Modle/TestCases/XlData/scac_codes_2.xlsx",
                              "write_file22.xlsx")

    def test_get_name3(self):
        self.getscac = ScacCode(self.driver)
        self.get_data_from_xl("/Users/nikitasaxena/PycharmProjects/POM_Modle/TestCases/XlData/scac_codes_3.xlsx",
                              "write_file33.xlsx")

    def test_get_name4(self):
        self.getscac = ScacCode(self.driver)
        self.get_data_from_xl("/Users/nikitasaxena/PycharmProjects/POM_Modle/TestCases/XlData/scac_codes_4.xlsx",
                              "write_file44.xlsx")

    def get_data_from_xl(self, file_loacation, write_file_name):
        workbook = xlrd.open_workbook(file_loacation)
        sheet = workbook.sheet_by_name("Sheet1")

        """Get the row count"""
        row_count = sheet.nrows
        col_count = sheet.ncols
        scac_comp_list = []
        for curr_row in range(1, row_count):
            scac = sheet.cell_value(curr_row, 0)
            company_name = self.getscac.click_input(scac)
            self.write_excel_1(scac_comp_list, scac, company_name, write_file_name)

    def write_excel_1(self, scac_comp_list, scac, comp_name, file_name):
        scac_comp_list.append([scac, comp_name])
        df = pd.DataFrame(scac_comp_list, columns=['SCAC Code', 'Company Name'])
        df.to_excel(file_name)

