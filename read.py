from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import traceback
import string


creds = open('typeracer.creds', 'r')
user = string.strip(creds.readline())
pw = string.strip(creds.readline())

def main():
    driver = webdriver.Chrome()
    driver.get("http://play.typeracer.com/")

    try:
        
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'gwt-Anchor'))
        )
        element.send_keys(Keys.CONTROL, Keys.ALT, "L")
        # drop down for sign-in
        
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'gwt-TextBox'))
        )
        element.send_keys(user)
        
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'gwt-PasswordTextBox'))
        )
        element.send_keys(pw, Keys.RETURN)
        # username and pw
        
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'gwt-Anchor'))
        )
        element.send_keys(Keys.CONTROL, Keys.ALT, "I")
        # start new race
            
            
        while True:    
            element = WebDriverWait(driver,20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'inputPanel'))
            )
            
            # read the words in buffer
            print('read words')
            print(element)
            words = []
            
            buffer = element.text
            words = buffer.split(' ')
            
            while len(words) <= 1:
                element = WebDriverWait(driver,20).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'inputPanel'))
                )
                print('read words')
                buffer = element.text
                words = buffer.split(' ')
            
            print(words)
            
            element = WebDriverWait(driver,30).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'txtInput'))
            )
            print('input is clickable')
            element.send_keys(words[0])
            length = len(words)
            
            # write the words into text input box
            for x in range(1, length):
                if '\n' in words[x]:
                    words[x] = string.strip(words[x])
                    element.send_keys(' ', words[x])
                    break
                else:
                    element.send_keys(' ', words[x])
                    time.sleep(0.5)
            # element.send_keys(Keys.RETURN)
                    
            element = WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'raceAgainLink'))
            )
            
            element.send_keys(Keys.RETURN)
            print('clicked raceagain')

    except Exception:
        print(traceback.format_exc())

if __name__=="__main__":
    main()