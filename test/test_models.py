# -*- coding: utf-8 -*-
# Created by richie at 2018/10/25


import oct_requests

data = {
        "key": "value1",
        "key1": "value1",
        "key2": "value1",
        "key3": "value1",
        "key4": "value1",
    }

req = oct_requests.Request()

print req.headers
