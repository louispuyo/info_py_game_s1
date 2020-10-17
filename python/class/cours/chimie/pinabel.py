#PINABEL

from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time 


#browser = webdriver.Firefox()#Chrome('./chromedriver.exe') 
YOUTUBER_HOME_PAGE_URL = "https://www.doctolib.fr/account/appointments/1868784635" 
PATIENCE_TIME = 60 
LOAD_MORE_BUTTON_XPATH = '/html/body/div[5]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/button' 

driver = webdriver.Chrome('./chromedriver.exe') 
driver.get(YOUTUBER_HOME_PAGE_URL) 

while True: 
    try: 
     loadMoreButton = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/button") 
     time.sleep(2) 
     loadMoreButton.click() 
     time.sleep(5) 
    except Exception as e: 
     print (e)                      
     break 
print ("Complete")
time.sleep(10) 
driver.quit() 