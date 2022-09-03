from selenium import webdriver

import time

options = webdriver.ChromeOptions() ;

prefs = {"download.default_directory" : "D:\\USER\\Documents\\GitHub\\Code\\Python\\Discord"};

options.add_experimental_option("prefs",prefs);

driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=options);

try:

    driver.get('https://www.browserstack.com/test-on-the-right-mobile-devices');

    downloadcsv= driver.find_element_by_css_selector('.icon-csv');

    gotit= driver.find_element_by_id('accept-cookie-notification');

    gotit.click();    

    downloadcsv.click();

    time.sleep(5)

    driver.close()

except:

     print("Invalid URL")