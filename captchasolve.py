from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytesseract, os, sys, time
try:
    from PIL import Image
except ImportError:
    import Image

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
b = webdriver.Chrome('/root/Desktop/Projects/CaptchaSolve/chromedriver', options=chrome_options)

b.get(sys.argv[1])

time.sleep(3) # wait for page to fully load

b.find_element_by_xpath(sys.argv[2]).screenshot('captcha.png')
print(pytesseract.image_to_string(Image.open('captcha.png')).replace(' ', ''))
os.remove('captcha.png')

# 1 - https://www.website.com/captcha
# 2 - //img[@alt="Captcha example"]
