from os import error, path
import time
import pyautogui
from pyautogui import *
import pandas as pd
import bot_functions
import subprocess

def is_browser_open(): 

    """
    this function is used to check browser was open or not ... 
    """
    
    bot_functions.please_wait("./Screenshots/redirect.png")

def normalize_browser(website_name): 

    """
    This function is used to open the browser and normalize the browser, and check the browser open the webpage correctly or not ... 
    """

    if website_name == "instagram": 

        bot_functions.redirect_url("https://www.instagram.com/")
        time.sleep(1)
        bot_functions.please_wait("./Screenshots/Instagram/create.png")
        time.sleep(3)

        pyautogui.press('esc')
        pyautogui.press('esc')
        pyautogui.press('esc')
    
    elif website_name == "tiktok":


        bot_functions.redirect_url("https://www.tiktok.com/")
        time.sleep(1)
        bot_functions.please_wait("./Screenshots/TikTok/logo.png")
        time.sleep(3)

        pyautogui.press('esc')
        pyautogui.press('esc')
        pyautogui.press('esc')

    
    elif website_name == "facebook": 

        bot_functions.redirect_url("https://www.facebook.com/")
        time.sleep(1)
        bot_functions.please_wait("./Screenshots/Facebook/fb.png")
        time.sleep(3)

        pyautogui.press('esc')
        pyautogui.press('esc')


    elif website_name == "pinterest":

        bot_functions.redirect_url("https://www.pinterest.com/")
        time.sleep(1)
        bot_functions.please_wait("./Screenshots/Pinterest/dots.png")

        pyautogui.press('esc')
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('esc')
        pyautogui.press('esc')
        time.sleep(1)
    
    # elif website_name == "linkedin": 
    #     bot_functions.redirect_url("https://www.linkedin.com/") 
    #     time.sleep(1)
    #     bot_functions.please_wait("./Screenshots/Linkedin/all_activity.png") 

    #     pyautogui.press('esc')
    #     pyautogui.press('esc')
    #     pyautogui.press('esc')



def open_chrome():

    # Path to the chrome.exe
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    subprocess.Popen(chrome_path)

def close_browser():

    pyautogui.hotkey('ctrl','w')
    time.sleep(1)

# print("starts/_")
# time.sleep(4)
# # normalize_browser("pinterest")
# close_browser()
