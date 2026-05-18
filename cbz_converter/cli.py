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
    args = parser.parse_args()

    if os.path.isfile(args.cbz):
        output = args.output or os.path.splitext(args.cbz)[0] + ".pdf"
        if cbz2pdf(args.cbz, output):
            print(f"Created file {output}")
    else:
        input_dir = args.cbz
        output_dir = args.output or input_dir + "-pdf"
        for entry in os.listdir(input_dir):
            input_file = os.path.join(input_dir, entry)
            output_file = os.path.join(output_dir, os.path.splitext(entry)[0] + ".pdf")
            if cbz2pdf(input_file, output_file):
                print(f"Created file {output_file}")
