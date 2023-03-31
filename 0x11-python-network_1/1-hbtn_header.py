#!/usr/bin/python3
import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def make_request(url):
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
    url = sys.argv[1]
    # body, response = make_request("https://alx-intranet.hbtn.io/status")
    body, response = make_request(url)
    headers = response.headers
    # print(body)
    # print(type(headers))
    print(headers.get('X-Request-Id'))
