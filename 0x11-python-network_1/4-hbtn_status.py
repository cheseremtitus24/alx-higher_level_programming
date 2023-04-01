#!/usr/bin/python3
"""
This module makes use of the requests module to send a get request to a
web url then output its payload on-screen
"""

import requests

def make_request(url, params=None, data=None, headers=None):
    """
        :param url: resource URL to get content from
        :param headers: Custom Headers to be passed in e.g. Custom User-Agent
        :param params: post data to be sent with a POST HTTP Verb
        :return: request body and http client object
        :raises: No exceptions but handles HTTPError,
        URLError and TimeoutError
    """
    response = requests.get(url)
    # print(response.status_code)
    return (response.text, response)

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    body, response = make_request(url=url)
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(body), body))

