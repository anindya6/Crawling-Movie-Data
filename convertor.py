import os  
from bs4 import BeautifulSoup
import pandas as pd

f=open("stuff.txt",mode='r',encoding='latin-1')
x=BeautifulSoup(f)
dictn={}
q=-1
for i in range(0,501):
    try :
        texts=x.find(id=str(i))
        simpletexts=texts.findAll('simpletextpart')
        entities=texts.findAll('namedentityintext')
        a=0
        b=0
        data=texts.text
        #print(i, " : Length of simpletexts : ",len(simpletexts)," and Length of entities : ",len(entities))
        x01=len(simpletexts)
        x02=len(entities)
        for j in range(0,len(simpletexts)+len(entities)):
            #print (j)
            q+=1
            #print(a," ",b)
            #print(x01," ",x02)
            if x01>0 and x02>0:
                if data.find(simpletexts[a].text)<data.find(entities[b].text):
                    #print("Block 1")
                    dictn[q]={'sid':i,'chunk':simpletexts[a].text,'tag':'simpletextpart'}
                    a+=1
                    if a==x01:
                        x01=0
                else:
                    #print("Block 2")
                    dictn[q]={'sid':i,'chunk':entities[b].text,'tag':'namedentityintext'}
                    b+=1
                    if b==x02:
                        x02=0
                        #print("I reached here : ",x02)
            elif x01>0:
                #print("Block 3")
                dictn[q]={'sid':i,'chunk':simpletexts[a].text,'tag':'simpletextpart'}
                a+=1
                if a==x01:
                    x01=0
            elif x02>0:
                #print("Block 4")
                dictn[q]={'sid':i,'chunk':entities[b].text,'tag':'namedentityintext'}
                b+=1
                if b==x02:
                    x02=0
    except:
        pass
dx=pd.DataFrame(dictn)
dx.to_csv("dataset.csv",sep=',')
            
            
        
