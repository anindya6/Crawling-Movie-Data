#populate directory with actors and directors
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
import urllib
import urllib.request
import sys
def download_image_yay(url,imgname,filename):
    f=open("C:/Users/shankarb/Downloads/Movie_Images/"+filename+".jpg",'w')
    image=urllib.URLopener()
    image.retrieve(url,imgname)
    f.write(image)
    f.close()
    print("I downloaded ",filename)
def download_image(url,imgname,filename):
    f = open(filename,'wb')
    f.write(urllib.request.urlopen(str(url)+'/download.jpg').read())
    f.close()
    print("I downloaded ",filename)
def download_single_image(url_link, pic_prefix_str):
    temp_filename = pic_prefix_str
    temp_filename_full_path = os.path.join("C:/Users/shankarb/Downloads/Movie_Images/", temp_filename)
    valid_image_ext_list = ['.png','.jpg','.jpeg', '.gif', '.bmp', '.tiff']
    #url = URL(url_link)
    url=url_link
    if url.redirect:
        return # if there is re-direct, return
    if file_ext not in valid_image_ext_list:
        return #return if not valid image extension
    f = open(temp_filename_full_path, 'wb') # save as test.gif
    print(url_link)
    try:
        f.write(url.download())#if have problem skip
    except:
        print('Problem with processing this data: ', url_link)
        self.download_fault =1
    f.close()
i=0
movies=[None]*27000
with open('C:/Users/shankarb/Downloads/Movie_Images/movienames.csv', 'r', encoding='latin-1') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if i>0:
            movies[i-1]=str(row[1])+" "+str(row[4])
        i=i+1
#print(movies[0:5])
#sys.exit()
link=[None]*len(movies)
f.close()
browser=webdriver.Firefox()
q=0
for string in movies:
    try:
        i=0
        if string is None:
            break
        #browser.get('https://www.google.co.in/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=the%20revenant')
        url='https://www.google.co.in/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q='
        #string=string[0:-6]#remove year
        string=string.strip()#remove any trailing spaces
        #string=string.replace(' ','%20')#insert %20 between
        url=url+string#append to url
        browser.get(url)
        time.sleep(2)
        x=browser.page_source
        soup=BeautifulSoup(x,"html.parser")
        check=""
        check=soup.find('g-img',{'class','iuth'})
        for img in check:
            link[q]=img.get('src')
        #print(link[q])
        filename=str(str(movies[q])+".jpg")
        download_image(link[q], "download.jpg", filename)
        q+=1
    except:
        link[q]="Not Found"
        q+=1
        '''
        try:
            for str1 in str2:
                i=i+1
                if str1=='Director':
                    director[q]=str2[i]
                    break
        check1=soup.findAll('div',{'class','_NRl'})
        Actor1[q]=check1[0].text
        Actor2[q]=check1[1].text
        Actor3[q]=check1[2].text
        Actor4[q]=check1[3].text
        Actor5[q]=check1[4].text
        plot[q]=soup.find('div',{'class','kno-rdesc'}).text
        q=q+1
    except:
        q=q+1
    #, encoding='utf-8'
    time.sleep(2)'''
