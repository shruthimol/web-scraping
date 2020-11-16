import bs4  # first we import an library required for web scraping (bs4-beautiful soup )
from urllib.request import urlopen as u  # this is to parse an web url into python, i have declared it to be called 'u'
from bs4 import BeautifulSoup as soup  # here beautiful soup module is imported from the bs4 library

url = 'https://www.indeed.ae/jobs?q=oil+and+gas+&l=abudhabi'  # store the webpage url in an variable
url2 = 'https://www.indeed.ae/jobs?q=oil+and+gas+&l=abudhabi&start=10'  # same process"
uclient = u(url)  # here we invoke urlopen function to render for python
uclient2 = u(url2)

page = uclient.read()  # this code enables the content on the web html to be read by the parser into a beautiful soup object..
page2 = uclient2.read()

uclient.close()  # close function cuts connection from the website once html is read and converted so, even if networ error occurs our file will be running without error
uclient2.close()

scrap = soup(page,"html.parser")  # The soup function splits the html file content as a dictionary format in python or key value classification of the html file
scrap2 = soup(page2, "html.parser")

# scrap.h1
# scrap.body

fin = scrap.findAll("div", {"class": "title"})  # Here i only wanted to find the title of the jobs listed, so I coded using find all function that fetches me job title from different classes of the division tag in html
fin2 = scrap2.findAll("div", {"class": "title"})

fin
fin2

len(fin)  # This is just to know how many job titles are there in the file, if you want to know just use print function to see the output
fin[0]

a = fin[0]  # python is zero indexed so we initialize a variable at that point
i = fin[0]  # declaring another variable with same index
i.a["title"]  # Joined both the variable using dot to denote the relationship between both the variable is title of the job profile
# Now every element under the collected data has an title called "title" e.g - mechanical engineer is classified by python under the tag title

x = fin2[0]
y = fin2[0]
y.a["title"]

file = "jobs.csv"  # File operation is done to open a blank comma seperated value file (CSV file)..this is only executed during operation on the RAM
f = open(file,"w")  # open command is given to open the file and the tag "w" is given to notify the python that we need to write into the opened file
headers = "job\n"  # file title or heading is given here
f.write(headers)  # telling the python to start writing into the csv file the extracted data from the website
# Executing for loop to read through each and every tagline named title
for i in fin:
    job = i.a["title"]

    print("job profile    " + job)  # print as (job profile      Mechanical Engineer)

    f.write(job + "\n")  # this code writes every new listing under a new line
for y in fin2:  # same code for second url
    job2 = y.a["title"]
    print(" Job Profile    " + job2)
    f.write(job2 + "\n")
f.close()  # closing the file is important as this file operation is running in your RAM, so close file code is executed here
