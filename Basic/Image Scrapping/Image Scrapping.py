#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os


# In[5]:


save_dir="Image/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)


# In[7]:


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


# In[9]:


query="Dog"
response=requests.get(f"https://www.google.com/search?q={query}&sxsrf=AHTn8zpAumVsJGyODXgQTGeY6KCA7iT2Og:1745937281881&q=dog&udm=2&fbs=ABzOT_CWdhQLP1FcmU5B0fn3xuWpA-dk4wpBWOGsoR7DG5zJBsxayPSIAqObp_AgjkUGqel3rTRMIJGV_ECIUB00mupujJbyw82c7vlYBaFJu3BmNAQzAFr6obCTLutWM17qnmiOU-zUTKn7eXIlsD8HYbVMoPCUoQ-8w2eBI-HPhrVEu8E-X-pRJi-IDF2DFIJu34aAXq7SSNs64lEYJnUMf4GCLzulQQ&sa=X&ved=2ahUKEwjyiPKbu_2MAxXdyDgGHQm9IucQtKgLegQIERAB&biw=1440&bih=688&dpr=1.33")


# In[10]:


BeautifulSoup(response.content,"html.parser")


# In[11]:


#BeautifulSoup(response.text,"html.parser")
# or
soup=BeautifulSoup(response.content,"html.parser")
soup


# In[12]:


soup.find_all("img")


# In[17]:


images_tag=soup.find_all("img")


# In[19]:


len(images_tag)


# In[21]:


del images_tag[0]


# In[23]:


images_tag[2]["src"]


# In[33]:


img_data_mongo=[]
for i in images_tag:
    image_url =i['src']
    image_data=requests.get(image_url).content
    mydict={"index":image_url ,"image":image_data}
    img_data_mongo.append(mydict)
    with open (os.path.join(save_dir,f"{query}_{images_tag.index(i)}.jpg"),"wb")as f:
        f.write(image_data)


# ## For Advance 

# In[ ]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests
import os

query = "Dog"
save_dir = "Image/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Set up Chrome WebDriver
driver = webdriver.Chrome()
driver.get(f"https://www.google.com/search?q={query}&tbm=isch")

# Scroll to load more images
for _ in range(5):  # Increase range for more scrolls
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for images to load

# Extract image URLs
images = driver.find_elements(By.CSS_SELECTOR, "img.rg_i")
print(f"Found {len(images)} images")

count = 0
for img in images:
    src = img.get_attribute("src")
    if src and "http" in src:
        try:
            image_data = requests.get(src).content
            with open(os.path.join(save_dir, f"{query}_{count}.jpg"), "wb") as f:
                f.write(image_data)
            count += 1
        except:
            pass

driver.quit()
print(f"Downloaded {count} images.")

