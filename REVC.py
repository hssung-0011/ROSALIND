#!/usr/bin/env python
"""
Complementing a Strand of DNA
"""

import argparse
import os


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        help="Input file",
        default=None
    )

    return parser.parse_args()


# ----------------------------------------

def main():
    
    args = get_args()

    output = open("/mnt/c/ROSALIND_output/Complementing.txt","wt")
    for line in args.file.readlines():
        rev_list = list(line.rstrip())
        rev_list.reverse()
        changed = ''.join(map(trans, rev_list))
        output.write(changed)


# -----------------------------

def trans(base):
    rev = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return(rev[base])



# -----------------------------

def test_trans():
    assert trans('A') == 'T'
    assert trans('G') == 'C'    

    

#--------------------------
if __name__ == "__main__":
    main()