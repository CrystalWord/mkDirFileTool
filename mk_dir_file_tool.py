#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import os
import time

t_now = str(datetime.date.today())
try:
    os.mkdir(t_now)
except:
    pass


def mk_md_file():
    with open('./%s/%s.md' % (t_now, file_name), 'wb') as f:
        f.write("# Web应用开发技术\n".encode())
        f.close


def mk_py_file():
    with open('./%s/%s.py' % (t_now, file_name), 'wb') as f:
        f.write("#!/usr/bin/python3\n\
# -*- coding: utf-8 -*-\n\n\
".encode())
        f.close()   

def mk_html_file():
    with open('./%s/%s.html' % (t_now, file_name), 'wb') as f:
        f.write('<!DOCTYPE html>\n\
<html>\n\
    <head>\n\
        <meta charset="utf-8">\n\
        <meta name="viewport" content="width=device-width, initial-scale=1.0">\n\
        <title></title>\n\
    </head>\n\
    <body>\n\
        <div>\n\n\
        </div>\n\
    </body>\n\
</html>\
'.encode())
        f.close()   

l = ["笔记.md", "创建py文件.py", "计算代码量.py", "test.py", "test.html"]
for i in l:
    with open('./%s/%s' % (t_now, i), 'ab') as f:
        if i == "笔记.md":
            f.write("# Web应用开发技术\n".encode())
            f.close
        elif i == "创建py文件.py":
            f.write("#!/usr/bin/python3\n\
# -*- coding: utf-8 -*-\n\n\
import os\n\n\
while True:\n\
    name = input('请输入文件名：')\n\
    with open('./%s.py' % name, 'ab') as f:\n\
        f.write('#!/usr/bin/python3\\n# -*- coding: utf-8 -*-\\n\\n'.encode())\n\
        f.close()\
".encode())
            f.close()   
        elif i == "计算代码量.py":
            f.write("#!/usr/bin/python3\n\
# -*- coding: utf-8 -*-\n\n\
import os\n\n\
while True:\n\
    file_type = input('请需要统计文件类型的后缀名：')\n\
    file_type = '.' + file_type\n\
    print(file_type)\n\
    s = 0\n\
    for root, dirs, files in os.walk('./'):\n\
        for i in files:\n\
            if i[-3:].lower() == file_type:\n\
                try:\n\
                    with open(i, 'rb') as f:\n\
                        a = f.read()\n\
                        s += len(a.splitlines())\n\
                    f.close()\n\
                except:\n\
                    pass\n\
    if file_type == '.py':\n\
        s -= (24 + 10)\n\n\
    print('今日代码量：%s行' % s)".encode())
            f.close()
        elif i == "test.py": 
            f.write("#!/usr/bin/python3\n\
# -*- coding: utf-8 -*-\n\n\
".encode())
            f.close() 
        elif i == "test.html":
            f.write('<!DOCTYPE html>\n\
<html>\n\
    <head>\n\
        <meta charset="utf-8">\n\
        <meta name="viewport" content="width=device-width, initial-scale=1.0">\n\
        <title></title>\n\
    </head>\n\
    <body>\n\
        <div>\n\n\
        </div>\n\
    </body>\n\
</html>\
'.encode())
            f.close()   

    print("文件%s创建成功!" % i)  
    time.sleep(1)

while True:
    file_name = input("请输入文件名：")
    file_type = input("请输入文件类型：")
    if file_type == 'md':
        mk_md_file()
    elif file_type == 'py':
        mk_py_file()
    elif file_type == 'html':
        mk_html_file()