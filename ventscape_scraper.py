import time
import os
import selenium
import pytesseract
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.ventscape.life/')

progress_btn = driver.find_element("xpath", "/html/body/div[1]/div[2]/div/div/div/div/div")
progress_btn.click()
with open('output.txt', 'w') as f:
    f.write("")

time.sleep(28)

for i in range(5):
    driver.save_screenshot('capture.png')
    img = Image.open('capture.png')
    width, height = img.size
    img = img.crop((0, 60, width, height - 50))

    result = pytesseract.image_to_string(img)
    result = result.replace("\n", " ")
    with open('output.txt', 'a') as f:
        f.write("\n" + result)

    time.sleep(10)
    os.remove("capture.png")
driver.quit()
