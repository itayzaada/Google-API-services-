# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 17:52:11 2021

@author: Itay Zaada
"""
import json
import urllib
import requests

file=input("Enter File Name : ")
def  reader (file):
    lst=[]
    fhand = open(file,'r',encoding='UTF-8')
    fhand=fhand.readlines()
    for word in fhand :
        lst.append(word.strip())
    return lst
cities=(reader(file))

api_key=" " #I added the API In File in Moodel System ##



serviceurl='https://maps.googleapis.com/maps/api/distancematrix/json?'
parms = dict()
parms['origins']='תל אביב'
parms['key'] = api_key
lst=[]
lstprint=[]
dic={}
address=" "
try :
    
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
            textdur=duration['text']
        if('days' in textdur ):### if in days move to hours ## 
                text=textdur.split('days')
                add_houers=int(text[0])*24
                hours2=text[1].split('hours')
                houers3=int(hours2[0])
                hours=add_houers+houers3
                textdur=str(hours)+hours2[1]+" hours" 
        if('1 day' in textdur ):  ## if it is just one day ##
                text=textdur.split('day')
                add_houers=int(text[0])*24
                hours2=text[1].split('hours')
                houers3=int(hours2[0])
                hours=add_houers+houers3
                textdur=str(hours)+hours2[1]+" hours"  
        
        response2 = requests.get(url2).json()##second part ##
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
        dic.update({city: need})## the dictionary ineed to print ##
        to_print={'Destination':city,'Distance':textdist,'Duration':textdur,'lat':lat,'Lng':lng}
        lstprint.append(to_print)


    print("the dictonary:")
    print("---------------------------------------------------")
    print(dic)
    print("---------------------------------------------------")
    print("Printed nice looking")
    for item in lstprint:
       print("___________________________")
       print('\n'.join("{}: {}".format(k, v) for k, v in item.items()))
       print(" ") 


except:
    if api_key==" ":
        print("I add the API key in the text file in mooodel-add it in line 20 and try again")
    else:
        print("Something went wrong")





    
        
        