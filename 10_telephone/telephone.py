#!/usr/bin/env python3
"""
Author : hsung <hsung@localhost>
Date   : 2025-03-04
Purpose: Chapter 10 연습 코드
"""

import argparse
import random
import os
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Precent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()
    
    if args.mutations <= 1 and args.mutations >= 0:
        pass
    else:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')
        
    
    args.text = open(args.text).read().rstrip() if os.path.isfile(args.text) else args.text
    
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    text = args.text
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    
    mutations = args.mutations
    num_mutations = round(len(text) * mutations)
    indexes = random.sample(range(len(text)), num_mutations)
    print(f'You said: "{args.text}"')
    for i in indexes:
        new_char = random.choice(alpha.replace(text[i], ''))
        text = text[:i] + new_char + text[i+1:]
    
    print(f'I heard : "{text}"')



# --------------------------------------------------
if __name__ == '__main__':
    main()
