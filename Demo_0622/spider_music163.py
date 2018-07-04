#! /usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import pandas as pd
import numpy as np



url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_573583409?csrf_token="

payload = {
	'params':'ItFfhyPsF/mlNFywXRynsHDkLafy5eq/f3Ky9gtEZeo6+0/ZMMuCH92hOLRuUiKx/QqY03BjUemxMaawmDpXwpJ7kC7KO9vjVEruiKLfEt9iLKN7ka2Pkv02Bssowf6pjkBG1uN7I26QqaJnJJiwwnifAa4ck6jd/gNhfHHqo2Kh9PY9qvbBIq9XHLo6zNe9',
	'encSecKey':'5492dae48a8c9af96cf19ea7f82075923e1d38cc1112a0199db54a07e0c572cfec1cc8a0845c3bfc0d0feb9d6a0348e5553bbb2a3273e78112f27034efa5480bba3edbf74a78f158ebfeb2c6fc8db1e5804d48a40e3d96bf468e562211ffd5ae0e3e12d4feac8dec053886bc64482770e8520e14c2e8228caf0c8216cdd2505f',
}

headers = {
	'Cookie':'JSESSIONID-WYYY=B3vV%5CwcFEdERbytrDk%2FuF%2BAOYfulpR8rDa%2B9Jb7tfMYxnWf4gn%2F68YrM4Oo2N7iqYC2QcvCfxv5ZMl98VkvRdo3%2BUS5N8%2BulE%5CFpVWYWsvoJjaE9oI9I%2F%2FZt8kXc%2F8CYnPN0E5SpPvcfoO6uWnCwwBHGJ8B7Bej5uAJ19wBUxZpuUYE%2B%3A1529650935846; _iuqxldmzr_=32; _ntes_nnid=70c8ab6dbd32b2c30fb4fad91303ee4e,1529649135885; _ntes_nuid=70c8ab6dbd32b2c30fb4fad91303ee4e; __utma=94650624.415354408.1529649136.1529649136.1529649136.1; __utmc=94650624; __utmz=94650624.1529649136.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_TID=ECGJNX4g6PCIJ40I4XtI7KuVkXpNQTsX; __utmb=94650624.8.10.1529649136',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}

response = requests.post(url, data=payload, headers=headers)
encoding = 'utf-8-sig'

df = pd.DataFrame(response.json()['comments'])
df.to_csv("music163.csv",encoding = encoding)
