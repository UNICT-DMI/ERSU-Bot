""""scraper module"""
from datetime import datetime as time
import locale
import sqlite3
from bs4 import BeautifulSoup
import requests
import yaml
from yaml.loader import SafeLoader

with open('config/settings.yaml', 'r', encoding="UTF-8") as file:
    data = yaml.load(file, Loader=SafeLoader)

def get_html(url) -> str:
    response = requests.get(url, timeout=10)
    return response.text

def find_info(articles_list: list, article_number: int) -> tuple:
    #finds  the info of an article
    article = articles_list[article_number]
    href_article = article.find_all('a',href=True, title=True)
    title_article = href_article[1].get_text()
    div_article = article.find('div',{'class' : 'slide-meta' })
    link_article = article.find('a')
    link_article = link_article['href']
    if div_article is not None:
        time_article = div_article.find('time').get_text()
    else:
        time_article = None
    #find the tag of the article and content
    html_article = get_html(link_article)
    soup_article = BeautifulSoup(html_article, 'html.parser')
    tag_article = soup_article.find('a', {'rel' : 'tag' })

    if tag_article is None:
        tag_article = soup_article.find('a', {'rel' : 'v:url' }, {'property' : 'v:title'}, href=True).get_text()
    else:
        tag_article = soup_article.find('a', {'rel' : 'tag' }).get_text()

    content_article = soup_article.find('div', {'class' : 'entry-content'})
    if content_article is not None:
        content_article = content_article.find('p')

    return title_article , time_article, link_article, tag_article, content_article

def connect_db() -> any:
    try:
        db_connect = sqlite3.connect("data/ERSU_DB.db")
        print("connected to db")

    except sqlite3.Error as error:
        print("failed to connect ", error)

    return db_connect

def scrape_table(latest_article: list) -> None:
    #connects to db and takes the value of the last row added to the db
    try:
        db_connect = connect_db()
        db_cursor = db_connect.cursor()
        db_fetch = """SELECT *
                            FROM    Articles
                            WHERE   ROWID = (SELECT MAX(ROWID)  FROM Articles);"""
        db_cursor.execute(db_fetch)
        last_added_article = db_cursor.fetchone()
        print(last_added_article)

        #checks if the article is already published if not then it adds it to the db and publish it

        if  last_added_article is None or last_added_article[0] != latest_article[0]:
            db_insert = """INSERT INTO Articles
                            (Title, Time) 
                            VALUES (?, ?);"""
            db_data = (latest_article[0], latest_article[1])
            db_cursor.execute(db_insert, db_data)
            db_connect.commit()
            print("Python Variables inserted successfully into Articles table")
            db_cursor.close()
            publish_article(latest_article)

    finally:
        if db_connect:
            db_connect.close()
            print("The SQLite connection is closed")

def publish_article(latest_article: list) -> None:
    article_title = latest_article[0]
    article_time = latest_article[1]
    article_link = latest_article[2]
    article_tag = latest_article[3]
    article_content = latest_article[4]
    print(article_title ,article_time , article_link , article_tag , article_content)


def find_tester() -> None:
    for i in range(NUMBER_OF_ARTICLES):
        article_info=find_info(articles, i)
        print("article: ", i)
        print("\n")
        print(article_info)
        print("\n")

url_ersu = data['url_ersu']
url_html = get_html(url_ersu)
NUMBER_OF_ARTICLES = 15
date = time.now()
locale.setlocale(locale.LC_TIME, "it_IT.UTF-8") #converts the date in to another lang
date_formatted = date.strftime("%-d %B %Y") #formats date

soup = BeautifulSoup(url_html, 'html.parser')
articles = soup.find_all('article')
last_article = find_info(articles,0)
scrape_table(last_article)
