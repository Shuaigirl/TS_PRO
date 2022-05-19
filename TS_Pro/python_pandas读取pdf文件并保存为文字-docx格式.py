# _*_coding:utf-8_*_
# @Time:2022/4/27 14:19
# @Author:Young
# @File:python_pandas读取pdf文件
import pdfplumber
import pandas as pd
import csv
'''
.extract_text() 用来提页面中的文本，将页面的所有字符对象整理为的那个字符串
.extract_words() 返回的是所有的单词及其相关信息
.extract_tables() 提取页面的表格
.to_image() 用于可视化调试时，返回PageImage类的一个实例

'''
# with pdfplumber.open("demo/api4.pdf") as pdf:
#     page = pdf.pages[0]  # 第一页的信息
#     # print(type(page))  # <class 'pdfplumber.page.Page'>
#     text = page.extract_text()  #获取第一页的内容
#
import pdfplumber
import docx
text_path = "demo/api4.pdf"

with pdfplumber.open(text_path) as pdf:
    print(pdf.pages)#获取pdf文档所有的页，类型是dict
    total_pages = len(pdf.pages)
    print("total_pages: ",total_pages)

    # page = pdf.pages[0]  #获取第一页
    # print(type(page))  #<class 'pdfplumber.page.Page'>
    # # print(page.extract_text())  #获取第一页的内容

    #读取pdf全文
    # content = ""
    # for i in range(0, total_pages):
    #     # page=
    #     content += pdf.pages[i].extract_text()
    #     # print(page.extract_text())
    #     # print(page.extract_tables())
    #     print(content)
    # 保存为文本格式
    # with open("demo/api4.txt","a", encoding="utf-8") as fp:
    #     fp.write(content)
    # fp.close()

    #  保存为文docx格式，需安装python-docx库：pip install python-docx -i https://pypi.douban.com/simple
    dc = docx.Document()
    for page in pdf.pages:
        dc.add_paragraph(page.extract_text())
    dc.save("demo/api4.docx")
