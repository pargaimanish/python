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
search_term = "restaurants bhagsu"
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
   
    path = f"/Users/manishpargai/Documents/scrap/Cafes Dharamshala"

    dir_list = os.listdir(path) 
    print("Files and directories in '", path, "' :") 

    error_text = ["/Users/manishpargai/Documents/scrap/error.txt"]
    
    st = elementSelect[eachElement]
    arrrr = st.find_element(By.CSS_SELECTOR, "a").get_dom_attribute("aria-label")
    ar= st.find_element(By.CSS_SELECTOR, "a").get_dom_attribute("aria-label").replace("/", " ").replace(".", " ").replace("|", " ")
    selectingRcounts= st.find_element(By.CSS_SELECTOR, "span.UY7F9").text
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
      
      rev = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, f'//button[@aria-label="Reviews for {arrrr}"]')))
     
      #rev.click()
      actions.move_to_element(rev)

      driver.execute_script("arguments[0].click();", rev)
      
      
      
      
      
      bbutton = driver.find_element(By.XPATH, f'//button[@aria-label="Reviews for {arrrr}"]')
      
      
      bbutton.click()
      
    

     
      
      revClick = driver.find_element(By.CSS_SELECTOR, f'button[aria-label="Reviews for {ar}"], button.hh2c6')
      time.sleep(10)
      #revClick.click()


      
      time.sleep(10)
      #rev.click()
      #time.sleep(10)
      
      ssort = WebDriverWait(driver, 10000).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Sort reviews' or @aria-label='Most relevant']"))
            )
      ssort.click()
      #button = driver.find_element(By.XPATH,  '//button[@aria-label="Sort reviews"]')
      #actions.move_to_element(button)
      #driver.execute_script("arguments[0].click();", button)
      
      #sortClick = driver.find_element(By.XPATH, f"//button[@aria-label='Sort reviews']")
      findnew =  WebDriverWait(driver, 10000).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="fxNQSd" and @data-index="1"]')))
      
      
      #findnew = driver.find_element(By.XPATH, '//div[@class="fxNQSd" and @data-index="1"]')
      #actions.move_to_element(findnew)
      #driver.implicitly_wait(3)
      #time.sleep(10)
      findnew.click()
  
      
      driver.implicitly_wait(10)
      if selectingRcount >= 200:
        sdivSideBar = WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='m6QErb DxyBCb kA9KIf dS8AEf XiKgde ' and @style='' and @tabindex='-1']")))
        print(selectingRcount)
        print("200")
        print(st)
        skeepScrolling = True
        while skeepScrolling:
           driver.implicitly_wait(2)
           actions.move_to_element(sdivSideBar)
           sdivSideBar.send_keys(Keys.PAGE_DOWN)
           driver.implicitly_wait(0.5)
           sdivSideBar.send_keys(Keys.PAGE_DOWN)
           driver.implicitly_wait(0.5)
           shtml = driver.find_element(By.TAG_NAME, "html").get_attribute('innerHTML')

           if (shtml.find("a year ago") != -1 or 
               shtml.find("2 years ago") != -1 or 
               shtml.find("3 years ago") != -1):
                 skeepScrolling = False

      elif 100 <= selectingRcount < 200:  # Added a condition
          sdivSideBar = WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='m6QErb DxyBCb kA9KIf dS8AEf XiKgde ' and @style='' and @tabindex='-1']")))

          print(selectingRcount)
          print("50")
          skeepScrolling = True
          while skeepScrolling:
            time.sleep(2)
            actions.move_to_element(sdivSideBar)
            sdivSideBar.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            sdivSideBar.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)
            shtml = driver.find_element(By.TAG_NAME, "html").get_attribute('innerHTML')

            if (shtml.find("6 months ago") != -1 or
                shtml.find("7 months ago") != -1 or
                shtml.find("8 months ago") != -1 or
                shtml.find("9 months ago") != -1 or
                shtml.find("10 months ago") != -1 or
                shtml.find("11 months ago") != -1 or
                shtml.find("2 years ago") != -1 or 
                shtml.find("3 years ago") != -1):
                 skeepScrolling = False
      elif 50 <= selectingRcount < 100:
          sdivSideBar = WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='m6QErb DxyBCb kA9KIf dS8AEf XiKgde ' and @style='' and @tabindex='-1']")))

          print(selectingRcount)
          print("new")
          skeepScrolling = True
          while skeepScrolling:
            time.sleep(2)
            actions.move_to_element(sdivSideBar)
            sdivSideBar.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            sdivSideBar.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)
            shtml = driver.find_element(By.TAG_NAME, "html").get_attribute('innerHTML')

            if (shtml.find("3 months ago") != -1 or
                shtml.find("7 months ago") != -1 or
                shtml.find("8 months ago") != -1 or
                shtml.find("9 months ago") != -1 or
                shtml.find("10 months ago") != -1 or
                shtml.find("11 months ago") != -1 or
                shtml.find("2 years ago") != -1 or 
                shtml.find("3 years ago") != -1):
                 skeepScrolling = False
      elif selectingRcount < 50:
          print(selectingRcount)
          print("50")
          skeepScrolling = False 
          with open("error.txt", 'a', encoding="utf-8") as f:   
             f.write(str(ar) + "\n")
      time.sleep(30)
      findr= driver.find_elements(By.CLASS_NAME, "jftiEf.fontBodyMedium")




  

      clickMore= driver.find_elements(By.XPATH, '//button[@aria-label="See more"]')
      
        
      for t in range(len(clickMore)):
       
        
        #WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="See more"]'))).click()  
        button = driver.find_element(By.XPATH, '//button[@aria-label="See more"]')
        driver.execute_script("arguments[0].click();", button)
  
      Savinghtml=driver.find_element(By.TAG_NAME, "html").get_attribute('outerHTML')

  
      os.makedirs("Cafes Dharamshala", exist_ok=True)
      file_path = os.path.join("Cafes Dharamshala", f"{ar}.html")
      with open(file_path, 'a', encoding='utf-8') as f:
        f.write(Savinghtml)
        
    
    
   
 
#fin= driver.find_elements(By.CSS_SELECTOR, 'button[class="hh2c6 "]') 
#for int in range(7):
  
    #findrr= fin[int]
    #findrr.click()
        

print("Scraping completed.")
driver.quit()
