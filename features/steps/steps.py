from behave import *
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


@given(u'Create and check new task "{url}"')
def step_impl(context, url):
    context.browser.find_element_by_id("add_new_todo").click()
    print('Adding new task')
    time.sleep(2)
    category_list = Select(context.browser.find_element_by_id("select_category"))
    category_list.select_by_index(1)
    print('Chosen category "Работа"')
    time.sleep(2)
    context.browser.find_element_by_id("project_text").click()
    context.browser.find_element_by_id("project_text").send_keys('New task')
    print('Giving name to a new task')
    time.sleep(2)
    context.browser.find_element_by_id("submit_add_todo").click()
    context.browser.find_element_by_xpath('//body//form[4]')
    print('New task was created')
    time.sleep(2)


@given(u'Create an empty task "{url}"')
def step_impl(context, url):
    context.browser.find_element_by_id("add_new_todo").click()
    print('Adding new task')
    time.sleep(2)
    category_list = Select(context.browser.find_element_by_id("select_category"))
    category_list.select_by_index(1)
    print('Choose category "Работа')
    time.sleep(2)
    context.browser.find_element_by_id("project_text").click()
    print('Left field unfilled')
    time.sleep(2)
    context.browser.find_element_by_id("submit_add_todo").click()
    time.sleep(2)
    context.browser.find_element_by_xpath('//body//form[5]')
    print('Empty task can be created')


@given(u'Creating new category "{url}"')
def step_impl(context, url):
    context.browser.find_element_by_id("add_new_todo").click()
    print('Adding new task')
    time.sleep(2)
    category_list = Select(context.browser.find_element_by_id("select_category"))
    category_list.select_by_index(3)
    context.browser.find_element_by_id("project_title").click()
    context.browser.find_element_by_id("project_title").send_keys("Новая категория")
    print('Creating new category')
    time.sleep(2)
    context.browser.find_element_by_id("project_text").click()
    context.browser.find_element_by_id("project_text").send_keys("Новая задача")
    print('Giving name to a new task')
    time.sleep(2)
    context.browser.find_element_by_id("submit_add_todo").click()
    time.sleep(2)
    context.browser.find_element_by_xpath('//div[4]//div[1]//h2[1]')
    print('New category was created')


@given(u'Validating checkbox "{url}"')
def step_impl(context, url):
    context.browser.find_element_by_id("todo_check").click()
    time.sleep(1)
    context.browser.find_element_by_id("todo_check").click()
    print('Status of task is changeable')
    time.sleep(2)
