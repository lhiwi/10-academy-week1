import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.scraper import scrape_play_store_reviews

if __name__ == "__main__":
    # Create a data folder if not exists
    if not os.path.exists("data"):
        os.makedirs("data")
    scrape_play_store_reviews()
