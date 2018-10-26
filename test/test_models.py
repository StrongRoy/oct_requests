# -*- coding: utf-8 -*-
# Created by richie at 2018/10/25


import richie_httplib

data = {
        "key": "value1",
        "key1": "value1",
        "key2": "value1",
        "key3": "value1",
        "key4": "value1",
    }

req = richie_httplib.Request()
# req.prepare_body({'files': u'../upload_file/你好.pdf'},data)

req.prepare_headers({'User-Agent': 'Mozilla/5.0'})

print req.headers
