# CaptchaSolve
A simple Python script to solve text captchas using both OCR and Selenium.

### Usage
The script takes two inputs: the website URL of the captcha and the XPATH selector to gain control of the captcha element.
<br /><br />
The example below gets the captcha element by targeting the `alt` attribute.
<br />
`python3 captchasolve.py https://website.com/login '//img[@alt="Captcha Verification"]'`

### How it works
It gains control of the captcha element and then screenshots it - saving it locally; avoiding refreshing the page and having a new image generared. The image file is then scanned for text using an OCR library. The *suspected* captcha text is outputted to your terminal.

### Expansion
As the script incoorportates the use of Selenium, you can then use this script to bypass captchas across a range of sites that use text captchas - given that the OCR functions correctly towards the specific captcha.

### Dependencies
* Selenium - and the chromedriver it uses.
* PyTesseract (OCR library) - and its binaries.
