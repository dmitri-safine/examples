import argparse
import os
from PIL import Image


def __create_parser():
    parser = argparse.ArgumentParser(description="Image size detector")
    parser.add_argument(
        "-i", "--image", required=True, metavar="", help="path to image file"
    )

    return parser


def __get_image_size(image_file):
    image_path = f"/images/{image_file}"
    image = Image.open(image_path)
    width, height = image.size
    print(f"{width}x{height}")


def main():
    """
    detects size of an image
    """
    parser = __create_parser()
    args = parser.parse_args()

    if args.image:
        __get_image_size(args.image)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
