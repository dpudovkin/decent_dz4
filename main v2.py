import sys
import argparse
import hashlib

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', nargs='?')
    parser.add_argument('--parametr', nargs='?')
    parser.add_argument('--numbilets', nargs='?')
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    file_path = namespace.file
    param = int(namespace.parametr)
    num = int(namespace.numbilets)

    with open(file_path, 'r') as f:
        raw_data = f.read()
        students = raw_data.splitlines()
        hash = hashlib.sha256((students[param % len(students)]+raw_data).encode())


    result = {}
    for item in students:
        result[item] = 0

    next=1
    while len(students) > 0:
        j = int(hash.hexdigest(),16) % len(students)
        hash = hashlib.sha256((hash.hexdigest()+students[j]).encode())
        result[students[j]] = next
        students.pop(j)
        next = 1 if next==num else next+1

    for student in result:
        print('{}: {}\n'.format(student, result[student]))
