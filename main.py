from selenium import webdriver #seleniumのimport
import time

browser = webdriver.PhantomJS() 
loginURL = "http://yoursite.com/wp/wp-login.php" #yoursite.comにはあなたのサイトのアドレスを書いてください
browser.get(loginURL)
time.sleep(3)
print(browser.title) # "あなたのサイト名 ‹ ログイン"と表示される

#ログイン

username = ""　#あなたのユーザー名を入れてください
password = "" #あなたのパスワードを入れてください

browser.find_element_by_css_selector("#user_login").send_keys(username)
browser.find_element_by_xpath("//*[@id='user_pass']").send_keys(password)
browser.find_element_by_css_selector("#wp-submit").click()
time.sleep(3) # waiting for sign in 

print(browser.title) #"ダッシュボード ‹ あなたのサイト名 — WordPress"と表示される

#投稿
browser.get("http://yoursite.com/wp/wp-admin/post-new.php")
time.sleep(3) # waiting for sign in 
print(browser.title) #"新規投稿を追加 ‹ あなたのサイト名 — WordPress"と表示される

title = "Test"
content = "test post"
browser.find_element_by_css_selector("#title").send_keys(title)
browser.find_element_by_css_selector("#content_ifr").send_keys(content)
browser.find_element_by_css_selector("#save-post").click
time.sleep(3) #waiting for post
