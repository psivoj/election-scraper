"""
Projekt 3 - election scraper

author: Magdalena Slánská
email: magdalena@slansti.cz
discord: magdalena2586
"""

import argparse
import requests
import re
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

    results = []
    parties = {}

    city_rows = main_page_parsed.select("table tr")
    for city_row in city_rows:
        code = city_row.select_one(".cislo a")
        location = city_row.select_one(".overflow_name")
        if code is None or location is None:
            continue
        city_row = {
            "code": code.text,
            "location": location.text
        }

        city_href = urljoin(args.url, code.attrs["href"])
        city_results = parse_city(city_href)
        city_row.update(city_results)
        results.append(city_row)
        if len(parties.keys()) == 0:
            print("Extracting parties")
            parties = city_results["parties"].keys()


def select_to_int(html, selector):
    return int(re.sub(r"\s*", "", html.select_one(selector).text))


def parse_city(url):
    city_results = {
        "parties": {}
    }

    city_request = requests.get(url)
    city_parsed = BeautifulSoup(city_request.text, features="html.parser")

    city_results["registered"] = select_to_int(city_parsed, 'td[headers="sa2"]')
    city_results["envelopes"] = select_to_int(city_parsed, 'td[headers="sa3"]')
    city_results["valid"] = select_to_int(city_parsed, 'td[headers="sa6"]')

    party_results = city_parsed.select("div.t2_470 tr")
    for party_result in party_results:
        party = party_result.select_one('td[headers="t1sa1 t1sb2"]')
        if party is None:
            continue
        city_results["parties"][party.text] = select_to_int(party_result, 'td[headers="t1sa2 t1sb3"]')

    return city_results


if __name__ == '__main__':
    main()

