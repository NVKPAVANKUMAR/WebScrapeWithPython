import xlrd, xlwt
import unittest
import HtmlTestRunner


class TestExcelHandle(unittest.TestCase):

    def test_ExcelReader(self):
        workbook = xlrd.open_workbook("dataEngine.xlsx")
        worksheet = workbook.sheet_by_index(0)
        print()
        for i in range(worksheet.nrows):
            print(worksheet.row_values(i))

    def test_ExcelWriter(self):
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet("Pysheet1")
        cols = ["A", "B", "C", "D", "E"]
        txt = "Row %s,Col %s"
        for num in range(5):
            row = sheet1.row(num)
            for index, col in enumerate(cols):
                value = txt % (num + 1, col)
                row.write(index, value)
        workbook.save("dataEngine.xlsx")

    def test_sheetMetrics(self):
        workbook = xlrd.open_workbook("dataEngine.xlsx")
        worksheet = workbook.sheet_by_index(0)
        print(worksheet.row_values(1))
        print(worksheet.col_values(1))
        print(worksheet.nrows)
        print(worksheet.ncols)
        print(worksheet.cell(0, 0).value)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="example_dir"))
