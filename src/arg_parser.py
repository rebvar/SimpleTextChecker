import argparse

def parse_args(args):

    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('pattern', default="", type=str, nargs=None, help='pattern')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='set of integers')
    return parser.parse_args(args)