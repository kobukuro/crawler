import requests as rq
from bs4 import BeautifulSoup


def get_html(url):
    response = rq.get(url)
    html_text = response.text
    return html_text


def soup_analyze(html_text):
    analyze_result = BeautifulSoup(html_text, "lxml")  # 指定 lxml 作為解析器
    return analyze_result


class Web(object):
    pass
