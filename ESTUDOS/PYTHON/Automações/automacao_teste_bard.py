from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Abrir o Word
driver = webdriver.Chrome()
driver.get("https://office.live.com/start/Word.aspx")

# Esperar o Word abrir
time.sleep(5)

# Selecionar a primeira célula
body = driver.find_element_by_tag_name('body')
body.send_keys(Keys.CONTROL + 'a')
body.send_keys(Keys.DELETE)

# Digitar o texto "Tese em Ciências da Computação" na primeira linha
body.send_keys('Tese em Ciências da Computação')
body.send_keys(Keys.ENTER)
