#!/usr/bin/env python3
"""
Author : hsung <hsung@localhost>
Date   : 2025-02-26
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crows's nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word")
    parser.add_argument("--side", metavar="side", help="larboard, starboard", default="larboard")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    side = args.side
    word = args.word
    if word[0].lower() in 'abcdefghijklmnopqrstuvwxyz':    
        is_upper = True if word[0].upper() == word[0] else False
        article = "An" if word[0].lower() in "aeiou" else "A"
        article = article.lower() if is_upper == False else article
        print(f"Ahoy, Captain, {article} {word} off the {side} bow!")
    else:
        print("not a correct word")

# --------------------------------------------------
if __name__ == "__main__":
    main()
