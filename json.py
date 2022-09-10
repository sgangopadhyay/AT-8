# Working with JSON

import requests


url = "https://631c07611b470e0e12f931a6.mockapi.io/food"

# Fetch the data from the API server
def FetchData(url):
    response = requests.get(url)
    return response.json()

# Count the number of JSON data present on the server
def CountJSONData(url):
    data = FetchData(url)
    count  = 0
    for data in data:
        count=count+1
    return count 

# Fetching all the names from the API server
def Suman(url):
    data = FetchData(url)
    for data in data:
        print(data['name'])

# Fetch data based on ID
def FetchByName(url, id):
    data = FetchData(url)
    # type casting to convert the interger format to string format for ID
    id = str(id)
    for data in data:
        if(data['id']==id):
            print(data['id'])
            print(data['name'])
            print(data['location'])
            print(data['image_url'])
        else:
            print("ID does not exists !")
            
# Fetch Data based on country
def FetchByCountry(url, country_name):
    data = FetchData(url)
    for data in data:
        if(data['location']==country_name):
            print(data['id'])
            print(data['name'])
            print(data['location'])
            print(data['image_url'])
        

FetchByCountry(url,"Oman")
