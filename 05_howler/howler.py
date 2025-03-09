#!/usr/bin/env python3
"""
HOWLER
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler (upper-cases input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text",type=str, help="Input string or file")

    parser.add_argument(
        "-o", "--outfile", help="Output filename", metavar="str", type=str, default=""
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if os.path.isfile(args.text): ## 빈 문자열은 fFalse 취급이므로 이렇게 복잡하게 경로 검사할 필요 없음..!
        fh_in = open(args.text)
        upper_text = fh_in.read().upper()
    else:
        upper_text = args.text.upper()
    out_path = args.outfile
    if out_path != "": ## 얘도 마찬가지로, 그냥 빈 문자열 자체가 False이므로 그냥 if out_path하고 if랑 else문 바꿨으면 됐음.aa
        fh_out = open(out_path, "wt")
        fh_out.write(upper_text)
    else:
        print(upper_text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
