# -*- encoding: utf-8 -*-

class Equals(object):
    @staticmethod
    def dict(one, other):
        r = {}
        if not type(one) == type(other):
            r['__type__'] = False
            return False, r

        if not isinstance(one, dict) or not isinstance(other, dict):
            r['__type__'] = False
            return False, r

        if len(one) == 0 and len(other) == 0:
            return True, True

        equals = True
        for k, v in one.iteritems():
            if k not in other.keys():
                return False
            e, ret = Equals.cmp(v, other[k])
            equals &= e
            r[k] = ret
        return equals, r

    @staticmethod
    def cmp(one, other):
        r = {}
        equals = True
        if not type(one) == type(other):
            r['__type__'] = False
            equals = False
            return equals, r

        if isinstance(one, int):
            equals, r = Equals.int(one, other)
        elif isinstance(one, long):
            equals, r = Equals.long(one, other)
        elif isinstance(one, float):
            equals, r = Equals.float(one, other)
        elif isinstance(one, complex):
            equals, r = Equals.complex(one, other)
        elif isinstance(one, bool):
            equals, r = Equals.bool(one, other)
        elif isinstance(one, tuple):
            equals, r = Equals.tuple(one, other)
        elif isinstance(one, str):
            equals, r = Equals.str(one, other)
        elif isinstance(one, unicode):
            equals, r = Equals.unicode(one, other)
        elif isinstance(one, list):
            equals, r = Equals.list(one, other)
        elif isinstance(one, dict):
            equals, r = Equals.dict(one, other)
        elif one is None and other is None:
            equals, r = True, True
        else:
            equals, r = False, False
        return equals, r

    @staticmethod
    def int(one, other):
        return one == other, one == other

    @staticmethod
    def long(one, other):
        return one == other, one == other

    @staticmethod
    def float(one, other):
        return one == other, one == other

    @staticmethod
    def complex(one, other):
        return one == other, one == other

    @staticmethod
    def bool(one, other):
        return one == other, one == other

    @staticmethod
    def tuple(one, other):
        return one == other, one == other

    @staticmethod
    def str(one, other):
        return one == other, one == other

    @staticmethod
    def unicode(one, other):
        return one == other, one == other

    @staticmethod
    def list(one, other):
        r = {}
        equals = True
        if not isinstance(one, list) or not isinstance(other, list):
            return False, False

        for a, b in zip(sorted(one), sorted(other)):
            e, ret = Equals.cmp(a, b)
            equals &= e
            r = ret
        return equals, r


if __name__ == '__main__':
    xx = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["3333", "4444", "111"]}}
    yy = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["111", "3333", "4444"]}}
    print Equals.cmp(xx, yy)
