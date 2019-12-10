#!/usr/bin/env python

from __future__ import print_function
from sys import stderr as std
from os import system
from blessed import Terminal

system("clear")


def main():
    """Program entry point."""
    term = Terminal()

    assert (
        term.hpa(1) != u""
    ), "Terminal does not support hpa (Horizontal position absolute)"

    col, offset = 1, 1

    with term.cbreak():
        inp = None
        print("press 'X' or 'x' to stop.")
        std.write(term.move(term.height, 0) + u"[")
        std.write(term.move_x(term.width) + u"]" + term.move_x(1))
        while "x" != inp != "X":
            if col >= (term.width - 2):
                offset = -1
            elif col <= 1:
                offset = 1
            std.write(term.move_x(col))
            if offset == -1:
                std.write(u".")
            else:
                std.write(u"=")
            col += offset
            std.write(term.move_x(col))
            std.write(u"|\b")
            std.flush()
            inp = term.inkey(0.04)

    print()


if __name__ == "__main__":
    main()
