#!/usr/bin/env python3
"""
Author : hsung <hsung@localhost>
Date   : 2025-03-05
Purpose: Chapter11 연습코드
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)



    parser.add_argument('-n',
                        '--number',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)
 
    if parser.parse_args().number < 1:
        parser.error(f'--num "{parser.parse_args().number}" must be greater than 0')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for i in range(args.number,0,-1):
        print(verse(i))
        print(end='\n' if i != 1 else '')


# -------------------------------------------------
def verse(bottle):
    """Sing a verse"""
    def is_single(bt):
        return '' if bt == 1 else 's'
    # is_single = '' if bottle == 1 else 's'
    is_last = 'No more bottles of beer on the wall!' if bottle == 1 else f'{bottle-1} bottle{is_single(bottle-1)} of beer on the wall!'
    
    return '\n'.join([
        f'{bottle} bottle{is_single(bottle)} of beer on the wall,', f'{bottle} bottle{is_single(bottle)} of beer,', 
        'Take one down, pass it around,',
        is_last
    ])



# --------------------------------------------------
def test_verse(): ## verse 함수를 테스트하는 테스트코드
    """Test verse"""
    
    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,', 
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])
    
    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])




if __name__ == '__main__':
    main()
