from openpyxl import Workbook
from random import *

wb = Workbook()
ws = wb.active

ws.append(["번호", "영어", "수학"])
for i in range(1, 11):
    ws.append([i, randint(0, 100), randint(0, 100)])

col_B = ws["B"]
# print(col_B)
for cell in col_B:
    print(cell.value, end=" ")

col_range = ws["B:C"]
for cols in col_range:
    for cell in cols:
        print(cell.value, end=" ")

row_title = ws[1]
for cell in row_title:
    print(cell.value, end=" ")

row_range = ws[2:6]
for rows in row_range:
    for cell in rows:
        print(cell.value, end=" ")
    print()

from openpyxl.utils.cell import coordinate_from_string

row_range = ws[2 : ws.max_row]
for rows in row_range:
    for cell in rows:
        print(cell.coordinate, end=" ")
        xy = coordinate_from_string(cell.coordinate)
        print(xy, end=" ")
        print(xy[0], end=" ")  # A
        print(xy[1], end=" ")  # 1
    print()

print(tuple(ws.rows))

print(tuple(ws.columns))

for row in tuple(ws.rows):
    print(row[2].value, end=" ")

wb.save("example.xlsx")
