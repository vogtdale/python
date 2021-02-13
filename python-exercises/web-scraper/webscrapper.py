import requests 
from bs4 import BeautifulSoup

# use get function to provide access to webpage
result = requests.get("https://www.google.com")

# to make sure the website is accessible 
# ensure we obtain a 200 OK response 
'''print("response: ",result.status_code)'''

# we can also check the HTTP header of the website to
# verify that we have indeed accessed the correct page
'''print("headers: ",result.headers)'''

# now store the page content of the website accessed
# from websites request into a variable
src = result.content

# now that w have the page source stored we will use 
# the bs4 module to parse and process the source 
# to do so we create a bs4 object based on the src variable
# we created
soup = BeautifulSoup(src, "lxml")

# now that the source has been processed via bs4
# we can access specific info directly from it. For instance
# we can see a list of all of the links on the page
links = soup.find_all("a")
'''print(links)'''
'''print("\n")'''

# if we want to only get the link that contains the text 
# About on the page instead of every link we can use the 
# built in text function to access the text content between the <a> tag
for link in links:
    if "Gmail" in link.text:
        print(link)
        print(link.attrs['href'])

