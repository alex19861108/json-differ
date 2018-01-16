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


class JsonFileDiffer(object):
    """
    compare two file
    format:
        key \t  json-string
    """
    def __init__(self):
        self.one = {}
        self.another = {}

    def load_files(self, file_this, file_another):
        self.one = JsonFileDiffer.__load_file(file_this)
        self.another = JsonFileDiffer.__load_file(file_another)

    def generator(self):
        for k, v in self.one.iteritems():
            equals, r = Equals.cmp(v, self.another[k])
            yield k, equals, r

    @staticmethod
    def __load_file(f):
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