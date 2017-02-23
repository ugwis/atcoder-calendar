#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
from datetime import datetime as dt
import cal
import re

check_url = "https://atcoder.jp/contest"

def regex(r,text):
    rec = re.compile(r)
    match = rec.search(text)
    if match is None:
        return None
    return match.group(1)

r = requests.get(check_url)
soup = BeautifulSoup(r.text.encode(r.encoding),"html.parser")
contests = soup.find_all("table")[2].find_all("tr")
for contest in contests:
    tds = contest.find_all("td")
    if len(tds) < 3:
        continue
    date = dt.strptime(tds[0].a.renderContents(), "%Y/%m/%d %H:%M")
    
    print(tds[1].a.get("href"))
    id = regex("https://(\w*).contest.atcoder.jp",tds[1].a.get('href'))
    name = tds[1].a.renderContents()
    time = tds[2].renderContents().split(":")
    start = date - datetime.timedelta(hours=9)
    end = date + datetime.timedelta(hours=int(time[0]), minutes=int(time[1])) - datetime.timedelta(hours=9)
    cal.add_event(id,name,start,end)
