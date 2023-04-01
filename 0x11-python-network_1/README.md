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

