from selenium import webdriver
driver = webdriver.Firefox()

driver.get("https://webkiosk.thapar.edu/index.jsp")
username = driver.find_element_by_name("MemberCode")
username.clear()
username.send_keys("your_username")

password = driver.find_element_by_name("Password")
password.clear()
password.send_keys("your_password")
driver.find_element_by_name("BTNSubmit").click()
driver.get("https://webkiosk.thapar.edu/StudentFiles/Exam/StudentEventMarksView.jsp")

el = driver.find_element_by_name('exam')
for option in el.find_elements_by_tag_name('option'):
    if option.text == '1819EVESEM':
        option.click()
        break
driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td/input").click()
