from bs4 import BeautifulSoup
import os
import json


path = f"/Users/manishpargai/Documents/scrap/Cafes Dharamshala"

dir_list = os.listdir(path)
change_list = [] 
cafes_data_list =[]
for i in range(len(dir_list)):
    change= dir_list[i].replace(".html","").replace(".", "").replace("icloud", "")
    cafes_data = {
        "cafename": change,
        "userId": [{"$oid": "67c9497b6a31d6241c359b93"}],
        "reviews": [],
        "createdAt": {"$date": "2024-12-24T13:12:56.774Z"},
        "updatedAt": {"$date": "2025-02-03T09:16:07.371Z"},
        "__v": 0,
        "ambienceR": 0,
        "foodR": 0,
        "serviceR": 0,
        "Av": 0,
        "drinkR": 0
          }
    
    file_path = "cafes_list.json"
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(cafes_data, ensure_ascii=False, indent=4) + ",\n")
    print(cafes_data)


#with open("file.html", "r") as f:
    #html = f.read()

    #soup = BeautifulSoup(html, 'html.parser')

    #print(soup.prettify())

    #print(soup.title.text)
