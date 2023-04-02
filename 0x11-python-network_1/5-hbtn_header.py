#!/usr/bin/python3
"""
This module makes use of the requests module to send a get request to a
web url then output its payload on-screen
"""
import sys

import requests
from requests import HTTPError


def make_request(url):
    """
        :param url: resource URL to get content from
        :return: request body and http client object
    """
    try:
        with requests.Session() as s:
            response = s.get(url=url, timeout=10)
        # print(response.status)
        return response.text, response
    except HTTPError as error:
        print(error.status, error.reason)
    except TimeoutError:
        print("Request timed out")


if __name__ == '__main__':
    args_length = len(sys.argv)
    if args_length == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        # body, response = make_request("https://alx-intranet.hbtn.io/status")
        try:
            body, response = make_request(url=url)
            print(response.headers.get('X-Request-Id'))
        except BaseException as e:
            print(e)
