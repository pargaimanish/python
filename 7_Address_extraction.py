from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time
import os
import re
from selenium.webdriver import ActionChains


proxy_auth= '3c617fdc66b92fe43e6f__cr.de:9ca3640b1de7273f'
proxy_url= 'gw.dataimpulse.com:823'

options = webdriver.ChromeOptions()
options.add_argument('--headless')

options.add_argument(f'--proxy-server=http://{proxy_auth}@{proxy_url}')

driver = webdriver.Firefox()
driver.get("https://www.google.com/maps")

actions = ActionChains(driver)
try:
    accept_button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Accept all']")
    accept_button.click()
except NoSuchElementException:
    print("No GDPR requirements detected")

# Wait for the search box and enter query
search_box = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#searchboxinput"))
)
search_term = "restaurants Dharamkot"
search_box.send_keys(search_term)
search_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Search']")
search_button.click()


# Wait for business listings
business_items = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "Nv2PK.THOPZb.CpccDe"))
)
#Nv2PK THOPZb CpccDe 

#business_items = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "Nv2PK.THOPZb.CpccDe")))

#elementSelect = driver.find_elements(By.CLASS_NAME, "Nv2PK.THOPZb.CpccDe")
#print(elementSelect[0].get_attribute("outerHTML"))

divSideBar=driver.find_element(By.CSS_SELECTOR,f"div[aria-label='Results for {search_term}']")
keepScrolling=True
while(keepScrolling):
    divSideBar.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    divSideBar.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    html=driver.find_element(By.TAG_NAME, "html").get_attribute('outerHTML')
    
    if(html.find("You've reached the end of the list.")!=-1):
        keepScrolling=False
        
time.sleep(3)
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
elementSelect = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "Nv2PK.THOPZb.CpccDe")))


counter = 0
for i in elementSelect:
  counter+= 1
  
for eachElement in range(len(elementSelect)):  
   
    path = f"/Users/manishpargai/Documents/scrap/Dharamshala details"

    dir_list = os.listdir(path) 
    print("Files and directories in '", path, "' :") 

    error_text = ["/Users/manishpargai/Documents/scrap/error.txt"]
    
    st = elementSelect[eachElement]
    arrrr = st.find_element(By.CSS_SELECTOR, "a").get_dom_attribute("aria-label")
    ar= st.find_element(By.CSS_SELECTOR, "a").get_dom_attribute("aria-label").replace("/", " ").replace(".", " ").replace("|", " ")
    driver.implicitly_wait(5)
    # Using find_elements to avoid NoSuchElementException for 'span.UY7F9'
    selectingRcountss_list = st.find_elements(By.CSS_SELECTOR, "span.UY7F9")
    selectingRcountss = selectingRcountss_list[0] if selectingRcountss_list else None  # Initialize the variable outside
    if(selectingRcountss):
        selectingRcounts = selectingRcountss.text

    arr= st.find_element(By.CSS_SELECTOR, "span").get_attribute("aria-label")
    
    
    change_list = [] 
    for i in range(len(dir_list)):
      change= dir_list[i].replace(".html","").replace(".", "").replace("icloud", "")
      change_list.append(change)
                 
    if ar not in change_list and ar not in error_text :

      
      selectingRcount=int(selectingRcounts.strip("()").replace(",", ""))
      print(selectingRcounts)
      print(ar)
      arr
      driver.implicitly_wait(5)
      st.click()
      
      
      escaped_ar = re.escape(ar)
     
      
    

     
      
     





  
      Savinghtml=driver.find_element(By.TAG_NAME, "html").get_attribute('outerHTML')

  
      os.makedirs("Dharamshala details", exist_ok=True)
      file_path = os.path.join("Dharamshala details", f"{ar}.html")
      with open(file_path, 'a', encoding='utf-8') as f:
        f.write(Savinghtml)
        
    
    
   
 
#fin= driver.find_elements(By.CSS_SELECTOR, 'button[class="hh2c6 "]') 
#for int in range(7):
  
    #findrr= fin[int]
    #findrr.click()
        

print("Scraping completed.")
driver.quit()
