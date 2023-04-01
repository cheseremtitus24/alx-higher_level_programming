#!/usr/bin/python3
"""
This module makes use of the requests module to send a get request to a
web url then output its payload on-screen
"""

import requests
from contextlib import closing

from requests import HTTPError


def make_request(url):
    """
        :param url: resource URL to get content from
        :return: request body and http client object
    """
    try:
        with closing(requests.get(url=url, stream=True, timeout=10)) as response:
            # print(response.status)
            return (response.text, response)
    except HTTPError as error:
        print(error.status, error.reason)
    except TimeoutError:
        print("Request timed out")


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    try:
        body, response = make_request(url=url)
        print("Body response:\n\t- type: {}\n\t- content: {}".format(type(body), body))
    except BaseException as e:
        pass
