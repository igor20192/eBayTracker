import logging
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import schedule

logging.basicConfig(filename="ebay_tracker.log", level=logging.INFO)

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")


def get_ebay_data(keywords):
    """
    Retrieves data from eBay based on given keywords.

    Args:
        keywords (str): Keywords for searching items on eBay.

    Returns:
        pd.DataFrame: DataFrame containing item details (title, price, link).
    """
    url = f"https://www.ebay.com/sch/i.html?_nkw={keywords}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    items = []
    for item in soup.select(".s-item"):
        title = item.select_one(".s-item__title").text
        price = item.select_one(".s-item__price").text
        link = item.select_one(".s-item__link")["href"]
        items.append({"title": title, "price": price, "link": link})

    return pd.DataFrame(items)


def store_data(df, db_name="ebay_data.db"):
    """
    Stores data into a SQLite database.

    Args:
        df (pd.DataFrame): DataFrame containing item details.
        db_name (str, optional): Name of the database file. Default is "ebay_data.db".
    """
    conn = sqlite3.connect(db_name)
    df.to_sql("items", conn, if_exists="append", index=False)
    conn.close()


def job():
    """
    Executes the job of retrieving data from eBay and storing it into the database.
    """
    try:
        df = get_ebay_data(keywords)
        store_data(df)
        logging.info(f"Data successfully received and saved: {formatted_date}")
    except Exception as e:
        logging.exception(f"An error has occurred: {e}: {formatted_date}")


keywords = input("Enter keyword: ")
start_time = input("Start time (e.g., 10:00): ")
schedule.every().day.at(start_time).do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
