from selenium import webdriver
import time
from getpass import getpass


print('_____  _    ____ _____ ____   ___   ___  _  __   ____  ____   _   ___  ___   ____   ___ _____')
print('|  ___/ \  / ___| ____| __ ) / _ \ / _ \| |/ /  / ___||  _ \ / \  |  \/  |  | __ ) / _ \_   _|')   
print("| |_ / _ \| |   |  _| |  _ \| | | | | | | ' /   \___ \| |_) / _ \ | |\/| |  |  _ \| | | || |")
print('|  _/ ___ \ |___| |___| |_) | |_| | |_| | . \    ___) |  __/ ___ \| |  | |  | |_) | |_| || |')
print('|_|/_/   \_\____|_____|____/ \___/ \___/|_|\_\  |____/|_| /_/   \_\_|  |_|  |____/ \___/ |_|')
print("\n")

username = input("Enter in your username: ")
password = getpass("Enter your password: ")
friend = input("Enter your friend name to message: ")
message = input("Enter your message to your friend: ")
mah = webdriver.Chrome("PASTE YOUR WEBDRIVER PATH HERE") #Example ("E:\WebDrivers\chromedriver.exe")
mah.implicitly_wait(15)

mah.get('https://www.facebook.com/')
username_textbox = mah.find_element_by_name("email")
username_textbox.send_keys(username)

password_textbox = mah.find_element_by_name("pass")
password_textbox.send_keys(password)

time.sleep(2)

login = mah.find_element_by_name("login")     
login.click()
time.sleep(5)

msg = mah.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/span/div/div[1]")
msg.click()
time.sleep(3)

search = mah.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/div/label/input')
search.send_keys(friend)
time.sleep(5)

select = mah.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/ul/div[1]/li[1]")
select.click()

i=0
while i<= 1:

  enter = mah.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div")
  enter.send_keys(message)

  send = mah.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/span[2]/div")
  send.click()
