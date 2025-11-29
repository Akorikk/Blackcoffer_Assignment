import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
import os
import re
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')

input_df = pd.read_excel("Input.xlsx")


def load_stopwords():
    stopwords = set()
    stopword_dir = "StopWords"

    for file in os.listdir(stopword_dir):
        file_path = os.path.join(stopword_dir, file)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding="ISO-8859-1") as f:
                for line in f:
                    stopwords.add(line.strip().lower())
    return stopwords


STOPWORDS = load_stopwords()


def load_master_dictionary():
    positive = set()
    negative = set()

    for file in os.listdir("MasterDictionary"):
        file_path = os.path.join("MasterDictionary", file)

        if "positive" in file.lower():
            with open(file_path, "r", encoding="ISO-8859-1") as f:
                for line in f:
                    positive.add(line.strip().lower())

        if "negative" in file.lower():
            with open(file_path, "r", encoding="ISO-8859-1") as f:
                for line in f:
                    negative.add(line.strip().lower())

    return positive, negative


POSITIVE_DICT, NEGATIVE_DICT = load_master_dictionary()


def extract_article(url):
    """
    Extract title + article text from the URL using BeautifulSoup.
    """
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        title_tag = soup.find("h1")
        title = title_tag.get_text(strip=True) if title_tag else ""

        paragraphs = soup.find_all("p")
        article = " ".join(p.get_text(strip=True) for p in paragraphs)

        return title + "\n" + article

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""


for index, row in input_df.iterrows():
    url_id = row["URL_ID"]
    url = row["URL"]

    print(f"Scraping URL_ID {url_id} ...")

   
    article_text = extract_article(url)

   
    with open(f"Articles/{url_id}.txt", "w", encoding="utf-8") as f:
        f.write(article_text)

    print(f"Saved: Articles/{url_id}.txt")