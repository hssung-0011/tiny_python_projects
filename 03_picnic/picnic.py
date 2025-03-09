#!/usr/bin/env python3
"""
go picnic!
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic lunch list",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("items", metavar="items", nargs="+", help="picnic items")

    parser.add_argument("-s", "--sorted", help="sort 여부", action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items_arg = args.items
    sorted_arg = args.sorted

    items_arg = sorted(items_arg) if sorted_arg == True else items_arg
    if len(items_arg) == 1:
        print(f"You are bringing {items_arg[0]}.")
    elif len(items_arg) == 2:
        print(f"You are bringing {items_arg[0]} and {items_arg[1]}.")
    else:
        last_one = items_arg.pop()
        print(f"You are bringing {', '.join(items_arg)}, and {last_one}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
