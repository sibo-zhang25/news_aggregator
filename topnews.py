# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 13:21:50 2025

@author: williamz
"""
import tkinter as tk
from tkinter import messagebox
from newsapi import NewsApiClient

class Topnews:
    ## GUI class to get top news with keyword input by the user
    ## display aggregate information for each news from search results
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x400') 
        self.root.title("Today's headline news")
        
        self.function_label = tk.Label(self.root, text="search and get latest news")
        self.function_label.pack(pady=10)
        
        self.question_label = tk.Label(self.root, text="Please enter your search keywords:")
        self.question_label.pack(pady=10)
        self.question_entry = tk.Entry(self.root)
        self.question_entry.pack(pady=5)
        
        self.number_label = tk.Label(self.root, text="Number of query(default amount:10 ; maximum amount:100)")
        self.number_label.pack()
        self.number_entry = tk.Entry(self.root)
        self.number_entry.pack(pady=5)
        
        self.get_button = tk.Button(self.root, text="Get news!",command=self.get_news)
        self.get_button.pack(pady=10)
        
        self.root.mainloop()
        
    def get_news(self):
        
        question=self.question_entry.get()
        
        try:
            Input=int(self.number_entry.get())
            if Input>0 and Input<=100:
                display_amount=Input
            else:
                display_amount=10
        except:
            display_amount=10
        
        api_key='6adfdd5a094c46daa53ea3bbb74379a5'
        api=NewsApiClient(api_key=api_key)
        response=api.get_everything(q=question,sort_by='relevancy')
        news=response['articles'][:display_amount]
        queries=''
        for item in news:
            t=item['title']
            n=item['source']['name']
            time=item['publishedAt']
            r=f'{t}\n{n}\t{time}\n\n'
            queries+=r
        
        messagebox.showinfo(title="Search Result",message=queries)