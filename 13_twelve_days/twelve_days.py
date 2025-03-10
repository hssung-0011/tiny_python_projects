#!/usr/bin/env python3
"""
Author : hsung <hsung@localhost>
Date   : 2025-03-08
Purpose: Chapter 13 연습코드
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()
    if args.num < 1 or args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')
    
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # verses = [verse(i) for i in range(1, args.num + 1)]
    verses = map(verse, range(1, args.num + 1))
    
    args.outfile.write('\n\n'.join(verses))
    
    
    

# -------------------------------------------------
def verse(day):
    """Create a verse"""
    ordinal = ['zero', 'first', 'second', 'third', 'fourth', 'fifth', 
               'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    present = ['A partridge in a pear tree',
               'Two turtle doves',
               'Three French hens',
               'Four calling birds',
               'Five gold rings',
               'Six geese a laying',
               'Seven swans a swimming',
               'Eight maids a milking',
               'Nine ladies dancing',
               'Ten lords a leaping',
               'Eleven pipers piping',
               'Twelve drummers drumming']
    ordinal_day = ordinal[day]
    present_list = [f'{present[i-1]},' if i != 1 else 'And a partridge in a pear tree.' if day != 1 else 'A partridge in a pear tree.' 
                    for i in range(day,0,-1)]
    return '\n'.join([f'On the {ordinal_day} day of Christmas,', 'My true love gave to me,'] + present_list)

# -------------------------------------------------
def test_verse():
    """Test verse"""
    assert verse(1) == '\n'.join([
        'On the first day of Christmas,', 'My true love gave to me,',
        'A partridge in a pear tree.'
    ])
    
    assert verse(2) == '\n'.join([
        'On the second day of Christmas,', 'My true love gave to me,',
        'Two turtle doves,', 'And a partridge in a pear tree.'
    ])

# --------------------------------------------------
if __name__ == '__main__':
    main()
