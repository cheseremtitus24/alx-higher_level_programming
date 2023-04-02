#!/usr/bin/python3
"""
This module makes use of the requests module to send a get request to a
web url then output its payload on-screen
"""
import sys

import requests
from requests import HTTPError
from requests.auth import HTTPBasicAuth


def make_request(
        url,
        username=None,
        access_token=None,
        data=None,
        method='get',
        params=None):
    """
        :param url: resource URL to get content from
        :return: request body and http client object
    """
    try:
        with requests.Session() as s:
            if method == 'get':
                response = s.get(url=url, data=data, timeout=10, params=params)

            elif method == 'post':
                response = s.post(
                    url=url, data=data, timeout=10, params=params)
            elif method == 'auth':
                response = s.get(
                    url, timeout=10, auth=HTTPBasicAuth(
                        username, access_token))

        # print(response.status_code)
        return response.text, response
    except HTTPError as error:
        print(error.status, error.reason)
    except TimeoutError:
        print("Request timed out")


if __name__ == '__main__':
    args_length = len(sys.argv)
    if args_length == 3:
        username = sys.argv[1]
        password = sys.argv[2]
        git_user_url = "https://api.github.com/user"
        try:
            body, response = make_request(
                url=git_user_url, method='auth', username=username, access_token=password)
            # if status_code is btwn 200 and 400 response == True Else False
            if response:
                try:
                    result_dict = response.json()
                except BaseException:
                    print("Not a valid JSON")
                else:
                    if result_dict:
                        id = result_dict.get('id')
                        print("{}".format(id))
                    else:
                        print("No result")
            else:
                print("None")
                # print("Error code:", response.status_code)

        except BaseException as e:
            print(e)
