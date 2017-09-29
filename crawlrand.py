from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
browser=webdriver.Firefox()
url = 'http://www.movieforums.com/community/showthread.php?t=45711'
browser.get(url)
x=browser.page_source
check=[None]*300
usrnm=[None]*300
soup=BeautifulSoup(x,"html.parser")
for i in range(2,8):
    time.sleep(2)
    check[i-1]=soup.findAll('div',{'class','posttext'})
    usrnm[i-1]=soup.findAll('a',{'class','username'})
    urlx=url+'&page='+str(i)
    browser.get(urlx)
    x=browser.page_source
    soup=BeautifulSoup(x,"html.parser")
check[i]=soup.findAll('div',{'class','posttext'})


with open('C:/Users/shankarb/Documents/disney_data.csv', 'w', encoding='utf-8', newline='') as csv2: 
    fieldnames = ['#', 'Username', 'Comment']
    writer=csv.writer(csv2, delimiter=',')
    q=0
    writer = csv.DictWriter(csv2, fieldnames=fieldnames)
    for i in range(1,len(check)-1):
        for j in range(0,len(check[i])):
            if 'adsbygoogle' not in str(check[i][j]):
                q=q+1
                comm=str(check[i][j].text)
                writer.writerow({'#':str(q),'Username':str(usrnm[i][j].text),'Comment':comm.strip().replace('^','')})
