from autoscraper import AutoScraper
import pandas as pd

# Define the URL of the site to be scraped
url = "https://www.scrapethissite.com/pages/simple/"

# Instantiate the AutoScraper
scraper = AutoScraper()

# Define the wanted list by using an example from the webpage
# This list should contain some text or values that you want to scrape
wanted_list = ["Andorra", "Andorra la Vella", "84000", "468.0"]

# Build the scraper based on the wanted list and URL
scraper.build(url, wanted_list)

# Get the results for all the elements matched
results = scraper.get_result_similar(url, grouped=True)

# Display the keys and sample data to understand the structure
print("Keys found by the scraper:", results.keys())

# Assign columns based on scraper keys and expected order of data
columns = ["Country Name", "Capital", "Area (sq km)", "Population"]

# Create a DataFrame with the extracted data
data = {columns[i]: results[list(results.keys())[i]] for i in range(len(columns))}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_filename = 'countries_data.csv'
df.to_csv(csv_filename, index=False)

print(f"Data has been successfully saved to {csv_filename}")
