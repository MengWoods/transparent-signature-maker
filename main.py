#!/usr/bin/python3
import utils.constant as con
import utils.imgUtils as ut

# Read configs
p = con.configargparse.ArgParser()
p.add('-b', '--base-path', default='./files', type=str, help='Base path to the picture files for processing')
p.add('-i', '--input-files', required=True, nargs='+', help="Input picture files name(s), add space between two files")
p.add('-g', '--gray-threshold', type=float, default=140, help="Gray threshold [0,255] to process signature image")
p.add('-c', '--color', type=str, default='black', help='Define the color of output signature')

options = p.parse_args()

def main():
    image_utils = ut.imgUtils(options.base_path, \
                              options.input_files, \
                              options.gray_threshold, \
                              options.color)
    image_utils.process()

if __name__ == "__main__":
    main()