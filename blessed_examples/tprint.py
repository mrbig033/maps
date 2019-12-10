#!/usr/bin/env python
"""
A simple cmd-line tool for displaying FormattingString capabilities.

For example::

    $ python tprint.py bold A rather bold statement.

"""
# std
from __future__ import print_function
from argparse import ArgumentParser as aparser

# local
from blessed import Terminal


def parse_args():
    """Parse sys.argv, returning dict suitable for main()."""
    p = aparser(description="displays argument as specified style")
    p.add_argument("style", type=str, help="style formatter")
    p.add_argument("text", type=str, nargs="+")
    return dict(p.parse_args()._get_kwargs())


def main(style, text):
    """Program entry point."""
    term = Terminal()
    style = getattr(term, style)
    print(style(" ".join(text)))


if __name__ == "__main__":
    exit(main(**parse_args()))
