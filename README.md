# Oct_requests
October based on the Requests package to use the generator to achieve large file transfer

# Installation oct_requests
```commandline
pip install git+https://github.com/StrongRoy/oct_requests.git
```

# Send get request
```python
import oct_requests
req = oct_requests.request('GET', 'https://httpbin.org/get')
print req.content
```

# Send post request 

```python
import oct_requests

s = oct_requests.Session()

data = {
    "key": "123",
    "key2": "123",
}


url = 'http:127.0.0.1/uploadfile'
preq = s.request("post", url, data=data,
                 files={'files': u'/Users/username/upload_file/test.pdf'})
print preq.content

```

# Multiple file transfer

```python
import oct_requests

s = oct_requests.Session()



url = 'http:127.0.0.1/uploadfile'
preq = s.request("post", url, files={'files1': u'/Users/username/upload_file/test1.pdf',
                                     'files2': u'/Users/username/upload_file/test2.pdf'})
print preq.content

```
