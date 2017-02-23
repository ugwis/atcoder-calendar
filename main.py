#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

check_url = "https://atcoder.jp/contest"

r = requests.get(check_url)
soup = BeautifulSoup(r.text.encode(r.encoding),"html.parser")
contests = soup.find_all("table")[2].find_all("tr")
for contest in contests:
    tds = contest.find_all("td")
    if len(tds) < 3:
        continue
    date = tds[0].a.renderContents()
    name = tds[1].a.renderContents()
    time = tds[2].renderContents()
    print(date)
    print(name)
    print(time)
