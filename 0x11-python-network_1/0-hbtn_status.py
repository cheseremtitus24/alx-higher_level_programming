#!/usr/bin/python3
"""
This module sends a get request to a url and returns
response body as well as an HTTP-client object.

"""
import urllib.request


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body, response = response.read(), response
    body_type = type(body)
    character_set = response.headers.get_content_charset()
    decoded_body = body.decode(character_set)
    print("Body response:")
    print("\t- type: {}".format(body_type))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(decoded_body))
