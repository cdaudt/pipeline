# Simple example to show usage of the data processing pipes
# Reads images, resizes, and stores them
# See https://github.com/cdaudt/pipeline for more details
# Author: Christian Daudt

import argparse
from sources import PictureSource
from filters import SaveImage, ResizeImage

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', nargs=2, type=int, default=[224,224], help='new height/width. Default is 224x224' )
    parser.add_argument('pics', nargs='+', help='pictures to resize')
    args = parser.parse_args()

    return vars(args)
def main():
    args = get_args()

    print("Parameters:{}".format(args))

    si = SaveImage(None, '.jpg', '-small.jpg') # Save image
    rs = ResizeImage(si, args['size'])
    p = PictureSource(rs, args['pics'])
    p.run()


if __name__ == '__main__':
    main()
