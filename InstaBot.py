from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import system

class InstagramBot():
  
  def __init__(self):

    self.driver = webdriver.Chrome("..\\drivers\\chromedriver_83.exe")

  def openInstagram(self):

    self.driver.get("https://instagram.com")

  def logIn(self, username, password):

    try:

      self.driver.find_element_by_xpath("//input[@name='username']")\
          .send_keys(username)
      sleep(1)

      self.driver.find_element_by_xpath("//input[@name='password']")\
          .send_keys(password)
      sleep(1)

      self.driver.find_element_by_xpath("//button[@type='submit']")\
          .click()
      sleep(3)

      self.driver.find_element_by_xpath("//button[contains(text(), 'Non ora')]")\
          .click()
      sleep(1)

      self.driver.find_element_by_xpath("//button[contains(text(), 'Non ora')]")\
          .click()
      sleep(1)

      print("<- Log-in succesfully complited.")

    except:

      self.driver.find_element_by_xpath("//input[@name='username']")\
          .send_keys(Keys.CONTROL, 'a')
      self.driver.find_element_by_xpath("//input[@name='username']")\
          .send_keys(Keys.BACKSPACE)
      sleep(1)

      self.driver.find_element_by_xpath("//input[@name='password']")\
          .send_keys(Keys.CONTROL, 'a')
      self.driver.find_element_by_xpath("//input[@name='password']")\
          .send_keys(Keys.BACKSPACE)
      sleep(1)

      print("<- Log-in informations are wrong.")


  def sendMessage(self, receiver, message):

    try:
      self.driver.find_element_by_xpath("//a[contains(@href,'/direct/inbox')]")\
            .click()
      sleep(3)

      self.driver.find_element_by_xpath(f"//div[contains(text(),'{receiver}')]")\
          .click()
      sleep(1)

      self.driver.find_element_by_xpath("//textarea[@placeholder='Scrivi un messaggio...']")\
          .send_keys(message)
      sleep(1)

      self.driver.find_element_by_xpath("//button[contains(text(), 'Invia')]")\
        .click()
      sleep(1)

      self.driver.find_element_by_xpath("//a[contains(@href,'/')]")\
            .click()
      sleep(3)

      print(f"<- Sent '{message}' to {receiver} succesfully.")

    except:

      print(f"<- Can not find {receiver}.")

    finally:

      self.driver.find_element_by_xpath("//a[@href='/']")\
          .click()
      sleep(3)


  def follow(self, username):

    try:

      self.driver.find_element_by_xpath("//a[contains(@href,'/explore')]")\
          .click()
      sleep(3)

      self.driver.find_element_by_xpath("//span[contains(text(),'Cerca')]")\
          .click()
      sleep(1)

      self.driver.find_element_by_xpath("//input[@placeholder='Cerca']")\
          .send_keys(username)
      sleep(3)

      self.driver.find_element_by_xpath(f"//span[contains(text(),'{username}')]")\
          .click()
      sleep(2)

      self.driver.find_element_by_xpath("//button[contains(text(),'Segui')]")\
          .click()
      sleep(1)

      try:
        self.driver.find_element_by_xpath("//input[@aria-label='Chiudi']")\
            .click()
        sleep(1)

      except: pass

      print(f"<- Profile '{username}' succesfully followed.")

    except:

      print("<- Username is not correct or you already follow this profile.")

    finally:

      self.driver.find_element_by_xpath("//a[@href='/']")\
          .click()
      sleep(3)

  def unfollow(self, username):

    try:

      self.driver.find_element_by_xpath("//a[contains(@href,'/explore')]")\
          .click()
      sleep(3)

      self.driver.find_element_by_xpath("//span[contains(text(),'Cerca')]")\
          .click()
      sleep(1)

      self.driver.find_element_by_xpath("//input[@placeholder='Cerca']")\
          .send_keys(username)
      sleep(3)

      self.driver.find_element_by_xpath(f"//span[contains(text(),'{username}')]")\
          .click()
      sleep(2)

      self.driver.find_element_by_xpath("//span[@aria-label='Segui già']")\
          .click()
      sleep(1)

      self.driver.find_element_by_xpath("//button[contains(text(),'Non seguire più')]")\
          .click()
      sleep(1)

      print(f"<- Profile '{username}' succesfully unfollowed.")

    except:

      print("<- Username is not correct.")

    finally:

      self.driver.find_element_by_xpath("//a[@href='/']")\
          .click()
      sleep(3)

  def getFollowerList(self):

    pass

  def getFollowedList(self):

    pass

  def searchProfile(self, username):

    profile = None

    self.driver.find_element_by_xpath("//a[contains(@href,'/explore')]")\
          .click()
    sleep(3)

    self.driver.find_element_by_xpath("//span[contains(text(),'Cerca')]")\
        .click()
    sleep(1)

    self.driver.find_element_by_xpath("//input[@placeholder='Cerca']")\
        .send_keys(username)
    sleep(3)

    try:

      profile = self.driver.find_element_by_xpath(f"//span[contains(text(),'{username}')]").text
      sleep(1)

      print(f"<- Searched: {username}\n<- Founded: {profile}")

    except:

      print(f"<- Nothing founded with '{username}'")

    finally:

      self.driver.find_element_by_xpath("//div[@class='aIYm8 coreSpriteSearchClear']")\
          .click()
      sleep(1)

      self.driver.find_element_by_xpath("//a[@href='/']")\
          .click()
      sleep(3)

      return profile

  def close(self):

    print("<- Exit.")

    self.driver.close()

    quit()


def cls():

  system("clear")


def help():
    
    print("""
bot.
    openInstagram() 
    logIn(username, password) 
    sendMessage(receiver, message)
    follow(username)
    unfollow(username)
    getFollowerList() # Not Working
    getFollowedList() # Not Working
    searchProfile(username)
    close()

cls() # Clear terminal
""")

bot = InstagramBot()