#!/usr/bin/env python3
"""random_maker.py - generate small random things"""

import argparse
import random
import secrets
import string
import sys

WORD_BANK = [
    "sun", "river", "code", "engine", "coffee", "planet", "star", "cloud",
    "forest", "echo", "pixel", "dragon", "silver", "thunder", "quiet", "blaze",
    "north", "shadow", "crystal", "ember", "frost", "wave", "stone", "lantern"
]

EMOJI_BANK = ["🔥","⭐","🌙","⚡","🌊","🍕","🚀","🎲","🧠","👾","🎯","💀","🪐","🌈","🦊","🐉"]


def random_password(length=16):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def random_number(lo=0, hi=100):
    return random.randint(lo, hi)


def random_sentence(n=6):
    words = [random.choice(WORD_BANK) for _ in range(n)]
    words[0] = words[0].capitalize()
    return ' '.join(words) + '.'


def random_ascii_art(width=40, height=8):
    chars = "  ..::++**##@@"
    lines = []
    for _ in range(height):
        lines.append(''.join(random.choice(chars) for _ in range(width)))
    return '\n'.join(lines)


def random_emoji(count=10):
    return ' '.join(random.choice(EMOJI_BANK) for _ in range(count))


def build_parser():
    p = argparse.ArgumentParser(description="Generate random things.")
    p.add_argument("--type", choices=["password","number","sentence","ascii","emoji"], default="password")
    p.add_argument("--length", type=int, default=16)
    p.add_argument("--min", type=int, default=0)
    p.add_argument("--max", type=int, default=100)
    p.add_argument("--words", type=int, default=6)
    p.add_argument("--width", type=int, default=40)
    p.add_argument("--height", type=int, default=8)
    p.add_argument("--count", type=int, default=10)
    return p


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    args = build_parser().parse_args(argv)
    if args.type == "password":
        print(random_password(args.length))
    elif args.type == "number":
        print(random_number(args.min, args.max))
    elif args.type == "sentence":
        print(random_sentence(args.words))
    elif args.type == "ascii":
        print(random_ascii_art(args.width, args.height))
    elif args.type == "emoji":
        print(random_emoji(args.count))


if __name__ == "__main__":
    main()
