
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

pdf = pdfplumber.open("demo/test.pdf")
page = pdf.pages[0]
table = page.extract_table()
df = pd.DataFrame(table)
df.to_excel("demo/test.xlsx", header=False, index=False)
