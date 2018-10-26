# -*- coding: utf-8 -*-
# Created by richie at 2018/10/26


import oct_requests


req = oct_requests.request('GET', 'https://httpbin.org/get')
print req.content


