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

    args_length = len(sys.argv)
    if args_length == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        post_dict = {"email": email}
        url_encoded_data = urlencode(post_dict)
        # print(url_encoded_data)

        post_data = url_encoded_data.encode("utf-8")
        body, response = make_request(url, data=post_data)
        print(body.decode("utf-8"))
