from selenium import webdriver
import time
import urllib.parse
import requests
import json
import threading
def login(driver, username, password):
    # https://soundeo.com/
    driver.get("https://soundeo.com/")
    driver.find_element_by_xpath('//*[@id="top-menu-account"]/a').click()
    time.sleep(1)
    username_box = driver.find_element_by_xpath('//*[@id="UserLogin"]')
    username_box.send_keys(username)
    password_box = driver.find_element_by_xpath('//*[@id="UserPassword"]')
    password_box.send_keys(password)
    login_btn = driver.find_element_by_xpath('//*[@id="UserLogoregForm"]/div[5]/button')
    login_btn.click()
    time.sleep(1)
def get_creds():
    with open("config.json") as json_data:
        d = json.load(json_data)
        json_data.close()
        return d
def main():
    options = webdriver.ChromeOptions()
    prefs = {'prompt_for_download ': True}
    options.add_experimental_option("prefs", prefs)
    # options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    d = get_creds()
    login(driver, d["username"], d["password"])
    query=""
    while not query == "q":
        try:
                query=input("search (type q and enter to quit): ")
                if (query == "q"):
                        break
                query=query.strip(' ')
                print("Processing %s" % (query))
                # driver.get("https://soundeo.com/search?q="+query)
                driver.get(query)
                time.sleep(1.5)
                download_links = driver.find_elements_by_class_name("track-download-lnk")
                if (len(download_links) > 0):
                        download_links[0].click()
                        time.sleep(1.5)
                        '''
                        files = driver.find_elements_by_class_name('info')
                        print("Downloading  "+files[0].text+" to downloads folder")
                        frame = driver.find_element_by_id("iDownload")
                        download_url = frame.get_attribute('src')
                        r = requests.get(download_url)
                        open("./downloads/"+files[0].text+".mp3", 'wb').write(r.content)     
                        '''
        except:
                continue
    while True:
        time.sleep(1)
main()
