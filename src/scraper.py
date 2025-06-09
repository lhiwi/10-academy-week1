from google_play_scraper import Sort, reviews
import csv
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(filename='scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

apps = [
    {"bank_name": "Commercial Bank of Ethiopia", "app_id": "com.combanketh.mobilebanking"},
    {"bank_name": "Bank of Abyssinia", "app_id": "com.boa.boaMobileBanking"},
    {"bank_name": "Dashen Bank", "app_id": "com.dashen.dashensuperapp"}
]


def scrape_play_store_reviews(output_path="data/"):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'{output_path}bank_reviews_{timestamp}.csv'

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['review_text', 'rating', 'date', 'bank_name', 'source'])
        writer.writeheader()

        for app in apps:
            logging.info(f"🔄 Fetching reviews for {app['bank_name']}...")

            try:
                results, _ = reviews(
                    app['app_id'],
                    lang='en',
                    country='us',
                    sort=Sort.NEWEST,
                    count=500
                )

                for entry in results:
                    writer.writerow({
                        'review_text': entry['content'],
                        'rating': entry['score'],
                        'date': entry['at'].strftime('%Y-%m-%d'),
                        'bank_name': app['bank_name'],
                        'source': 'Google Play'
                    })

                logging.info(f"✅ Saved {len(results)} reviews for {app['bank_name']}")

            except Exception as e:
                logging.error(f"Error occurred for {app['bank_name']}: {e}")

    print(f"Data saved to {filename}")
