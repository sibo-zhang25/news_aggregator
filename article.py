# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 12:21:35 2025

@author: williamz
 
"""
import re

class Article:
    def __init__(self,title,author,date,url,source,content):
        
        ## all parameters must be of string type
        if  isinstance(title,str) and isinstance(author,str) \
            and isinstance(date,str) and isinstance(content,str) \
            and isinstance(url,str) and isinstance(source,str):
                pass
        else:
            raise TypeError('all parameters must be of string type')
            
        self._title=title
        self._author=author
        self._date=date
        self._link=url
        self._source=source
        self._content=content
        

    def __str__(self):
        ## produce a string that concatenate all information in the article
        seperator=' '
        result=seperator.join([self._title,
                               self._author,
                               self._date,
                               self._link,
                               self._source,
                               self._content])
        return result
    
    def __len__(self):
        ## calculate length of the content
        return len(self._content)
     
    def display(self):
        ## display the article in an easy-to-read fashion
        
        content=re.sub(r'\s', ' ', self._content)
        ## cleaning the main passage to get more sensible articles
        s = f'Title:{self._title}\nAuthor:{self._author}\n'\
            f'Published at {self._date} on {self._source}\n'\
            f'Content:{content}\n\nLink to the original news page: {self._link}'
        print(s)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
