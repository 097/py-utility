#!/usr/bin/env python3
"""
Merge PDF files in a folder
"""

import os
import sys
import PyPDF2


def merge_pdfs(input_folder, output_file):
    # 获取文件夹中的所有PDF文件
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

    # 按文件名顺序排序PDF文件
    pdf_files.sort()

    # 创建一个PDF合并对象
    pdf_merger = PyPDF2.PdfMerger()

    # 逐个合并PDF文件
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        pdf_merger.append(pdf_path)

    # 将合并后的PDF写入输出文件
    with open(output_file, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f'Usage: python {os.path.basename(sys.argv[0])} input_folder output_file')
        sys.exit(1)

    input_folder = sys.argv[1]
    output_file = sys.argv[2]

    # 确定输出文件路径
    if not output_file.endswith('.pdf'):
        output_file = os.path.join(output_file, 'output.pdf')

    merge_pdfs(input_folder, output_file)

    print(f'write file to: {output_file}')
