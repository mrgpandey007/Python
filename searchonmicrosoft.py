# Import required module
from selenium.webdriver.opera.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from time import sleep
# Driver Code
if __name__ == '__main__':
     
    # Instantiate the webdriver with the executable location of MS Edge
    # Provide the full location of the path to recognise correctly
    edgeBrowser = webdriver.Edge(r"msedgedriver.exe")
     
    # This is the step for maximizing browser window
    edgeBrowser.maximize_window()
     
    # Browser will get navigated to the given URL
    edgeBrowser.get('https://www.lambdatest.com')
    try:
        # We need to insert Email in order to proceed further. 
        # So it is given by using 'useremail'
        sampleElement = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'useremail')))
         
        # We can give a valid email address and since 
        # this page carries the email id alone, it just 
        # appends the email id at the end
        sampleElement.send_keys("gfg@lambdatest.com")
         
        # A click is happening to move to next page
        sampleElement.click()
         
        # A Submit button is searched to click and start 
        # free testing. Actually "testing_form" is the id 
        # of the form, which needs to get tested
        sampleElement2 = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 
                                        "#testing_form > div")))
         
        # Starting free testing on LambdaTest
        sampleElement2.click()
         
        # Just to show the set of actions happening, we can 
        # give sleep, you can change the values as per requirement
        sleep(20)
    except TimeoutException:
        print("Trying to find the given element but unfortunately no element is found")
    sleep(20)
    # Once all operations over, we can close browser too
    # edgeBrowser.close()