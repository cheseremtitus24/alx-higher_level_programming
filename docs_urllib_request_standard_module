# Python3- Using urllib to process web requests
Methods to Read in Header key:value pairs.
with urlopen("https://www.example.com") as response:
...     pass

headers = response.headers
print(headers.get('X-Request-Id'))
headers['X-Request-Id'];

header_method2 = response.getheader('X-Request-Id')

# Decoding
character_set = response.headers.get_content_charset()
decoded_body = body.decode(character_set)

# Writing to Files as String
```
>>> from urllib.request import urlopen
>>> with urlopen("https://www.google.com") as response:
...     body = response.read()
...
>>> character_set = response.headers.get_content_charset()
>>> character_set
'ISO-8859-1'
>>> content = body.decode(character_set)
>>> with open("google.html", encoding="utf-8", mode="w") as file:
...     file.write(content)

```
# Handling Urllib req. Errors
HTTP status codes accompany every response in the status line. If you can read a status code in the response, then the request reached its target. While this is good, you can only consider the request a complete success if the response code starts with a 2. For example, 200 and 201 represent successful requests. If the status code is 404 or 500, for example,
 something went wrong, and urllib.request will raise an `HTTPError`.

Sometimes mistakes happen, and the URL provided isn’t correct, or 
a connection can’t be made for another reason. In these 
cases, urllib.request will raise a `URLError`.

Finally, sometimes servers just don’t respond. Maybe your network connection is slow, the server is down, or the server is programmed to ignore specific requests. To deal with this, you can pass a timeout argument to urlopen() to raise a `TimeoutError` after a certain amount of time.

#### Catching Errors
```
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

def make_request(url):
    try:
        with urlopen(url, timeout=10) as response:
            print(response.status)
            return response.read(), response
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")
```

# Using a Custom User-agent string to handle "403 Errors - persay"
# request.py
```
from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request

def make_request(url, headers=None):
     request = Request(url, headers=headers or {})
     try:
     with urlopen(request, timeout=10) as response:
         print(response.status)
         return response.read(), response
     except HTTPError as error:
         print(error.status, error.reason)
     except URLError as error:
         print(error.reason)
     except TimeoutError:
         print("Request timed out")
         
 if __name__ == '__main__':
    body, response = make_request(
     "https://www.httpbin.org/user-agent",
     {"User-Agent": "Real Python"}
 )
200
    body
b'{\n  "user-agent": "Real Python"\n}\n'
 ```
 
 # Fixing the SSL CERTIFICATE_VERIFY_FAILED Error
```
>>> from urllib.request import urlopen
>>> urlopen("https://superfish.badssl.com/")
Traceback (most recent call last):
  (...)
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED]
```

You may be tempted to opt out of verifying the certificate, but this will render your connection insecure and is definitely not recommended:
```
>>> import ssl
>>> from urllib.request import urlopen
>>> unverified_context = ssl._create_unverified_context()
>>> urlopen("https://superfish.badssl.com/", context=unverified_context)
<http.client.HTTPResponse object at 0x00000209CBE8F220>
```

#####Using Certifi to Resolve this error
install:
```bash
pip3 install certifi
```
certifi is a collection of certificates that you can 
use instead of your system’s collection. You do this by 
creating an SSL context with the certifi bundle of 
certificates instead of the OS’s bundle:

```>>> import ssl
>>> from urllib.request import urlopen
>>> import certifi
>>> certifi_context = ssl.create_default_context(cafile=certifi.where())
>>> urlopen("https://sha384.badssl.com/", context=certifi_context)
<http.client.HTTPResponse object at 0x000001C7407C3490>
```

# Make Request With Support For POST and Custom Header
```bash
from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request


def make_request(url, headers=None, data=None):
    request = Request(url, headers=headers or {}, data=data)
     try:
         with urlopen(request, timeout=10) as response:
             print(response.status)
             return response.read(), response
     except HTTPError as error:
         print(error.status, error.reason)
     except URLError as error:
         print(error.reason)
     except TimeoutError:
         print("Request timed out")
         
 if __name__ == '__main__':
     from urllib.parse import urlencode 
     post_dict = {"Title": "Hello World", "Name": "Real Python"}
     url_encoded_data = urlencode(post_dict)
>>> print(url_encoded_data)
    'Title=Hello+World&Name=Real+Python'
    
    post_data = url_encoded_data.encode("utf-8")
    body, response = make_request("https://httpbin.org/anything", data=post_data)
200
    print(body.decode("utf-8"))
```