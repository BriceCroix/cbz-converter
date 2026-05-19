import argparse
import os

from .converter import cbz2pdf


def main():
    parser = argparse.ArgumentParser(description="CBZ converter CLI")
    parser.add_argument(
        "cbz", help="Input cbz file, or directory containing cbz files."
    )
    parser.add_argument(
        "-o", "--output", help="Output file, or directory if input is a directory."
    )
    parser.add_argument(
        "-q",
        "--quality",
        help="Integer between 0 (lowest) and 100 (highest) to downgrade the quality "
        "of images.",
        type=int,
    )
    parser.add_argument(
        "-W", "--width", help="Maximum width of output in pixels.", type=int
    )
    parser.add_argument(
        "-H", "--height", help="Maximum height of output in pixels.", type=int
    )
    args = parser.parse_args()

    if os.path.isfile(args.cbz):
        output = args.output or os.path.splitext(args.cbz)[0] + ".pdf"
        if cbz2pdf(
            args.cbz, output, quality=args.quality, width=args.width, height=args.height
        ):
            print(f"Created file {output}")
    else:
        input_dir = args.cbz
        output_dir = args.output or input_dir + "-pdf"
        for entry in sorted(os.listdir(input_dir)):
            input_file = os.path.join(input_dir, entry)
            output_file = os.path.join(output_dir, os.path.splitext(entry)[0] + ".pdf")
            if cbz2pdf(
                input_file,
                output_file,
                quality=args.quality,
                width=args.width,
                height=args.height,
            ):
                print(f"Created file {output_file}")
