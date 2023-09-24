"""
Projekt 3 - election scraper

author: Magdalena Slánská
email: magdalena@slansti.cz
discord: magdalena2586
"""

import argparse


def main():
    parser = argparse.ArgumentParser(description="Election parser")
    parser.add_argument("url", help="The URL on the VOLBY.CZ portal for scraping")
    parser.add_argument("outfile", help="The output file to export data")

    args = parser.parse_args()
    if not args.url or not args.outfile:
        parser.print_help()
        print("Error: Two parameters are required")
        quit()

    print(f"URL: {args.url}")
    print(f"Outfile: {args.outfile}")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
