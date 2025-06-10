from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "My Sheet"
wb.save("example.xlsx")
wb.close()

