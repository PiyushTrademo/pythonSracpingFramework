import pytest
import xlrd
import openpyxl
from openpyxl import load_workbook

from Config.Config import TestData
from Pages.SCAC_Code import ScacCode
from TestCases.test_BaseTest import BaseTest


class Test_GetScacCompName(BaseTest):
    def test_get_name(self):
        self.getscac = ScacCode(self.driver)
        self.get_data_from_xl("/Users/nikitasaxena/PycharmProjects/POM_Modle/TestCases/XlData/carrier_codes.xlsx")
        #self.getscac.click_input(TestData.SCAC_Code)

    def get_data_from_xl(self, file_loacation):
        workbook = xlrd.open_workbook(file_loacation)
        sheet = workbook.sheet_by_name("Carrier Code List")

        """Get the row count"""
        row_count = sheet.nrows
        col_count = sheet.ncols

        for curr_row in range(1, row_count):
            scac = sheet.cell_value(curr_row, 0)
            company_name = self.getscac.click_input(scac)
            print(company_name)

    # def write_data_into_xl(self,file_location):
    #     wrkb = load_workbook("/Users/nikitasaxena/PycharmProjects/POM_Modle/TestCases/XlData/write_carrier_codes.xlsx")
    #