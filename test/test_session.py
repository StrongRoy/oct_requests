# -*- coding: utf-8 -*-
# Created by richie at 2018/10/25


import richie_httplib

s = richie_httplib.Session()

data = {
    "conversion": "1",
    "key": "toEq2v6A0Ym549U1",
    "serial": "108692010",
}


url = 'http://global.talk-cloud.net/WebAPI/uploadfile'
preq = s.request("post", url, data=data,
                 files={'files': u'/Users/richie/PycharmProjects/richie_test_project/talk_cloud/upload_file/test.pdf'})
print preq.content
