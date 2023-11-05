import requests
import urllib.parse
import pprint

def get_all(search: str, description = None, keywords= None, media = None):
    y= 'https://images-api.nasa.gov/search?q='+urllib.parse.quote(search)
    if description != None:
        y = y + '&description='+urllib.parse.quote(description)
    if keywords != None:
        y = y + '&keywords='+urllib.parse.quote(keywords)
    if media != None:
        y = y + '&media_type='+urllib.parse.quote(media)
    #print(y)
    x = requests.get(y)
    return x,media

def get_asset(asset: str):
    y = 'https://images-api.nasa.gov/asset/' + urllib.parse.quote(asset)
    x = requests.get(y)
    return x

def get_items(api_response: dict, media = None):
    #pprint.pprint(api_response)
    d = api_response['collection']['items']
    image_list = []
    description_list=[]
    number = api_response['collection']['metadata']['total_hits']
    if number > 10:
        number = 10
    for i in range(number):
        j_file = d[i]['href']
        api_response2 = requests.get(j_file).json()[0]
        if media == 'video':
            while not api_response2.endswith('.mp4'):
                api_response2 = requests.get(j_file).json()[(requests.get(j_file).json().index(api_response2)+1)]
        if media == 'image':
            while not api_response2.endswith('.jpg'):
                api_response2 = requests.get(j_file).json()[(requests.get(j_file).json().index(api_response2)+1)]
        image = api_response2
        description = d[i]['data'][0]['description']
        image_list.append(image)
        description_list.append(description)
        
        # print(number)
        # for image in image_list:
        #     print(image)
        # for description in description_list:
        #     print(description)


    return image_list, description_list


get_items(get_all('mars', media = 'image')[0].json(),get_all('mars', media = 'image')[1])
