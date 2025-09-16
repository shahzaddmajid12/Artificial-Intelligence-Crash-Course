# python -m pip install requests
# pip install --user requests
# python.exe -m pip install --upgrade pip

import requests

response= requests.get("https://api.alquran.cloud/v1/surah")

if response.status_code==200:
    meriSurahsList=response.json()["data"]
    for i in meriSurahsList:
        print(i["englishName"])