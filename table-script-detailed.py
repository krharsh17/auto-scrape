from autoscraper import AutoScraper
import pandas as pd

# Define the URL of the site to be scraped
url = "https://www.scrapethissite.com/pages/forms/"

def setup_model():

    # Instantiate the AutoScraper
    scraper = AutoScraper()

    # Define the wanted list by using an example from the webpage
    # This list should contain some text or values that you want to scrape
    wanted_list = ["Boston Bruins", "1990", "44", "24", "0.55", "299", "264", "35"]

    # Build the scraper based on the wanted list and URL
    scraper.build(url, wanted_list)

    # Get the results for all the elements matched
    results = scraper.get_result_similar(url, grouped=True)

    print(results)
    # Display the keys and sample data to understand the structure
    print("Keys found by the scraper:", results.keys())

    scraper.save("teams_model.json")

def prune_rules():
    scraper = AutoScraper()
    scraper.load("teams_model.json")

    scraper.keep_rules(['rule_hjk5', 'rule_9sty', 'rule_2hml', 'rule_3qvv', 'rule_e8x1', 'rule_mhl4', 'rule_h090', 'rule_xg34'])

    scraper.save("teams_model.json")
    
def load_and_run_model():
    scraper = AutoScraper()
    scraper.load("teams_model.json")

    # Get the results for all the elements matched
    results = scraper.get_result_similar(url, grouped=True)

    print(results.values())

    # Assign columns based on scraper keys and expected order of data
    columns = ["Team Name", "Year", "Wins", "Losses", "Win %", "Goals For (GF)", "Goals Against (GA)", "+/-"]

    # Create a DataFrame with the extracted data
    data = {columns[i]: results[list(results.keys())[i]] for i in range(len(columns))}
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    csv_filename = 'teams_data.csv'
    df.to_csv(csv_filename, index=False)

    print(f"Data has been successfully saved to {csv_filename}")

# setup_model()
# prune_rules()
load_and_run_model()