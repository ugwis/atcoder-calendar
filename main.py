#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
from datetime import datetime as dt

check_url = "https://atcoder.jp/contest"

r = requests.get(check_url)
soup = BeautifulSoup(r.text.encode(r.encoding),"html.parser")
contests = soup.find_all("table")[2].find_all("tr")
for contest in contests:
    tds = contest.find_all("td")
    if len(tds) < 3:
        continue
    date = dt.strptime(tds[0].a.renderContents(), "%Y/%m/%d %H:%M")
    name = tds[1].a.renderContents()
    time = tds[2].renderContents().split(":")
    start = date
    end = date + datetime.timedelta(hours=int(time[0]), minutes=int(time[1]))
    print(name)
    print(start)
    print(end)
