# -*- coding: utf-8 -*-
# Created by richie at 2018/10/25


import oct_requests

s = oct_requests.Session()

data = {
    "key": "123",
    "key2": "123",
}


url = 'http:127.0.0.1/uploadfile'
preq = s.request("post", url, data=data,
                 files={
                     'files': u'/Users/username/upload_file/test.pdf',
                 }
                 )
print preq.content
