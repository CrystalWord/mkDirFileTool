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

l = ["笔记.md", "创建py文件.py", "计算代码量.py", "test.py"]
for i in l:
    with open('./%s/%s' % (t_now, i), 'ab') as f:
        if i == "笔记.md":
            f.write("# Python高级\n".encode())
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
    print(i + "创建成功！")    
    time.sleep(1)