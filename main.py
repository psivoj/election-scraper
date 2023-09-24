"""
Projekt 3 - election scraper

author: Magdalena Slánská
email: magdalena@slansti.cz
discord: magdalena2586
"""

import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


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

    main_page_request = requests.get(args.url)
    main_page_parsed = BeautifulSoup(main_page_request.text, features="html.parser")

    city_array = main_page_parsed.select("table td.cislo a")
    for city_a in city_array:
        city_href = urljoin(args.url, city_a.attrs["href"])
        parse_city(city_href)

def parse_city(url):
    city_results = {}
    print(url)
    return city_results


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
