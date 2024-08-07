#!/usr/bin/env python3
import argparse
from .diff_generator import generate_diff


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument(
        "first_file",
        help="Path to the first configuration file")
    parser.add_argument(
        "second_file",
        help="Path to the second configuration file")
    parser.add_argument(
        '-f',
        '--format',
        help='Set format of output',
        default='stylish',
        choices=[
            'stylish',
            'plain',
            'json'])
    return parser.parse_args()


def main():
    args = parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)
