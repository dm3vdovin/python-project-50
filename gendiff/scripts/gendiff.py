from argparse import ArgumentParser
import json


def parse_json(file_path):
    return json.load(file_path)

def main():
    parser = ArgumentParser(
        prog = 'gendiff',
        description = 'Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        help = 'set format of output'
    )

    args = parser.parse_args()

    print(parse_json(args.first_file))
    print(parse_json(args.second_file))


if __name__ == '__main__':
    main() 