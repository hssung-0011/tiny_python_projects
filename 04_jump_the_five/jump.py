#!/usr/bin/env python3
"""
Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("str", metavar="str", help="Input text")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    jumper = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }

    args = get_args()
    str_arg = args.str

    for chr in str_arg:
        if chr in jumper.keys():
            chr = jumper[chr]
        print(chr, end="")


# --------------------------------------------------
if __name__ == "__main__":
    main()
