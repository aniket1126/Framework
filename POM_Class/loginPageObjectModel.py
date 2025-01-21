from selenium.webdriver.common.by import By
from selenium import webdriver

class login:
    emailID="email"
    passwdID="passwd"
    login_button='//*[@id="SubmitLogin"]'

#constructor
    def __init__(self,driver):
       self.driver=driver


 #Actions
    def setUserName(self,username):
        usertxt=self.driver.find_element(By.ID,self.emailID)
        usertxt.send_keys(username)

    def setUserPasswrd(self,password):
        userpasswrd=self.driver.find_element(By.ID,self.passwdID)
        userpasswrd.send_keys(password)

    def button(self):
        userbtn=self.driver.find_element(By.XPATH,self.login_button)
        userbtn.click()

