#!/usr/bin/env python3

import argparse
import base64
import os
import sys

# Light green ANSI color
GREEN = "\033[92m"
RESET = "\033[0m"

def print_banner():
    print(f"""{GREEN}
███████╗ ███████╗███████╗
██╔════╝ ██╔════╝██╔════╝
███████╗ █████╗  ███████╗
╚════██║ ██╔══╝  ╚════██║
███████║ ███████╗███████║
╚══════╝ ╚══════╝╚══════╝
    Extra64 - Base64 Tool
{RESET}""")


def encode_file(input_file, output_file):
    try:
        with open(input_file, "rb") as f:
            raw_data = f.read()
            b64_data = base64.b64encode(raw_data)

        with open(output_file, "wb") as out:
            out.write(b64_data)

        os.remove(input_file)
        print(f"{GREEN}[+] File encoded and saved to '{output_file}'")
        print(f"[+] Deleted original file '{input_file}'{RESET}")
    except Exception as e:
        print(f"{GREEN}[!] Error during encoding: {e}{RESET}")
        sys.exit(1)

def decode_file(input_file, output_file):
    try:
        with open(input_file, "rb") as f:
            b64_data = f.read()
            raw_data = base64.b64decode(b64_data)

        with open(output_file, "wb") as out:
            out.write(raw_data)

        os.remove(input_file)
        print(f"{GREEN}[+] File decoded and saved to '{output_file}'")
        print(f"[+] Deleted base64 file '{input_file}'{RESET}")
    except Exception as e:
        print(f"{GREEN}[!] Error during decoding: {e}{RESET}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="A tool to encode files to base64 and decode them back. Automatically deletes the input file.",
        usage="extra -i <input_file> -o <output_file> -m <encode|decode>"
    )
    parser.add_argument("-i", "--input", required=True, help="Input file")
    parser.add_argument("-o", "--output", required=True, help="Output file")
    parser.add_argument("-m", "--mode", choices=["encode", "decode"], default="encode", help="Mode: encode (default) or decode")

    args = parser.parse_args()
    input_file = args.input
    output_file = args.output
    mode = args.mode

    print_banner()

    if not os.path.isfile(input_file):
        print(f"{GREEN}[!] Input file '{input_file}' not found.{RESET}")
        sys.exit(1)

    if mode == "encode":
        encode_file(input_file, output_file)
    elif mode == "decode":
        decode_file(input_file, output_file)

if __name__ == "__main__":
    main()
