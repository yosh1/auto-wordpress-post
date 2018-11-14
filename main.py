from selenium import webdriver #seleniumのimport
import time
import requests

url = ‘http://weather.livedoor.com/forecast/webservice/json/v1’ 
payload = {‘city’:’130010′} 
tenki_data = requests.get(url, params=payload).json()


browser = webdriver.PhantomJS() 
loginURL = "http://example.com/wp/wp-login.php" #yoursite.comにはあなたのサイトのアドレスを書いてください
browser.get(loginURL)
time.sleep(3)
print(browser.title) # "あなたのサイト名 ‹ ログイン"と表示される

#ログイン

username = ""　#ユーザー名を入れてください
password = "" #パスワードを入れてください

browser.find_element_by_css_selector("#user_login").send_keys(username)
browser.find_element_by_xpath("//*[@id='user_pass']").send_keys(password)
browser.find_element_by_css_selector("#wp-submit").click()
time.sleep(3) # waiting for sign in 

print(browser.title) #"ダッシュボード ‹ あなたのサイト名 — WordPress"と表示される

#投稿
browser.get("http://yoursite.com/wp/wp-admin/post-new.php")
time.sleep(3) # waiting for sign in 
print(browser.title) #"新規投稿を追加 ‹ あなたのサイト名 — WordPress"と表示される

location = tenki_data[‘title’]
date = tenki_data[‘forecasts’][0][‘date’]
forecasts = (tenki_data[‘forecasts’][0][‘telop’] 
temp_max = [‘forecasts’][0][‘temperature’][‘max’][‘celsius’]
info_time = print(tenki_data[‘publicTime’]

title = "今日の" + location
content = "今日の" + location + "は、<br>" + 
browser.find_element_by_css_selector("#title").send_keys(title)
browser.find_element_by_css_selector("#content_ifr").send_keys(content)
browser.find_element_by_css_selector("#save-post").click
time.sleep(3) #waiting for post
