#!/usr/bin/env python3
"""
Author : hsung <hsung@localhost>
Date   : 2025-03-06
Purpose: Chapter 12 연습코드
"""

import argparse
import random
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file',
                        type=str)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()
    args.text = open(args.text).read().rstrip() if os.path.isfile(args.text) else args.text

    
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    new = []
    random.seed(args.seed)
    for char in args.text:
        char = choose(char)
        new.append(char)
        
        
    print(''.join(new))

# --------------------------------------------------
def choose(char):
    char = char.upper() if random.choice([0,1]) == 1 else char.lower()
    return char

# --------------------------------------------------
def test_choose():
    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'c'
    assert choose('d') == 'd'
    random.setstate(state)

# --------------------------------------------------
if __name__ == '__main__':
    main()
