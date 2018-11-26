from selenium import webdriver
import time
import urllib.parse
import requests
import json
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
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    d = get_creds()
    login(driver, d["username"], d["password"])
    query=""
    while not query == "q":
        query=input("search (type q and enter to quit): ")
        query=urllib.parse.quote_plus(query)
        driver.get("https://soundeo.com/search?q="+query)
        time.sleep(1)
        # track-download-lnk    print(title.text)
        download_links = driver.find_elements_by_class_name("track-download-lnk")
        if (len(download_links) > 0):
                download_links[0].click()
                time.sleep(1)
        title = driver.find_element_by_xpath('/html/body/section[1]/div/div[2]/div[1]/a')
        print("Downloading "+title.text+"...")
        frame = driver.find_element_by_id("iDownload")
        download_url = frame.get_attribute('src')
        r = requests.get(download_url)
        open("/downloads/"+title.text+".mp3", 'wb').write(r.content)
        
main()
