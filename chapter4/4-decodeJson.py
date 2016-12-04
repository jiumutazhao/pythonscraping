import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getCountry(ipAddress):
    response=urlopen("htpp://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson=json.loads(response)
    return  responseJson.get("country_code")
print(getCountry("50.78.253.58"))
