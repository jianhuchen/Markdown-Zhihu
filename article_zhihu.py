# -*- encoding: utf-8 -*-
'''
@File    :   article_zhihu.py
@Time    :   2020/03/12 13:55:27
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''

import re
import os.path as osp
import argparse

parser = argparse.ArgumentParser(usage="it's usage tip.", description="help info.")
parser.add_argument('--path', '-p', help='path of .md file', dest="path", required=True, type=str)
parser.add_argument('--output_path', '-o', help='path of output.', dest='output_path', type=str)
args = parser.parse_args()

path = str(args.path)
if not args.output_path:
    args.output_path = osp.join("output", f"zhihu_{path.split('/')[-1]}")
output_path = str(args.output_path)

with open(path, "r") as fp:
    content = fp.read()

content = re.sub(
    r"\$(.+?)\$",
    r'<img src="https://www.zhihu.com/equation\?tex=\1" alt="[公式]" eeimg="1" data-formula="\1">',
    content)

content = re.sub(
    r"\${2}([\w\W]+?)\${2}",
    r'\n<img src="https://www.zhihu.com/equation\?tex=\1\\\\" alt="[公式]" data-formula="\1\\\\" eeimg="1">\n',
    content)

with open(output_path, "w") as fp:
    content = fp.write(content)
    