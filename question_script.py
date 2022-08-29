from cgitb import text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

# Location of chromedriver
# This can be downloaded at https://chromedriver.chromium.org/downloads
PATH = ""

# The targeted website
website = ""

SLEEP_TIME = 5

# This process can be modified to target the correct placement
# More information at https://www.selenium.dev/documentation/webdriver/elements/locators/
def process(driver):
	driver.get(website)
	icon = driver.find_element(By.CLASS_NAME, "modal_trigger")
	icon.click()
	time.sleep(SLEEP_TIME)
	textArea = driver.find_element(By.TAG_NAME, "textarea")
	time.sleep(SLEEP_TIME)
	return textArea

def sendQuestions(textArea, questions, amount):
	questionsSize = len(questions)
	if questionsSize < amount:
		amount = questionsSize
	for x in range(0, amount):
		textArea.send_keys(questions[x])
		textArea.send_keys(Keys.RETURN)
		time.sleep(SLEEP_TIME)

def repeatedProcess(questions, questionAmount, repeatedProcessAmount):
	for x in range(0, repeatedProcessAmount):
		driver = webdriver.Chrome(PATH)
		textArea = process(driver)
		sendQuestions(textArea, questions, questionAmount)
		driver.quit()
		time.sleep(SLEEP_TIME)

if __name__ == "__main__":
	questions = [
		"hi",
		"english?",
		"Im not so sure what I should do",
		"could you help me"
	]
	random.shuffle(questions)
	repeatedProcessAmount = int(input("How many times this process should be repeated "))
	questionAmount = int(input("How many questions should be asked each process: "))
	repeatedProcess(questions, questionAmount, repeatedProcessAmount)
