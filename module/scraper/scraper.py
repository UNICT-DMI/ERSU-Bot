""""scraper module"""
from datetime import datetime as time
import locale
from bs4 import BeautifulSoup
import requests
import yaml
from yaml.loader import SafeLoader

with open('config/settings.yaml', 'r', encoding="UTF-8") as file:
    data = yaml.load(file, Loader=SafeLoader)

def get_html(url):
    response = requests.get(url, timeout=10)
    return response.text

def find_info(articles_list: list, article_number: int):
    #finds all the info of an article
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
    else:
        content_article = None

    return title_article , time_article, link_article, tag_article, content_article

def check_db(title_article: str ,time_article: str):
    print(title_article, "\n" ,time_article)
    #if title not present inside table return true


def publish_article():
    print("prova")

def find_tester() -> None:
    for i in range(15):
        article_info=find_info(articles, i)
        print(article_info)
        print("article: ", i)
        print("\n")

url_ersu = data['url_ersu']
url_html = get_html(url_ersu)
date = time.now()
locale.setlocale(locale.LC_TIME, "it_IT.UTF-8") #converts the date in to another lang
date_formatted = date.strftime("%-d %B %Y") #formats date

soup = BeautifulSoup(url_html, 'html.parser')
articles = soup.find_all('article')
last_articles = find_info(articles,0)
j=0

while True:
    j = j + 1
    tms_article = last_articles[1]
    title = last_articles[0]
    last_articles = find_info(articles,j)

    if  tms_article != date_formatted:
        print("esco")
        j=0
        break

    if check_db(title,tms_article):
        publish_article()
