""""scraper module"""
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
    last_article = articles_list[article_number]
    href_article = last_article.find_all('a',href=True, title=True)
    title_article = href_article[1].get_text()
    div_article = last_article.find('div', {'class' : 'slide-content'}).find('div',{'class' : 'slide-meta' })
    link_article = last_article.find('a')
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
    #you can use the code below to check if the data scraped are right
    #print(title_article, "\n", time_article, "\n", link_article, "\n" , tag_article, "\n", content_article, "\n" )

url_ersu = data['url_ersu']
url_html = get_html(url_ersu)

soup = BeautifulSoup(url_html, 'html.parser')
articles = soup.find_all('article') #it gives a list of all the article tags

for i in range(15):
    article_info=find_info(articles, i)
    print(article_info)
    print("article: ", i)
    print("\n")
    