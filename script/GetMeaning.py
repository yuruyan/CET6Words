import requests
from hashlib import md5
import urllib.parse as parse
import time


def generate_signature(params: dict):
    value_array = []
    keys = sorted(list(params.keys()))
    for value in keys:
        value_array.append(str(params[value]))
    return md5(('/dictionary/word/query/web' + ''.join(value_array) +
                '7ece94d9f9c202b0d2ec557dg4r9bc').encode('utf-8')).hexdigest()


def get_meaning(word: str):
    headers = {
        'Origin':
        'https://www.iciba.com',
        'Referer':
        'https://www.iciba.com/',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
    }
    params = {
        'client': 6,
        'key': 1000006,
        'timestamp': int(time.time() * 1000),
        'word': parse.quote(word)
    }
    params['signature'] = generate_signature(params)
    url = 'https://dict.iciba.com/dictionary/word/query/web'
    # url = 'https://dict.iciba.com/dictionary/word/query/web?' + parse.urlencode(
    #     params)
    # print(parse.urlencode(params))
    resp = requests.get(url, params=params, headers=headers)
    return resp.text


