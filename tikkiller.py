from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import subprocess
import pyautogui


def aftool(username):
    try:
        driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
        driver.get(f'https://www.tiktok.com/@{username}')
        time.sleep(5)
        driver.find_element('xpath', '/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/a/div/div[2]').click()
        pyautogui.hotkey('m')
        time.sleep(3)
        driver.find_element('xpath', '/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/button').click()
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get('https://tikmate.online/#google_vignette')
        time.sleep(5)
        driver.find_element('xpath', '//*[@id="url"]').click()
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        driver.find_element('xpath', '/html/body/main/div[1]/div/div/div/div/form/button/span').click()
        time.sleep(5)
        driver.find_element('xpath', '/html/body/main/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div/a/span/span').click()
        time.sleep(10)
        print('                     ')
        print('                     ')
        print('                     ')

        print(f'you have the latest video from {username} in your downloads folder')
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        pyautogui.hotkey('ctrl', 'f4')
        pyautogui.hotkey('ctrl', 'f4')
        pyautogui.hotkey('ctrl', 'f4')

    except:
        print('something went wrong')


username = input("Enter the username of the user (Example arifanxum) : ")
aftool(username)
