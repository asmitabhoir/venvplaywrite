import re
from playwright.sync_api import  sync_playwright


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False,slow_mo=2000)#to launch chrom
    page=browser.new_page()
    page.goto("https://www.google.co.in/")
    page.screenshot(path="playimg.png")
