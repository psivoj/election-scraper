# Czech Election Scraper
The script reads the webpages of Czech portal [Results of Elections and
Referendums](https://www.volby.cz). It reads the results from the page
of the municipality and exports the total results in the CSV file.

## Installation
1.Install Python (may be already installed in your system)
2. Load the scraper from the GitHub: https://github.com/psivoj/election-scraper
3. Install libraries necessary for the scraper: `pip install -r requirements.txt`

## Usage

`python main.py [URL] [outfile]`
* URL - the address of the municipality details page
* outfile - the file where the results should be stored

Example:

1. Open the municipality page on the [Results of Elections and 
Referendums](https://www.volby.cz) and copy the URL of the page.

Example: https://volby.cz/pls/ps2017nss/ps32?xjazyk=EN&xkraj=9&xnumnuts=5302
2. Run the scraping script:

Example: `python main.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=EN&xkraj=9&xnumnuts=5302" results_pardubice.csv`

Note: the URL page should contain quotes, so the ampersands (&) are correctly
interpreted.