import pandas as pd
import numpy as np

xls=pd.read_excel('./excel-comp-data.xlsx',sheetname=0)#sheetname是第几栏
#xls = pd.ExcelFile('./excel-comp-data.xlsx')
#xls.sheet_names#显示出读入excel文件中的表名字
#print(xls.sheet_names)
print(xls.head())
print("**************************************")
#增加一列 Jan Feb Mar的 求和
xls["total"] = xls["Jan"] + xls["Feb"] + xls["Mar"]
print(xls.head())