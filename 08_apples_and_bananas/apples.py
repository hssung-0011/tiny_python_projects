#!/usr/bin/env python3
"""
Author : hsung <hsung@localhost>
Date   : 2025-03-01
Purpose: Chapter 8 예제코드
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file',
                        type=str)

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=['a', 'e', 'i', 'o', 'u'])
    
    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read()


    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    outcome = ''
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    vowel = args.vowel
    for letter in args.text:
        is_upper = True if letter.upper() == letter else False  # 대소문자 확인
        letter = args.vowel if letter.lower() in vowel_list else letter  # 자모음 확인
        letter = letter.upper() if is_upper else letter  # letter이 원래 대문자였다면 대문자 전환. args.vowel은 원래 소문자이기 때문
        outcome += letter
    # text = [
    #     vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c
    #     for c in args.text
    # ]  # comprehension
    print(outcome)


# --------------------------------------------------
if __name__ == '__main__':
    main()
