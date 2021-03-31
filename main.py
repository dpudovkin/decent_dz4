import sys
import argparse


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
        students = f.read().splitlines()

    result = {}
    for item in students:
        result[item] = 0
    next = 1
    while len(students) > 0:
        j = abs((next) ^ param) % len(students)
        param = param^len(students)
        result[students[j]] = next
        students.pop(j)
        next = 1 if next==num else next+1

    for student in result:
        print('{}: {}\n'.format(student, result[student]))
