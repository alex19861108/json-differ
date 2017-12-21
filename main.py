import sys
from bin.json_differ import JsonFileComparer

if __name__ == '__main__':
    jfc = JsonFileComparer()
    jfc.do(sys.argv[1], sys.argv[2])