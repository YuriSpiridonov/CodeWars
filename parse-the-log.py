# https://www.codewars.com/kata/parse-the-log/train/python

#logparser=r'(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3})\s+(ERROR|INFO|DEBUG)\s+\[(\w+):(\w+):?(\w+)?\]\s+(.+)'

import re

regex=re.compile(r'''
(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3})   # date and time
\s+
(ERROR|INFO|DEBUG)                             # msg type
\s+
\[(\w+):(\w+):?(\w+)?\]                        # user and func and sub func he struggle
\s+
(.+)                                           # message
''', re.VERBOSE)

mo = regex.findall("2003-07-08 16:49:45,896 ERROR [user1:mainfunction:subfunction] We have a problem")
print(mo)
