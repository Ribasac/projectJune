from selenium import webdriver

cD = webdriver.Chrome()

rNumber = "+918848219624"

cD.get("https://web.whatsapp.com/send/?phone="+rNumber)
