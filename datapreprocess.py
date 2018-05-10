from bs4 import BeautifulSoup
#import urllib2
import urllib.request as urllib2

import csv
from pyparsing import Literal, quotedString, removeQuotes, delimitedList
import time
from random import randint
import pandas as pd
import numpy as np


def open_csvfile(file_name):
    X=open(file_name,"r")
    Xdata=[]
    
    with X:
        reader = csv.reader(X)
        for row in reader:
            #%for e in row:
            Xdata.append(row)
            
    return Xdata


filename='restaurant.csv'


rawdata=pd.read_csv(filename,index_col=0)

attribute=rawdata['attributes']

i=5


att=attribute[5]

def SPLIT(att):
    
    att=att.split(',')
    att=[i.split('(', 1)[0] for i in att]
    att2=[i.split(')', 1)[0] for i in att]
    att2=[i.split('=', 1)[0] for i in att2]

    return att2

def SPLIT2(att):
    
    att=att.split(',')
    att=[i.split('(', 1)[0] for i in att]
    att2=[i.split(')', 1)[0] for i in att]

    return att2

#find every attribute
totalfeatures=[]
k=0
for sample in attribute:
    features=SPLIT(sample)
    for singlef in features:
        if singlef in totalfeatures:
            k+=1
        else:
            totalfeatures.append(singlef)
    

array=np.asarray(totalfeatures)

data=pd.DataFrame({})
for feat in totalfeatures:
    data[feat]=1


att=attribute[6]

#ind=attribute.index
i=0
for att in attribute:
    prop=SPLIT2(att)
    dummy={}
    prop.remove('list')
    #oneind=attribute[ind[i]].index
    for element in prop:
        BK=[element.split('=')]
        dummy[BK[0][0]]=BK[0][1]
    
    dummydf=pd.DataFrame(dummy,index=[attribute.index[i]])
    
    data = pd.concat([data, dummydf], axis=1)
    i+=1
    if i == 300:
        break
    print(i)
    #dummydf=pd.DataFrame.from_dict(dummy,orient='index')
    #dummydf=pd.DataFrame.T
    
        

        
    
        
        
    


                
    
    
    
    

