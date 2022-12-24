from selenium import  webdriver
from  selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import  ChromeDriverManager
from time import sleep
tarayici = webdriver.Chrome(ChromeDriverManager().install())



tarayici.get("https://i.pinimg.com/550x/f4/54/1f/f4541f6a1e8622cf935d69a5103f2bef.jpg")
sleep(3)

















