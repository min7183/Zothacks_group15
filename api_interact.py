import requests
import urllib.parse
import pprint

def get_all(search: str, description = None, keywords= None, media = None, ):
    y= 'https://images-api.nasa.gov/search?q='+urllib.parse.quote(search)
    if description != None:
        y = y + '&description='+urllib.parse.quote(description)
    if keywords != None:
        y = y + '&keywords='+urllib.parse.quote(keywords)
    if media != None:
        y = y + '&media_type='+urllib.parse.quote(media)
    print(y)
    x = requests.get(y)
    return x

def get_asset(asset: str):
    y = 'https://images-api.nasa.gov/asset/' + urllib.parse.quote(asset)
    x = requests.get(y)
    return x

def get_items(api_response: dict):
    #pprint.pprint(api_response)
    d = api_response['collection']['items']
    image_list = []
    description_list=[]
    number = api_response['collection']['metadata']['total_hits']
    if number > 10:
        number = 10
    for i in range(number):
        image = d[i]['links'][0]['href']
        description = d[i]['data'][0]['description']
        image_list.append(image)
        description_list.append(description)

    return image_list, description_list


