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
    def load_files(self, fthis, fother):
        self.one = self.__load_file(fthis)
        self.other = self.__load_file(fother)

    def generator(self):
        for k, v in self.one.iteritems():
            equals, r = Equals.cmp(v, self.other[k])
            yield k, equals, r

    def __load_file(self, f):
        d = {}
        with open(f, 'rb') as fd:
            for line in fd:
                pieces = line.strip().split('\t')
                if len(pieces) == 2:
                    key, json_string = pieces
                    d[key] = json.loads(json_string)

                    # filter
                    if 'faces' in d[key]:
                        for face in d[key]['faces']:
                            if 'landmark' in face:
                                del face['landmark']

        return d

if __name__ == '__main__':
    xx = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["3333", "4444", "111"]}}
    yy = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["111", "3333", "4444"]}}
    print JsonItem(json.dumps(xx)) == JsonItem(json.dumps(yy))