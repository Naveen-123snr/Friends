import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@given(u'launch Firefox browser')
def step_impl(context):
    path = r"C:\Users\C NAVEEN\PycharmProjects\FRIENDS_SPRINT\drivers\geckodriver.exe"
    # path = r"C:\Users\C NAVEEN\PycharmProjects\capgemini_sprint2\drivers\chromedriver.exe"
    context.driver = webdriver.Firefox(executable_path=path)
    # context.driver.implicitly_wait(25)
    context.driver.get("https://www.facebook.com/")
    context.driver.maximize_window()
    time.sleep(3)
    context.driver.implicitly_wait(20)



@given(u'enter username "{username_}"')
def step_impl(context, username_):
    time.sleep(3)
    context.driver.find_element("xpath",'//input[@class="inputtext _55r1 _6luy"]').send_keys(username_)
    time.sleep(2)


@given(u'enter password "{pwd}"')
def step_impl(context, pwd):
    context.driver.find_element("xpath",'//input[@class="inputtext _55r1 _6luy _9npi"]').send_keys(pwd)



@then(u'click on login')
def step_impl(context):
    context.driver.find_element("xpath",'//div[@class ="_6ltg"]//button[@name="login"]').click()
    time.sleep(6)

@then(u'click on friends button')
def step_impl(context):
    context.driver.find_element("xpath",'(//a[@href="/friends/"])[1]').click()
    time.sleep(4)


@then(u'click on friend requests')
def step_impl(context):
    context.driver.find_element("xpath",'(//div[@aria-label="Friends"])[1]//span[text()="Friend requests"]').click()
    time.sleep(4)

@then(u'click on send requests')
def step_impl(context):
    context.driver.find_element("xpath",'//span[text()="View sent requests"]').click()
    time.sleep(4)

@then(u'click on cancel request')
def step_impl(context):
    context.driver.find_element("xpath",'//span[text()="Cancel Request"]').click()
    time.sleep(4)

@then(u'click on close button')
def step_impl(context):
    context.driver.find_element("xpath",'//div[@class="x92rtbv x10l6tqk x1tk7jg1 x1vjfegm"]').click()
    time.sleep(4)

@then(u'click on suggestion')
def step_impl(context):
    context.driver.find_element("xpath",'//span[text()="Suggestions"]').click()
    time.sleep(4)

@then(u'click on add friend')
def step_impl(context):
    context.driver.find_element("xpath",'(//span[text()="Add Friend"])[1]').click()
    time.sleep(4)

@then(u'click on remove friend')
def step_impl(context):
    context.driver.find_element("xpath",'(//span[text()="Remove"])[2]').click()
    time.sleep(4)

@then(u'click on all friends')
def step_impl(context):
    context.driver.find_element("xpath",'//span[text()="All Friends"]').click()
    time.sleep(4)

@then(u'click on birthday')
def step_impl(context):
    context.driver.find_element("xpath",'//span[text()="Birthdays"]').click()
    time.sleep(4)

@then(u'click on custom list')
def step_impl(context):
    context.driver.find_element("xpath",'//span[text()="Custom lists"]').click()
    time.sleep(4)

@then(u'click on close friend')
def step_impl(context):
    context.driver.find_element("xpath",'//span[text()="Close friends"]').click()
    time.sleep(4)

@then(u'click on notification settings')
def step_impl(context):
    context.driver.find_element("xpath",'//div[@class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 x14yjl9h xudhj91 x18nykt9 xww2gxu x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xl56j7k xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xc9qbxq x14qfxbe x1qhmfi1"]').click()
    time.sleep(4)

@then(u'click on notification dot')
def step_impl(context):
    context.driver.find_element("xpath",'//input[@class="x1i10hfl x9f619 xggy1nq x1s07b3s x1ypdohk x5yr21d xdj266r x11i5rnm xat24cr x1mh8g0r x1w3u9th x1a2a7pz xexx8yu x4uap5 x18d9i69 xkhd6sd x10l6tqk x17qophe x13vifvy xh8yej3"]').click()
