# ScrapeDaWeb_Lvl3

ScrapeDaWeb_Lvl3 is a web scraping project that uses a browser agent to extract product information from e-commerce websites. It demonstrates the use of AgentQL and Playwright for advanced web scraping techniques.

## Features

- Scrapes product information including name, price, number of reviews, and rating
- Handles pagination to scrape multiple pages
- Outputs data in a formatted CSV file
- Uses browser automation for dynamic content loading

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ScrapeDaWeb_Lvl3.git
   cd ScrapeDaWeb_Lvl3
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables by creating a `.env` file in the project root directory.

## Usage

To run the scraper, execute the following command:

The script will start scraping the target website and save the results in a file named `products.csv`.

## Project Structure

- `scrapedaweb.py`: Main script for web scraping using AgentQL and Playwright
- `browseragent.py`: Alternative implementation using a different approach (currently not in use)
- `products.csv`: Output file containing scraped data in CSV format
- `.env`: Environment variables file (not included in the repository)

## Code Overview

### Main Scraping Logic

The main scraping logic is implemented in the `scrapedaweb.py` file:


This script uses Playwright to automate browser interactions and AgentQL to query the page for specific elements. It iterates through pages, extracts product information, and stores it in memory before writing to a CSV file.

### Data Extraction Queries

The script uses GraphQL-like queries to extract data:

These queries define the structure of the data to be extracted from the web page.

## Output

The script generates a CSV file named `products.csv` with the following columns:
- Product Name
- Price
- Number of Reviews
- Rating

The data is formatted using PrettyTable for better readability.

## Contributing

Contributions to ScrapeDaWeb_Lvl3 are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

S4MPL3BI4S // vivasecuris.co
