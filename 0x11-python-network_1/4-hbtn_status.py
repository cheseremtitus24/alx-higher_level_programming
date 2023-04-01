#!/usr/bin/python3
"""
This module makes use of the requests module to send a get request to a
web url then output its payload on-screen
"""

import requests


def make_request(url):
    """
        :param url: resource URL to get content from
        :return: request body and http client object
    """
    response = requests.get(url)
    return (response.text, response)


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    body, response = make_request(url=url)
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(body), body))
