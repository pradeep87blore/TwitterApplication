"""
Utils file
"""

import os

TWITTER_AUTH_FILE = '\\Tokens\\twitter_tokens.txt'
PROXY_FILE = '\\Proxy\\proxy.txt'


def get_tokens():
    """
    Read the consumer key, consumer secret, access token and access token secret from a file
    :return:
    """

    # create element tree object
    token_file_path = os.path.dirname(__file__) + TWITTER_AUTH_FILE

    token_file = open(token_file_path)

    tokens = {}  #dictionary
    for line in token_file.readlines():
        temp_line = line.split('=')
        tokens[temp_line[0]] = temp_line[1].strip()

    return tokens


def get_proxy():
    """
    Return the local proxy

    :return: First return value is the http proxy, second one is the https proxy
    """

    proxy_file_path = os.path.dirname(__file__) + PROXY_FILE

    proxy_file = open(proxy_file_path)

    httpProxy = proxy_file.readline()
    httpsProxy = proxy_file.readline()

    return httpProxy, httpsProxy