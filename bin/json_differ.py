# -*- encoding: utf-8 -*-
import json
from equals import Equals

class JsonItem(object):
    """
    compare two json string
    """
    def __init__(self, s):
        self._d = json.loads(s)

    def data(self):
        return self._d

    def __eq__(self, other):
        return Equals.cmp(self._d, other.data())

class JsonFileComparer(object):
    """
    compare two file
    format:
        key \t  json-string
    """
    def do(self, fthis, fother):
        one = self.load_file(fthis)
        other = self.load_file(fother)
        return Equals.cmp(one, other)

    def load_file(self, f):
        d = {}
        with open(f, 'rb') as fd:
            for line in fd:
                pieces = line.strip().split('\t')
                if len(pieces) == 2:
                    key, json_string = pieces
                    d[key] = json.loads(json_string)
        return d

if __name__ == '__main__':
    xx = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["3333", "4444", "111"]}}
    yy = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["111", "3333", "4444"]}}
    print JsonItem(json.dumps(xx)) == JsonItem(json.dumps(yy))