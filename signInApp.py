import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import random

# 帳號密碼
username = "username"
password = "password"

# 全局變量 driver
scheduler = BackgroundScheduler(timezone="Asia/Shanghai")
global driver
driver = webdriver.Chrome()



def Accountsigning():
    driver.get("https://my.ntu.edu.tw/attend/ssi.aspx?type=login")
    box_account = driver.find_element(By.XPATH, '//*[@id="myTable"]/td/input')
    box_account.send_keys(username)

    box_password = driver.find_element(By.XPATH, '//*[@id="myTable2"]/td/input')
    box_password.send_keys(password)

    button_login_account = driver.find_element(By.NAME, "Submit")
    button_login_account.click()
    

def signIn():
    Accountsigning()
    time.sleep(1)  # 等待頁面加載
    # 到達指定時間後進行簽到操作
    box_signIn = driver.find_element(By.XPATH, '//*[@id="btSign"]')
    driver.execute_script("arguments[0].click();", box_signIn)
    print("簽到時間：", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(10)

def startJobs():
   
    random_min = random.randint(0, 10)
    random_sec = random.randint(0, 59)
    
    # 設定簽到時間為當天的 8點的隨機分鐘和秒數
    sign_in_time = datetime.datetime.now().replace(hour=8, minute=random_min, second=random_sec)

    time_to_wait_sign_in = (sign_in_time - datetime.datetime.now()).total_seconds()
    if time_to_wait_sign_in > 0:
        time.sleep(time_to_wait_sign_in)
    signIn()
    
scheduler.add_job(startJobs, 'cron', day_of_week='0-4', hour=7, minute=59)
scheduler.start()   
print("Schedule started...")
while True:
    time.sleep(60)
    print("程式執行中......現在時間：", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) 