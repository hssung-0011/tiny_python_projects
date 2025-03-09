#!/usr/bin/env python3
"""
Author : hsung <hsung@localhost>
Date   : 2025-03-03
Purpose: Rock the Casbah
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adjectives',
                        type=int,
                        default=2)

    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='insults',
                        type=int,
                        default=3)
    
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')
    
    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')
    
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    
    adjectives = '''
    bankrupt base caterwauling corrupt cullionly detestable dishonest false filthsome
    filthy foolish foul gross heedless indistinguishable infected insatiate irksome
    lascivious lecherous loathsome lubbery old peevish rascaly rotten ruinous scurilous
    scurvy slanderous sodden-witted thin-faced toad-spotted unmannered vile wall-eyed'''.split()
    noun = '''
    Judas Satan ape ass barbermonger beggar block boy braggart butt carbuncle coward coxcomb
    cur dandy degeneerate fiend fishmonger fool gull harpy jack jolthead knave liar lunatic
    maw milksop minion ratcatcher recrreant rogue scold slave swine traitor varlet villain worm'''.split()
    
    for n in range(args.number):
        insult_list = random.sample(adjectives, args.adjectives)
        insult_str = ', '.join(insult_list)
        print(f'You {insult_str} {random.choice(noun)}!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
