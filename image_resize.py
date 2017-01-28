import argparse
from PIL import Image
import ntpath


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def set_resized_filename(path_to_file, width, height):
    namefile = path_leaf(path_to_file)
    part_filename = namefile.split('.')
    return '{}__{}x{}.{}'.format(part_filename[0], width, height, part_filename[-1])


def calc_size(width, height, scale, old_width, old_height):
    if scale:
        return (round(old_width*scale), round(old_height*scale))

    default_scale = old_width/old_height

    if width and height:
        if new_width/new_height != width/height:
            print_warning()
        return (width, height)
    elif height:
        return (round(height*default_scale), height)
    else:
        return (width, round(width*default_scale))


def resize_image(parametrs):

    im = Image.open(parametrs.path)

    width, height = im.size

    new_width = parametrs.width
    new_height = parametrs.height
    new_scale = parametrs.scale

    im = im.resize(calc_size(new_width, new_height, new_scale, width, height))
    if parametrs.output:
        im.convert('RGB').save(parametrs.output)
    else:
        im.convert('RGB').save(set_resized_filename(
            parametrs.path, im.size[0], im.size[1]))


def print_warning():
    print('Proportion of image are changed!')


def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--path', help="Path to image", required=True)
    parser.add_argument(
        '--width', help="Width of resized image (px)", type=int)
    parser.add_argument(
        '--height', help="Height of resized image (px)", type=int)
    parser.add_argument(
        '--scale', help="Scale of resized image", type=float)
    parser.add_argument(
        '--output', help="Path to resized image")
    return parser.parse_args()

if __name__ == '__main__':

    args = parse_arg()

    if (args.scale and args.width and args.hieght):
        print ('Too many arguments, input "Scale" or "Hieght"/"Width"!')
        exit(1)
    resize_image(args)
