#!/usr/bin/env python3
"""
Author : hsung <hsung@localhost>
Date   : 2025-03-08
Purpose: Chapter 14 연습코드드
"""

import argparse
import string as s
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme',
                        type=str)

    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    ch_list = '''bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl
               sm sn sp st sw th tr tw thw wh wr sch scr shr sph 
               spl spr squ str thr'''.split()
    ch_list.extend((i for i in s.ascii_lowercase if i not in 'aeiou'))
    ch_list.sort()
    
    first, rest = stemmer(args.word)
    if first in ch_list:
        ch_list.remove(first)
    
    if rest:
        print('\n'.join([i + rest for i in ch_list]))
    else:
        print(f'Cannot rhyme "{args.word}"')    
    
            
    


# --------------------------------------------------
def stemmer(text):
    """Return leading consonants (if any), and 'stem' of word"""
    consonants = ''.join([i for i in s.ascii_lowercase if i not in 'aeiou'])
    text = text.lower()
    match = re.match(f'([{consonants}]+)?([aeiou])(.*)', text)
    
    if match:
        p1 = match.group(1) or ''
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return (p1, p2 + p3)
    else:
        return(text, '')


# --------------------------------------------------
def test_stemmer():
    """test the stemmer"""
    
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')


# --------------------------------------------------
if __name__ == '__main__':
    main()
