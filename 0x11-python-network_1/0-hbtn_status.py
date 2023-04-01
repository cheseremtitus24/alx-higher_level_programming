#!/usr/bin/python3
"""
This module sends a get request to a url and returns
response body as well as an HTTP-client object.

"""
import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def make_request(url='https://alx-intranet.hbtn.io/status'):
    """
    :param url: resource URL to get content from
    :return: request body and http client object
    :raises: No exceptions but handles HTTPError,
    URLError and TimeoutError
    """
    try:
        with urlopen(url, timeout=10) as response:
            # print(response.status)
            return response.read(), response
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")


if __name__ == '__main__':
    body, response = make_request()
    body_type = type(body)
    character_set = response.headers.get_content_charset()
    decoded_body = body.decode(character_set)
    print("Body response:")
    print("\t- type: {}".format(body_type))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(decoded_body))
