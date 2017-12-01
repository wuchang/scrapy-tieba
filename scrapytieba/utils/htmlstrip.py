# coding:utf-8
# http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
#from HTMLParser import HTMLParser
from html.parser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data().replace('\t', '').replace('\r\n', '').strip()
