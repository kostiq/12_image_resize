import argparse
from PIL import Image


def set_resized_filename(path_to_file, width, height):
    namefile = (path_to_file.split('/')[-1])
    part_filename = namefile.split('.')
    return '{}__{}x{}.{}'.format(part_filename[0], width, height, part_filename[-1])


def resize_image(params):

    im = Image.open(params['path'])

    width, height = im.size
    default_scale = round(width/height, 2)

    new_width = params['width']
    new_height = params['height']
    new_scale = params['scale']

    if new_scale:
        im = im.resize((
            width*new_scale, height*new_scale))
    else:
        if new_width and new_height:
            if round(new_width/new_height, 2) != default_scale:
                print('Proportion of image are changed!')
            im = im.resize((new_width, new_height))
        elif not new_width:
            im = im.resize((
                round(new_height*default_scale), new_height))
        else:
            im = im.resize((
                new_width, round(new_width*default_scale)))
    if params['output']:
        im.save(params['output'], 'JPEG')
    else:
        im.save(set_resized_filename(
            params['path'], im.size[0], im.size[1]), 'JPEG')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--path', help="Path to image", required=True)
    parser.add_argument(
        '--width', help="Width of resized image (px)", type=int)
    parser.add_argument(
        '--height', help="Height of resized image (px)", type=int)
    parser.add_argument(
        '--scale', help="Scale of resized image", type=int)
    parser.add_argument(
        '--output', help="Path to resized image")

    args = parser.parse_args()

    if (args.scale and args.width and args.hieght):
        print ('Too many arguments, input "Scale" or "Hieght"/"Width"!')
        exit(1)
    resize_image(vars(args))
