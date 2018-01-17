import sys

from json_differ.json_differ import JsonFileDiffer

if __name__ == '__main__':
    jfc = JsonFileDiffer()
    jfc.load_files(sys.argv[1], sys.argv[2])
    for key, equals, r in jfc.generator():
        print key, equals, r