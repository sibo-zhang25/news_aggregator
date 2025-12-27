# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 12:05:16 2025

@author: williamz
"""
from newsapi import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException
from article import Article

def getenews(api_key):
    ## require an API key from NewsAPI at
    ## https://newsapi.org/docs/authentication
    clipping = []
    api=NewsApiClient(api_key=api_key)
    try:
        query = api.get_top_headlines(page_size=50)
        ## 50 is an arbitrary number to balance between querying speed
        ## and chance of obtaining at least ten articles
        clipping = query['articles'][:10]
    
    except NewsAPIException as err:
        code  = err.get_code()
        msg = err.get_message()
        print(f'Bad request: {code}\n{msg}')
        return clipping
    
    articles = []
    for article in clipping:
        article_instance = _toArticle(article['title'],article['author'],\
                   article['publishedAt'],article['url'],\
                   article['source']['name'],article['content'])
        articles.append(article_instance)

    return articles

def _toArticle(title,author,date,url,source,content):
    ## helper func to store information in an Article instance
    ## all vars are str objects according to API
    ## https://newsapi.org/docs/endpoints/top-headlines
    title_default = ''
    author_default = ''
    date_default = ''
    url_default = ''
    source_default = ''
    content_default = ''

    if not isinstance(title,str):
        title = title_default
    if not isinstance(author,str):
        author = author_default
    if not isinstance(date,str):
        date = date_default
    if not isinstance(url,str):
        url = url_default
    if not isinstance(source,str):
        source = source_default
    if not isinstance(content,str):
        content = content_default
    
    return Article(title,author,date,url,source,content)
    


















