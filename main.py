
import sys
from src.patterns import PatternConverter
from src.arg_parser import parse_args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    try:
        converter = PatternConverter(args.pattern)
    except Exception as ex:
        print ('Error: ',ex)
        exit(-1)
    
    for n in args.integers:
        try:
            print(converter.convert_pattern(n))
        except Exception as ex:
            print ('Error: ', ex)
            exit(0)