# encoding=utf8
import sys, os, selenium
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random, time, csv, datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from openpyxl.styles import Color, PatternFill, Font, Border
import openpyxl
import locale
locale.setlocale(locale.LC_ALL, '')
from pathlib import Path

userName = os.getenv('USEREMAIL','')
passWord = os.getenv('PASSWORD','')
#print(userName,passWord)
def time_sleep(type):
    if type == 1:
        sleeptime = random.randrange(10,100)/100
    elif type == 2:
        sleeptime = random.randrange(70, 200)/100
    elif type == 3:
        sleeptime = random.randrange(100, 300)/100
    elif type == 4:
        sleeptime = random.randrange(150, 400)/100
    elif type == 5:
        sleeptime = random.randrange(200, 500)/100
    elif type == 6:
        sleeptime = random.randrange(500, 800)/100
    elif type == 7:
        sleeptime = random.randrange(800, 1500)/100
    elif type == 401:
        sleeptime = random.randrange(60, 100)
    time.sleep(sleeptime)


def get_selenium(url, count=0):
  
    options = Options()
    if os.name == "nt":
        #options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)
      
    else:
        #options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
      
    driver.get(url)
    driver.implicitly_wait(30)
    time_sleep(1)

    return driver
def login(url):
    driver = get_selenium(url)
    # driver.find_element_by_class_name("agree-button").click()
    driver.find_element_by_id("current-email").send_keys("marcinbalcerzak6@wp.pl")
    driver.find_element_by_id("current-password").send_keys("malak666")
    driver.find_element_by_css_selector(".css-5mruo-BaseStyles").click()
    time_sleep(3)

    # driver.find_element_by_id("se_userLogin").click()
    time.sleep(5)
    return driver

def processing_data(url):
    driver = login(url)

    #Get data from CSV
    with open('input.csv', 'r') as csvfile:
        rows = csv.reader(csvfile, delimiter='\t')
        i = 0 
        # for (row, index) in rows:  # how to loop with index in python for
        for row in rows:
            if i == 0:
                i +=1
                continue
            else:
                arr = row[0].split(",")
                #return the first state.
                driver.find_element_by_id("mainCategorySelect").click() 
                driver.find_element_by_xpath("//*[@id='mainCategorySelect']/option[6]").click()
                time_sleep(2)
                driver.find_element_by_xpath("//*[@id='subCategorySelect']/option[3]").click()
                time_sleep(2)
               
                ####Input Marka
                driver.find_element_by_xpath("//*[@id='newOffer']/div[2]/main/fieldset[1]/div/div[2]/span/span[1]/span").click()
                # driver.find_element_by_xpath("//*[@id='newOffer']/div[2]/main/fieldset[1]/div/div[1]/span/span[1]/span").click()
                time_sleep(2)
             
                elem1 = driver.find_element_by_xpath(f"//ul[@id='select2-param683-results']/li[contains(text(), '{arr[0]}')]")
                driver.execute_script("arguments[0].scrollIntoView(true);", elem1)
                WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, f"//ul[@id='select2-param683-results']/li[contains(text(), '{arr[0]}')]"))).click()
               
                # brandPath = "//ul[@id='select2-param683-results']/li[text()='{}']"
                # driver.find_element_by_xpath(brandPath.format(arr[0])).click()
                time_sleep(2)
                print("Folder " + arr[4]+" is processing.")

                ####Input model
                driver.find_element_by_id("param3").send_keys(arr[1])
                time_sleep(2)
                
                ####Input Rok
                driver.find_element_by_xpath("//*[@id='newOffer']/div[2]/main/fieldset[1]/div/div[4]/span/span[1]/span").click()
                
                
                # driver.find_element_by_xpath("//*[@id='newOffer']/div[2]/main/fieldset[1]/div/div[3]/span/span[1]/span").click()
                time_sleep(3)
                # brandPath = "//ul[@id='select2-param11-results']/li[text()='{}']"
                # driver.find_element_by_xpath(brandPath.format(arr[2])).click()
               
                elem = driver.find_element_by_xpath(f"//ul[@id='select2-param11-results']/li[contains(text(), {arr[2]})]")
                driver.execute_script("arguments[0].scrollIntoView(true);", elem)
                WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, f"//ul[@id='select2-param11-results']/li[contains(text(), {arr[2]})]"))).click()
              
               
                time_sleep(3)

                ####Input Radio
                driver.find_element_by_xpath("//*[@id='newOffer']/div[2]/main/fieldset[2]/div/div/label[5]").click()
                #driver.find_element_by_xpath("//div[@class='field--features']/label[text()='Radio']").click()
                time_sleep(1)
                ####Input Price
                driver.find_element_by_xpath("//*[@id='newOffer']/div[2]/main/fieldset[9]/div/div/div/div[1]/input[2]").send_keys(arr[3])
              
                time_sleep(1)
                
                ####Input Image
                imagePath = "D://Work//Koparko-Ladowarki//pictures//{}/a.jpg"
                #print (imagePath.format(arr[4]))
                driver.find_element_by_xpath('//input[@type="file"]').send_keys(imagePath.format(arr[4]))
                time_sleep(6)

                #step 10
                driver.find_element_by_id("save").click()
                time_sleep(3)

                #click checkbox
                driver.find_element_by_xpath("//*[@id='multipay']/li[1]/div/div/ul/div/li[1]/ul/li[1]").click()
                driver.find_element_by_xpath("//*[@id='multipay']/li[1]/div/div/ul/div/li[1]/ul/li[2]").click()
                driver.find_element_by_xpath("//*[@id='multipay']/li[1]/div/div/ul/div/li[2]").click()
                time_sleep(2)
                #step 11
                # driver.find_element_by_id("submit-contact").click()
                stepp = driver.find_element_by_id("submit-contact")
                driver.execute_script("arguments[0].scrollIntoView(true);", stepp)
                WebDriverWait(driver , 5).until(ec.element_to_be_clickable((By.ID,"submit-contact"))).click()
                
                
                time_sleep(3)
                driver.find_element_by_xpath("//*[@id='siteWrap']/header/div[2]/div/a").click()  
                time_sleep(2)
                driver.find_element_by_xpath("//*[@id='siteWrap']/section/div/div/div/ul/li[1]/a").click()
                time_sleep(3)
                
               
    driver.quit()
    

if __name__ == '__main__':
    url = "https://www.otomoto.pl/maszyny-budowlane/koparko-ladowarki/nowe-ogloszenie/"
    processing_data(url)
    print("________THE END_________")

        