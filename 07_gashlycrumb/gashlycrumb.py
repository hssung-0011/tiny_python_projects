#!/usr/bin/env python3
"""
Author : hsung <hsung@localhost>
Date   : 2025-03-01
Purpose: chapter 7 연습코드
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gaashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        type=str,
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt',
                        help='A readable file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_dict = {}
    for line in args.file:
        dict_key = line[0].upper()
        file_dict[dict_key] = line  # 첫글자 key로 하는 딕셔너리 생성
    # lookup = {line[0].upper() : line for line in args.file}  # comprehension 사용해 코드 압축

    for letter in args.letter:
        if letter.upper() in file_dict:
            print(file_dict[f'{letter.upper()}'], end='')
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
