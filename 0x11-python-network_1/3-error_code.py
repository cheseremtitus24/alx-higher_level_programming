#!/usr/bin/python3
"""
This module makes use of an http Post of an email address to
a url passed in via the commandline
"""
import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request


def make_request(url, headers=None, data=None):
    """
        :param url: resource URL to get content from
        :param headers: Custom Headers to be passed in e.g. Custom User-Agent
        :param data: post data to be sent with a POST HTTP Verb
        :return: request body and http client object
        :raises: No exceptions but handles HTTPError,
        URLError and TimeoutError
        """
    request = Request(url, headers=headers or {}, data=data)
    try:
        with urlopen(request, timeout=10) as response:
            # print(response.status)
            return response.read(), response
    except HTTPError as error:
        print("Error code:", error.status)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")


if __name__ == '__main__':
    from urllib.parse import urlencode

    args_length = len(sys.argv)
    if args_length == 2:
        url = sys.argv[1]
        try:
            body, response = make_request(url)
            character_set = response.headers.get_content_charset()
            if character_set:
                print(body.decode(character_set))
            else:
                print(body.decode('utf-8'))
        except BaseException:
            pass
