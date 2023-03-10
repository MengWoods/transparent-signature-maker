#!/usr/bin/python3
import utils.constant as con

# Read configs
p = con.configargparse.ArgParser()
p.add('-b', '--base-path', default='./files', type=str, help='Base path to the picture files for processing')

p.add('-i', '--input-files', required=True, nargs='+', help="Input picture files name(s), add space between two files")
p.add('-g', '--gray-threshold', type=float, default=100, help="Gray threshold [0,255] to process signature image, higher value, lower gray threshold")
options = p.parse_args()

def main():


if __name__ == "__main__":
    main()