""""scraper module"""
from datetime import datetime, timedelta
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


def find_info(article: any) -> tuple:

    # finds the info of an article
    href_article = article.find_all("a", href=True)

    if len(href_article) > 1:
        title_article = href_article[1].get_text()
    else:
        title_article = None

    link_article = article.find('a')
    link_article = link_article['href']

    time_article = None
    div_article = article.find("div", {"class": "sow-entry-meta"})
    if div_article is not None:
        time_el = div_article.find("time")
        if time_el is not None:
            time_article = div_article.find("time").get_text().strip()

    # find the tag of the article and content
    html_article = get_html(link_article)
    soup_article = BeautifulSoup(html_article, 'html.parser')
    tag_article = soup_article.find_all('a', {'rel': 'tag'})[-1]

    if tag_article is None:
        tag_article = soup_article.find_all(
            'a', {'rel': 'v:url'}, {'property': 'v:title'}, href=True)[-1].get_text()
    else:
        tag_article = soup_article.find_all('a', {'rel': 'tag'})[-1].get_text()

    content_article = soup_article.find("section", {"class": "entry-content"})
    if content_article is not None:
        paragraph = content_article.find('p')
        if paragraph:
            content_article = paragraph.text
        else:
            content_article = content_article.text

    return title_article, time_article, link_article, tag_article, content_article


def connect_db() -> sqlite3.Connection:
    try:
        db_connect = sqlite3.connect("data/ERSU_DB.db")
        db_connect.text_factory = str
        # print("connected to db")

    except sqlite3.Error as error:
        print("failed to connect ", error)

    return db_connect


def add_to_db(title: str, article_time: str, article_link: str, cursor: sqlite3.Cursor, connect: sqlite3.Connection) -> None:
    db_insert = "INSERT INTO Articles (Title, Time, URL) VALUES (?, ?, ?);"
    db_data = (title, article_time, article_link)
    cursor.execute(db_insert, db_data)
    connect.commit()
    # print("added article and pub \n")
    # print(title, article_time)


def get_interval_dates(interval_days: int) -> list[str]:
    dates = []

    for i in range(interval_days):
        date = datetime.now() - timedelta(days=i)
        date_formatted = date.strftime("%-d %B %Y")
        dates.append(date_formatted.lower())

    return dates


def get_recent_articles(list_of_articles: list) -> list:
    recent_articles = []
    dates = get_interval_dates(7)

    for article in list_of_articles:
        time_article = find_info(article)[1]
        if time_article and time_article.lower() in dates:
            recent_articles.append(article)

    return recent_articles


def scrape_table(list_of_articles: list, context: CallbackContext) -> None:
    # connects to db and takes the value of the last row added to the db
    try:
        db_connect = connect_db()
        db_cursor = db_connect.cursor()
        db_fetch = "SELECT title, URL FROM Articles ORDER BY ROWID DESC LIMIT 10;"
        db_cursor.execute(db_fetch)
        list_added_articles = [[r[0], r[1]] for r in db_cursor.fetchall()]

        recent_articles = get_recent_articles(list_of_articles)

        # verify that the articles are not already published
        for recent_article in recent_articles:
            already_published = False

            article_to_publish = find_info(recent_article)
            for added_article in list_added_articles:
                if article_to_publish[0] == added_article[0] or article_to_publish[2] == added_article[1]:
                    already_published = True
                    break

            if not already_published:
                add_to_db(
                    article_to_publish[0], article_to_publish[1], article_to_publish[2], db_cursor, db_connect)
                publish_article(article_to_publish, context)

    finally:
        if db_connect:
            db_connect.close()


def publish_article(latest_article: tuple, context: CallbackContext) -> None:
    [article_title, article_time, article_link,
        article_tag, article_content] = latest_article
    # print(article_title ,article_time , article_link , article_tag , article_content)

    message_content = f"<b>[{article_tag}]</b>"
    message_content += "\n"
    message_content += f'<a href="{article_link}">{article_link}</a>'
    message_content += "\n\n"
    message_content += f"<b>{article_title}</b>\n{article_content}"

    context.bot.send_message(
        chat_id=data['news_channel'], text=message_content, parse_mode=ParseMode.HTML)


def scrape_news(context: CallbackContext) -> None:
    # converts the date into another lang
    locale.setlocale(locale.LC_TIME, "it_IT.UTF-8")

    url_ersu = data['url_ersu']
    url_html = get_html(url_ersu)

    soup = BeautifulSoup(url_html, 'html.parser')
    articles = soup.find_all('article')
    articles.reverse()

    scrape_table(articles, context)
