import re

FILENAME = 'folder1/folder2/file.ext'


def extention_slice(filename):
    point_pos = filename.find('.')
    return filename[point_pos + 1:]

def extention_part(filename):
    return filename.partition('.')[2]

def extention_regex(filename):
    regex = r'\.(.+$)'
    return re.search(regex, filename)[1]

if __name__ == '__main__':
    print(extention_slice(FILENAME))
    print(extention_part(FILENAME))
    print(extention_regex(FILENAME))