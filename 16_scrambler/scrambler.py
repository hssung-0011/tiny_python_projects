#!/usr/bin/env python3
"""
Author : hsung <hsung@localhost>
Date   : 2025-03-09
Purpose: Chapter 16 연습코드드
"""

import argparse
import random
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Scramble the letters of words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("text",
                        metavar="text",
                        help="Input text or fileoptional arguments:")

    parser.add_argument("-s",
                        "--seed",
                        help="Random seed",
                        metavar="seed",
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    
    for line in args.text.splitlines():
        words = [scramble(wd) for wd in re.split(splitter, line)]
        print("".join(words))


# --------------------------------------------------
def scramble(word):
    """Scramble a word"""

    if len(word) <= 3:
        return word

    middle = list(word[1:-1])
    random.shuffle(middle)
    return "".join([word[0]] + middle + [word[-1]])


# --------------------------------------------------
def test_scramble():
    """Test scramble"""
    state = random.getstate()
    random.seed(1)
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate(state)


# --------------------------------------------------
if __name__ == "__main__":
    main()
