import sys

from src.json_differ.json_differ import JsonFileComparer

if __name__ == '__main__':
    jfc = JsonFileComparer()
    jfc.load_files(sys.argv[1], sys.argv[2])
    for key, equals, r in jfc.generator():
        print key, equals, r