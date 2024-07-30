import argparse
import os


def __create_parser():
    parser = argparse.ArgumentParser(description="Image size detector")
    parser.add_argument(
        "-i", "--image", required=True, metavar="", help="path to image file"
    )

    return parser


def main():
    """
    detects size of an image
    """
    parser = __create_parser()
    args = parser.parse_args()

    if args.image:
        print(f"detecting size of an image {args.image}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
