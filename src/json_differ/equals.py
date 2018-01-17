# -*- encoding: utf-8 -*-

MSG_EMPTY = ''
MSG_TYPE_ERROR = 'TYPE_ERROR'
MSG_DICT_KEY_NOT_EXISTS = 'DICT_KEY_NOT_EXISTS'
MSG_DICT_KEY_NOT_EQUALS = 'DICT_KEY_NOT_EQUALS'
MSG_LIST_SIZE_NOT_EQUALS = 'LIST_SIZE_NOT_EQUALS'


class Equals(object):
    @staticmethod
    def dict(one, another):
        r = {}
        msg = MSG_EMPTY
        if not type(one) == type(another):
            r['__type__'] = False
            return False, r, MSG_TYPE_ERROR

        if not isinstance(one, dict) or not isinstance(another, dict):
            r['__type__'] = False
            return False, r, MSG_TYPE_ERROR

        if len(one) == 0 and len(another) == 0:
            return True, True, MSG_EMPTY

        if set(one.keys()) != set(another.keys()):
            msg = MSG_DICT_KEY_NOT_EQUALS
            msg = msg + ': ' + ', '.join(set(one.keys()) ^ set(another.keys()))

        equals = True
        for k, v in one.iteritems():
            if k not in another.keys():
                equals &= False
                continue
            e, ret, m = Equals.cmp(v, another[k])
            equals &= e
            r[k] = ret
            if m != MSG_EMPTY:
                if msg == MSG_EMPTY:
                    msg = m
                else:
                    msg = '; '.join([msg, m])
        return equals, r, msg

    @staticmethod
    def cmp(one, another):
        r = {}
        equals = True
        if not type(one) == type(another):
            r['__type__'] = False
            equals = False
            return equals, r, MSG_EMPTY

        if isinstance(one, int):
            equals, r, msg = Equals.int(one, another)
        elif isinstance(one, long):
            equals, r, msg = Equals.long(one, another)
        elif isinstance(one, float):
            equals, r, msg = Equals.float(one, another)
        elif isinstance(one, complex):
            equals, r, msg = Equals.complex(one, another)
        elif isinstance(one, bool):
            equals, r, msg = Equals.bool(one, another)
        elif isinstance(one, tuple):
            equals, r, msg = Equals.tuple(one, another)
        elif isinstance(one, str):
            equals, r, msg = Equals.str(one, another)
        elif isinstance(one, unicode):
            equals, r, msg = Equals.unicode(one, another)
        elif isinstance(one, list):
            equals, r, msg = Equals.list(one, another)
        elif isinstance(one, dict):
            equals, r, msg = Equals.dict(one, another)
        elif one is None and another is None:
            equals, r, msg = True, True, MSG_EMPTY
        else:
            equals, r, msg = False, False, MSG_EMPTY
        return equals, r, msg

    @staticmethod
    def int(one, another):
        return one == another, one == another, MSG_EMPTY

    @staticmethod
    def long(one, another):
        return one == another, one == another, MSG_EMPTY

    @staticmethod
    def float(one, another):
        return one == another, one == another, MSG_EMPTY

    @staticmethod
    def complex(one, another):
        return one == another, one == another, MSG_EMPTY

    @staticmethod
    def bool(one, another):
        return one == another, one == another, MSG_EMPTY

    @staticmethod
    def tuple(one, another):
        return one == another, one == another, MSG_EMPTY

    @staticmethod
    def str(one, another):
        return one == another, one == another, MSG_EMPTY

    @staticmethod
    def unicode(one, another):
        return one == another, one == another, MSG_EMPTY

    @staticmethod
    def list(one, another):
        r = []
        equals = True
        msg = MSG_EMPTY
        if not isinstance(one, list) or not isinstance(another, list):
            return False, False, MSG_EMPTY

        if len(one) == 0 and len(another) == 0:
            return True, True, MSG_EMPTY

        if len(one) != len(another):
            msg = MSG_LIST_SIZE_NOT_EQUALS
            if len(one) > len(another):
                msg = msg + ': base bigger'
            else:
                msg = msg + ': compared bigger'

        for a, b in zip(sorted(one), sorted(another)):
            e, ret, m = Equals.cmp(a, b)
            equals &= e
            r.append(ret)
            if m != MSG_EMPTY:
                if msg == MSG_EMPTY:
                    msg = m
                else:
                    msg = '; '.join([msg, m])
        return equals, r, msg


if __name__ == '__main__':
    xx = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["3333", "4444", "111"]}}
    yy = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["111", "3333", "4444"]}}
    #xx = {"error_message": "INVALID_IMAGE_URL"}
    xx = {"image_id": "0Ajals8uygFhXbOGzKpqCQ==", "faces": [{"face_rectangle": {"width": 86, "top": 277, "height": 86, "left": 169}}]}
    yy = {"image_id": "0Ajals8uygFhXbOGzKpqCQ==", "faces": [{"face_rectangle": {"width": 86, "top": 277, "height": 86, "left": 169}}]}
    xx = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["3333", "4444", "111"]}}
    yy = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["3333", "4444", "555"]}}
    print Equals.cmp(xx, yy)
