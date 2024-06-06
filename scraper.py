from selenium import webdriver
from selenium.webdriver.common.by import By
from pymongo import MongoClient
from time import sleep
import time
import uuid
import requests

# MongoDB setup
client = MongoClient('mongodb+srv://ashishsharma0t:7Ci23JnVpbRUASeM@trends.qfdl1lb.mongodb.net/?retryWrites=true&w=majority&appName=trends')
db = client['twitter_trends']
collection = db['top_5_trends']

# ProxyMesh setup
# proxy_mesh_url = 'http://USERNAME:PASSWORD@us-il.proxymesh.com:31280'

# Unique ID
unique_id = str(uuid.uuid4())

# Twitter credentials
username = "s_ashish01"
password = "Ashish810@"

def fetch_trending_topics():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--proxy-server=%s' % proxy_mesh_url)
    driver = webdriver.Chrome()
    # driver.maximize_window()
    
    driver.get("https://twitter.com/login")
    
    # Login to Twitter
    sleep(4)
    driver.find_element(By.XPATH,"//input[@name='text']").send_keys(username)
    driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()

    sleep(4)
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password)
    driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]").click()
    
    sleep(4)
    # Fetch trending topics    
    driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[4]/div/section/div/div/div[8]/div/a").click()
    
    sleep(4)
    trends = driver.find_elements(By.XPATH,"//span[@dir='ltr']")
    top_5_trends = [trend.text for trend in trends[:5] if trend.text.strip()]

    
    
    # Record the IP address used
    ip_address = requests.get("http://api.ipify.org").text
    
    # Record the date and time of the end of the Selenium script
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    
    # Insert into MongoDB
    record = {
        "_id": unique_id,
        "trend1": top_5_trends[0],
        "trend2": top_5_trends[1],
        "trend3": top_5_trends[2],
        "trend4": top_5_trends[3],
        "trend5": top_5_trends[4],
        "end_time": end_time,
        "ip_address": ip_address
    }
    collection.insert_one(record)

    driver.close()

if __name__ == "__main__":
    fetch_trending_topics()





