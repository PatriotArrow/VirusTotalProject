import os
import requests
import json
from dotenv import load_dotenv
import sys

load_dotenv()
API_KEY = os.getenv("API_KEY")

hashes = open("hash.txt").read().splitlines()
# print(hashes)

#session init
session = requests.Session()
session.headers = {'X-Apikey': API_KEY}
# session.headers = {'X-Apikey': "123"}

# url = "https://www.virustotal.com/api/v3/monitor_partner/hashes/05dc7b24be0359720c2ac68c53966378063e51d23251cb9993be37300b195265/items"
url = "https://www.virustotal.com/api/v3/users/me"
response = session.get(url)
if response.status_code == 401:
    sys.exit("API Key could not be validated. Exiting...")




for num,hash in enumerate(hashes):

    url = f"https://www.virustotal.com/api/v3/files/{hash}"
    response = session.get(url)
    
    if response.status_code == 200:
        # print(response.json())
        with open(f'json_files/{hash}.json', 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, indent=4)
        print(f"{num}, {hash}.json saved ") #change phrasing ?
    elif response.status_code == 404:
        print(f"{num}, hash not found : {hash}  ")

    

##todo
# Implement basic error handling to manage potential issues with the API request, such as network problems ??? 


#https://realpython.com/python-requests/#get-started-with-pythons-requests-library
# https://docs.virustotal.com/reference/monitorpartner-hashes-items
# https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file