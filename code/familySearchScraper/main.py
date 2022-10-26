import json


v_settings = None
with open('config.json', 'r') as read_json:
    v_settings = json.load(read_json)
    print(v_settings['edge_driver'])

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
  
# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded.
import time 
   
from selenium.webdriver.common.keys import Keys 
  
# Creating an instance webdriver
options = EdgeOptions()
options.use_chromium = True
options.add_argument('start-maximized')

# #Here you set the path of the profile ending with User Data not the profile folder
# options.add_argument("--user-data-dir=C:\\Users\\sesa443933\\AppData\\Local\\Microsoft\\Edge\\User Data"); 
# #Here you specify the actual profile folder    
# options.add_argument("profile-directory=Profile 1");
# options.binary_location = r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

browser = webdriver.Edge(v_settings['edge_driver'], options=options)
browser.get('https://www.familysearch.org/es/')

# closing the browser
# browser.quit()
browser.close()