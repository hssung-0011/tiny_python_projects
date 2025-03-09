#!/usr/bin/env python3
"""
Author : hsung <hsung@localhost>
Date   : 2025-03-09
Purpose: Chapter 15 연습코드
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Southern fry text",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", type=str, help="Input text or file")

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.text.splitlines():
        words = map(fry, re.split(r"(\W+)", line))
        print("".join(words))


# --------------------------------------------------
def fry(word):
    match1 = re.match("([Yy])ou$", word)
    match2 = re.search("(.+)ing$", word)
    text = (
        match1.group(1) + "'all"
        if match1
        else (
            match2.group(1) + "in'"
            if (match2 and re.search("[aeiouy]", match2.group(1), re.IGNORECASE))
            else word
        )
    )

    return text


# --------------------------------------------------
def test_fry():
    assert fry("you") == "y'all"
    assert fry("You") == "Y'all"
    assert fry("fishing") == "fishin'"
    assert fry("Aching") == "Achin'"
    assert fry("swing") == "swing"


# --------------------------------------------------
if __name__ == "__main__":
    main()
