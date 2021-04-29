# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 17:52:11 2021

@author: Itay Zaada
"""
import json
import urllib
import requests
def  reader (file):
    lst=[]
    fhand = open(file,'r',encoding='UTF-8')
    fhand=fhand.readlines()
    for word in fhand :
        lst.append(word.strip())
    return lst


cities=(reader('dests.txt'))
api_key='AIzaSyC5rG6QFzHk6BsFHmiKcU-XiuI_chdkQno'
serviceurl='https://maps.googleapis.com/maps/api/distancematrix/json?'

parms = dict()
parms['origins']='תל אביב'
parms['key'] = api_key
lst=[]
dict={}
address=" "
for city in cities:
    parms['destinations']=city
    address=city
    url= serviceurl + urllib.parse.urlencode(parms)
    response=requests.get(url).json()
    row= response['rows']
    url2="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address,api_key)
    for rows in (row):
        element=rows['elements']
    for elements in (element):
        distance=elements['distance']
    for distances in (distance):
        textdist=distance['text'].strip().replace(" ","") ## the distace i need # 
        
    for elements in (element):
        duration=elements['duration']
    for distances in (distance):
        textdur=duration['text'] ## the duration i need #
    response2 = requests.get(url2).json()
    result= response2['results']
    for results in (result):
        geometry=results['geometry']
    for geometrys in (geometry):
        bound=geometry['bounds']
    for bounds in (bound):
        northeast=bound['northeast']
    for lats in (northeast):
        lat=northeast['lat'] ## the distace i need #        
    for lngs in (northeast):
        lng=northeast['lng'] ## the distace i need #   
    need=(textdist,(textdur),(lat,lng))
    dic={city: need}
    lst.append(dic)
print(lst, sep="\n")    

        


    
        
        