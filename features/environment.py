from selenium import webdriver
import os
import time
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser.maximize_window()
    context.browser.delete_all_cookies()
    context.browser.get("http://qa-assignment.oblakogroup.ru/board/:Klevtsov_Andrey-BBD")


def after_all(context):
    context.browser.quit()
