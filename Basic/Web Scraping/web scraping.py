#!/usr/bin/env python
# coding: utf-8

# #  What is Web Scraping?
# **Web scraping means automatically extracting data from websites using code. 
# Instead of manually copying information from webpages,
# you write a Python script (or use tools) to collect data programmatically.**
# 
# 
# # How Scraping Usually Works:
# **1. Send a Request ➔ Your code sends a request to a website URL.**
# 
# **2. Get the Response ➔ You receive HTML (page content) as text.**
# 
# **3. Parse the HTML ➔ Use libraries like BeautifulSoup, lxml, or selectolax to find and extract specific data (like headings, tables, prices, etc.).**
# 
# **4. Store the Data ➔ Save it into CSV, JSON, Database, or wherever you want.**
# 

# In[49]:


import requests
from bs4 import BeautifulSoup 
from urllib.request import urlopen 


# In[2]:


get_ipython().system('pip install requests')


# In[4]:


flipkart_url = "https://www.flipkart.com/search?q=" + "iphone12pro"
# urlClient=urlopen(flipkart_url)
# flipcart_page=urlClient.read()
# flipkart_html=bs(flipcart_page,'html.parser')
# flipkart_html


# import requests
# from bs4 import BeautifulSoup

# # Corrected URL
# flipkart_url = "https://www.flipkart.com/search?q=" + "iphone12pro"

# # Sending the GET request
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# }
# response = requests.get(flipkart_url, headers=headers)

# # Parsing the page with BeautifulSoup
# flipkart_html = BeautifulSoup(response.text, 'html.parser')

# # Printing the parsed HTML
# print(flipkart_html)


# In[5]:


flipkart_url


# In[7]:


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


# # ***Sending the GET request***

# In[9]:


#request = Request(flipkart_url, headers=headers)
# Opening the URL with urlopen
#urlClient = urlopen(request)

#or

response = requests.get(flipkart_url, headers=headers)


# # To convert in text

# In[15]:


response.text   #urlClient.read()


# # **Handle It:  'Site is overloaded'**
# 
# This way, your code can wait and try again after a few seconds instead of crashing.

# In[98]:


# import time
# import requests

# url =flipkart_url # Replace with your API
# max_retries = 5

# for attempt in range(max_retries):
#     response = requests.get(url)
    
#     if "overloaded" not in response.text.lower():
#         print("Success:", response.text)
#         break
#     else:
#         print(f"Attempt {attempt + 1}: Site overloaded, retrying...")
#         time.sleep(2)  # Wait 2 seconds before retrying
# else:
#     print("Failed after multiple retries.")


# # Best Professional Way — Use tenacity library   ---> for ***Handle It: 'Site is overloaded'***
# The tenacity library automatically handles retries with backoff + jitter (best for production quality).

# In[100]:


# from tenacity import retry, wait_exponential, stop_after_attempt
# import requests

# @retry(wait=wait_exponential(multiplier=1, min=2, max=60), stop=stop_after_attempt(10))
# def fetch_data():
#     response = requests.get(flipkart_url, headers=headers)
#     if "overloaded" in response.text.lower():
#         raise Exception("Site overloaded")
#     return response

# try:
#     data = fetch_data()
#     print(data.text)
# except Exception as e:
#     print("Failed after retries:", str(e))


#  # Parsing the page with BeautifulSoup

# In[17]:


#flipcart_page=urlClient.read()
#flipkart_html=bs(flipcart_page,'html.parser')
#flipkart_html

#or


flipkart_html = BeautifulSoup(response.text, 'html.parser')
#print(flipkart_html)
print(flipkart_html.prettify())


# In[19]:


big_box=flipkart_html.find_all("div",{"class":"cPHDOP col-12-12"})


# In[21]:


len(big_box)


# In[23]:


del big_box[0:2]
del big_box[-3:]


# In[213]:


len(big_box)


# In[25]:


big_box[1]


# In[27]:


big_box[3].div.div.div.a['href']


# In[29]:


"https://www.flipkart.com"+big_box[3].div.div.div.a['href'] 


# In[31]:


for i in big_box:
    print("https://www.flipkart.com"+i.div.div.div.a['href'])


#or
# for i in big_box:
#     if i.div and i.div.div and i.div.div.div and i.div.div.div.a:
#         print(i.div.div.div.a['href'])
#     else:
#         print("No anchor tag found")


# In[211]:


## By going sinle link
"https://www.flipkart.com"+big_box[4].div.div.div.a['href']


# # we can the url page by big_box[i] to extract one by one page

# **or we can combine all the page and scrap at ones ----> code for that is  the
# in last**  
# 

# In[217]:


product_link="https://www.flipkart.com"+big_box[22].div.div.div.a['href']


# In[219]:


product_req=requests.get(product_link)


# In[220]:


product_html=BeautifulSoup(product_req.text,'html.parser')


# In[221]:


comment_box=product_html.find_all('div',{'class':'RcXBOT'})


# In[222]:


len(comment_box)


# # Name of customer

# In[228]:


comment_box[0].div.div.find_all('p',{'class':'_2NsDsF AwS1CA'})[0].text


# In[230]:


comment_box[0].find_all('p',{'class':'_2NsDsF AwS1CA'})[0].text


# In[232]:


for i in comment_box:
    print(i.find_all('p',{'class':'_2NsDsF AwS1CA'})[0].text)


# To handel the **list index out of range**

# In[235]:


for i in comment_box:
    if i.div and i.div.div and i.div.div and i.div.div.p:
        print(i.find_all('p',{'class':'_2NsDsF AwS1CA'})[0].text)
    else:
        print("No anchor tag found")


# In[237]:


del comment_box[-1:] ## drop or delet the last row


# In[239]:


for i in comment_box:
    if i.div and i.div.div and i.div.div and i.div.div.p:
        print(i.find_all('p',{'class':'_2NsDsF AwS1CA'})[0].text)
    else:
        print("No anchor tag found")


# # Review OF customer

# In[242]:


for i in comment_box:
    print(i.find_all('p',{'class':'z9E0IG'})[0].text)


# # Rating 

# In[245]:


for i in comment_box:
    print(i.div.div.div.div.text)


# In[247]:


# or
for i in comment_box:
    print(i.find_all('div',{'class':'XQDdHH Ga3i8K'})[0].text)


# # comment

# In[250]:


for i in comment_box:
    print(i.find_all('div',{'class':''})[0].text)


# In[ ]:





# In[268]:


for i in big_box:
    product_link="https://www.flipkart.com"+i.div.div.div.a['href']
    product_req=requests.get(product_link)
    product_html=BeautifulSoup(product_req.text,'html.parser')
    comment_box=product_html.find_all('div',{'class':'RcXBOT'})

    for i in comment_box:
        if i.div and i.div.div and i.div.div and i.div.div.p:
            print(i.find_all('p',{'class':'_2NsDsF AwS1CA'})[0].text)
            print(i.find_all('p',{'class':'z9E0IG'})[0].text)
            print(i.div.div.div.div.text)
            print(i.find_all('div',{'class':''})[0].text)
            print("-"*55)
        else:
            print("No anchor tag found")


# In[ ]:




