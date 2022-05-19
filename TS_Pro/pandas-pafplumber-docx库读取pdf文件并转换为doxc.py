# _*_coding:utf-8_*_
# @Time:2022/5/17 16:47
# @Author:Young
# @File:pandas-pafplumber-docx库读取pdf文件并转换为doxc
import pandas as pd
import pdfplumber
import docx

path_pdf = "demo/workday.pdf"
with pdfplumber.open(path_pdf) as pdf:
    pages_total = len(pdf.pages)
    # print(type(pages_total)) # page_total返回的整型int
    print("pdf共："+str(pages_total)+"页")
    # cont = pdf.pages[0].extract_text() # 测试是否能获取到数据
    # print(cont)
    dc = docx.Document()
    for pages in pdf.pages:
        dc.add_paragraph(pages.extract_text())
    dc.save("demo/hetong.docx")

