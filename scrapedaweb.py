from dotenv import load_dotenv
import agentql
from playwright.sync_api import sync_playwright
import csv
from prettytable import PrettyTable

load_dotenv()

PRODUCTS = """
{
    results {
        products[] {
            product_name {
                name
            }
            product_price {
                name
            }
            num_reviews {
                name
            }
            rating
        }
    }
}
"""

NEXT_PAGE_BTN = """
{
    next_page_button_enabled
    next_page_button_disabled
}
"""

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = agentql.wrap(browser.new_page())
        
        page.goto("https://webscraper.io/test-sites/e-commerce/static/phones/touch")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        all_products = []

        while True:
            pagination = page.query_elements(NEXT_PAGE_BTN)
            print("get paginations")
            print(pagination)

            next_button_enabled = pagination.next_page_button_enabled
            next_button_disabled = pagination.next_page_button_disabled

            print(f"enabled button: {next_button_enabled}")
            print(f"disabled button: {next_button_disabled}")

            if not next_button_enabled:
                print("Next button not found or disabled. Exiting loop.")
                break

            products = page.query_elements(PRODUCTS)
            print("scraped product data")
            print(products)

            if products.results and products.results.products:
                for product in products.results.products:
                    all_products.append([
                        product.product_name.name if product.product_name else "N/A",
                        product.product_price.name if product.product_price else "N/A",
                        product.num_reviews.name if product.num_reviews else "N/A",
                        product.rating if product.rating else "N/A"
                    ])
                    print(f"Product added: {product.product_name.name if product.product_name else 'N/A'}")

            # Click next page and scroll
            next_button_enabled.click()
            print("Clicked page")
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        browser.close()

    # Create a PrettyTable object
    table = PrettyTable()
    table.field_names = ["Product Name", "Price", "Number of Reviews", "Rating"]
    table.align["Product Name"] = "l"  # Left align product names
    table.align["Price"] = "r"  # Right align prices
    table.align["Number of Reviews"] = "r"  # Right align number of reviews
    table.align["Rating"] = "c"  # Center align ratings

    # Add rows to the table
    for product in all_products:
        table.add_row(product)

    # Write the table to a CSV file
    with open("products.csv", "w", newline="") as file:
        file.write(table.get_csv_string())

    print("Data written to products.csv in table format")

if __name__ == "__main__":
    main()