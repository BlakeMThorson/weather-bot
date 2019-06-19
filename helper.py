from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
import random


#___________________________________________
#____________QUOTE OF THE NOW_______________ WORKING

def current(zipcode):
    
    
    import urllib.request    
    url = "https://www.weatherforyou.com/reports/index.php?config=&forecast=zandh&pands={}&Submit=Get+Weather".format(zipcode)
    update = ""
    
    # Open the URL as Browser, not as python urllib
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    page_soup = Soup(data, "html.parser") #html parsing
    
    Whole = page_soup.findAll("div", {"id": "currents"})
    
    #get current tempeture
    currentTemp = Whole[0].findAll("span",{"class":"Temp"})
    currentTemp = currentTemp[0].text
    
    #get current feels like
    currentFeelsLike = Whole[0].findAll("span",{"class":"SmallTemp"})
    currentFeelsLike = currentFeelsLike[1].text
    
    currentHumidity = Whole[0].findAll("td",{"style":"white-space:nowrap; width:130px;"})
    currentDewPoint = currentHumidity[1].text
    currentVisibility = currentHumidity[2].text
    currentHumidity = currentHumidity[0].text
    
    currentWind = Whole[0].findAll("td",{"style":"white-space:nowrap;"})
    currentBarometer = currentWind[1].text
    currentWind = currentWind[0].text
    #other current shit
    
    
    #get picture along with it
    currentTempPic = Whole[0].findAll("td", {"style":"width:55px; text-align:right; vertical-align:top;"})
    currentTempPic = currentTempPic[0]
    currentTempPic = currentTempPic.img["src"]
    
    #check advisories and append link to them
    link = "NONE"
    advisories = "There are currently no weather advisories!"
    
    check = page_soup.findAll("div",{"style":"width: 630px; border-style: solid; border-width: 3px; border-color: red; color: red; font-weight: bold; font-size: 16px;"})
 
    if len(check) >= 1:
        advisories = check[0].text
        advisories = advisories.replace("\xa0","")
        advisories = advisories[13:].replace("-","\n")
        
        link = check[0].a["href"]
        link = "https://www.weatherforyou.com" + link
                
    #gets current city
    city =  page_soup.findAll("div",{"style":"float:left; margin:0px;"})
    city = city[0].text
    city = city[:city.index("(")].replace("\n","").replace("  ","")
    
    laterWeather = page_soup.findAll("td",{"style":"vertical-align:top; background: #efefef;"})

    
    laterWeatherNight = None
    if "Night" in laterWeather[1].text:
        laterWeatherNight = laterWeather[1].text
    laterWeather = laterWeather[0].text
    
    
    #later weather picture
    laterWeatherIcon = page_soup.findAll("td",{"style":"text-align:left; vertical-align:top; width:55px; background: #efefef;"})
    laterWeatherIcon = laterWeatherIcon[0].img["src"]

    
    return [city,currentTemp,currentTempPic,advisories,link,currentFeelsLike,currentHumidity,currentVisibility,currentDewPoint,currentWind,currentBarometer,laterWeather,laterWeatherIcon]



