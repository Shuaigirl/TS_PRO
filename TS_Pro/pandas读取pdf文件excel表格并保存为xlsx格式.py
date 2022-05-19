
'''
需安装的库
pip install tabula -i https://pypi.douban.com/simple
pip install pdfplumber -i https://pypi.douban.com/simple
pip install openpyxl -i https://pypi.douban.com/simple
'''

# import tabula
# tables = tabula.read_pdf('demo/test.pdf')
#
# print(tables)
#
# tables.to_csv('demo/test.csv')

import pandas as pd
import pdfplumber
from datetime import datetime
# pd.options.display.max_columns = 777
pdf = pdfplumber.open("demo/test.pdf")
page = pdf.pages[0]
table = page.extract_table()
df = pd.DataFrame((table)[3:],columns=["VESSEL","SVC-CODE","NINGBO-ARRIVES","NINGBO-DEPARTS","SHANGHAI-ARRIVES","SHANGHAI-DEPARTS","OAKLAND-ARRIVES","OAKLAND-DEPARTS","LONGBEACH-ARRIVES","LONGBEACH-DEPARTS","HONOLULU-ARRIVES","HONOLULU-DEPARTS","GUAM-ARRIVES","GUAM-DEPARTS"])
#获取第三列的第一个时间格式
# print(df["NINGBO-ARRIVES"].values[0])
# print(len(df["NINGBO-ARRIVES"]))
#时间格式转换
now = datetime.now()
suffix = f'{now.year:04d}'
# for i in df["NINGBO-ARRIVES"]:
#     if i == "/":
#         i = "-"
#     else:
#         i = i+"-"+suffix
#         # print(i,type(i))
#         i =datetime.strptime(i, '%d-%b-%Y')
#         i = str(i)
#         if k < len(df["NINGBO-ARRIVES"]):
#             df["NINGBO-ARRIVES"].values[k] = i
#     k=k+1
# print(df["NINGBO-ARRIVES"])
for j in df.columns[2:]:
    k = 0
    for i in df[j]:
        if i == "/":
            i = "-"
        else:
            now = datetime.now()
            suffix = f'{now.year:04d}'
            i = i + "-" + suffix
            # i = i.map(lambda x: datetime.strptime(x, "%d-%b-%Y"))
            i = datetime.strptime(i, '%d-%b-%Y',)
            i = str(i).split(" ")[0]
            if k < len(df[j]):
                df[j].values[k] = i
        k = k+1
print(df)

df.to_excel("demo/test.xlsx", index=False)

