""""scraper module"""
from datetime import datetime as time
import locale
import sqlite3
from bs4 import BeautifulSoup
import requests
import yaml
from yaml.loader import SafeLoader
from telegram.ext import CallbackContext
from telegram import ParseMode

with open('config/settings.yaml', 'r', encoding="UTF-8") as file:
    data = yaml.load(file, Loader=SafeLoader)

def get_html(url: str) -> str:
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
        content_article = content_article.find('p').text

    return title_article, time_article, link_article, tag_article, content_article

def connect_db() -> sqlite3.Connection:
    try:
        db_connect = sqlite3.connect("data/ERSU_DB.db")
        db_connect.text_factory = str
        # print("connected to db")

    except sqlite3.Error as error:
        print("failed to connect ", error)

    return db_connect

def add_to_db(title: str, article_time: str, cursor: sqlite3.Cursor , connect: sqlite3.Connection ) -> None:
    db_insert = """INSERT INTO Articles (Title, Time) VALUES (?, ?);"""
    db_data = (title, article_time)
    cursor.execute(db_insert, db_data)
    connect.commit()
    cursor.close()
    # print("added article and pub \n")
    # print(title, article_time)

def scrape_table(list_of_articles: list, time_stm: str, context: CallbackContext) -> None:
    #connects to db and takes the value of the last row added to the db
    last_article = find_info(list_of_articles,0)
    counter = 0

    try:
        db_connect = connect_db()
        db_cursor = db_connect.cursor()
        db_fetch = """SELECT title FROM Articles ORDER BY ROWID DESC LIMIT 10;"""
        db_cursor.execute(db_fetch)
        list_added_article = [r[0] for r in db_cursor.fetchall()]

        # if db is empty automatically adds the last article
        if list_added_article == []:
            add_to_db(last_article[0], last_article[1], db_cursor, db_connect)
            publish_article(last_article, context)

        # checks for the articles that have the current date
        while True:
            if time_stm == find_info(list_of_articles, counter)[2]:
                counter += 1
            else:
                break

        # verify that the articles are not already published
        for i in range(counter):
            article_to_publish = find_info(list_of_articles, i)
            if article_to_publish[0] != list_added_article[i]:
                add_to_db(article_to_publish[0], article_to_publish[1], db_cursor, db_connect)
                publish_article(article_to_publish, context)

    finally:
        if db_connect:
            db_connect.close()

def publish_article(latest_article: tuple, context: CallbackContext) -> None:
    [article_title, article_time, article_link, article_tag, article_content] = latest_article
    # print(article_title ,article_time , article_link , article_tag , article_content)

    message_content = f"<b>[{article_tag}]</b>"
    message_content += "\n"
    message_content += f'<a href="{article_link}">{article_link}</a>'
    message_content += "\n\n"
    message_content += f"<b>{article_title}</b>\n{article_content}"

    context.bot.send_message(chat_id=data['news_channel'], text=message_content, parse_mode=ParseMode.HTML)


def scrape_news(context: CallbackContext) -> None:
    url_ersu = data['url_ersu']
    url_html = get_html(url_ersu)
    date = time.now()
    locale.setlocale(locale.LC_TIME, "it_IT.UTF-8") #converts the date into another lang
    date_formatted = date.strftime("%-d %B %Y") #formats date
    soup = BeautifulSoup(url_html, 'html.parser')
    articles = soup.find_all('article')
    scrape_table(articles, date_formatted, context)
