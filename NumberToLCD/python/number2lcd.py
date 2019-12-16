#!/usr/bin/env python3

import argparse
from lcd.display import Display


def main():
    parser = argparse.ArgumentParser(description="Convert a number to LCD form")
    parser.add_argument("-s", "--scale", action="store", type=int, default=1,
                        help="Scale factor")
    parser.add_argument("number", metavar='N', type=int,
                        help="A number to convert to LCD form")

    args = parser.parse_args()

    d = Display(scale_factor=args.scale, number=args.number)
    print(d.show())


if __name__ == "__main__":
    main()
