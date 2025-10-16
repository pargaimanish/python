from bs4 import BeautifulSoup
import os
import json
import pymongo
from pymongo import MongoClient
import re


exp_ = MongoClient("mongodb://noddles1_7L:aJU02Xiio4gZcbE@88.222.241.149:27017")
data = exp_["exp"]
cafes_list = data["cafes"]

path = f"/Users/manishpargai/Documents/scrap/Cafes Dharamshala"

dir_list = os.listdir(path)
change_list = [] 
cafes_data_list =[]
for j in range(len(dir_list)):
    change= dir_list[j].replace(".html","").replace("icloud", "")
    cafes_data_list.append(change)

for i in cafes_list.find({},{ "cafename": 1, "_id": 1 }):
    if i["cafename"] in cafes_data_list:
        file_path_c = f"/Users/manishpargai/Documents/scrap/Cafes Dharamshala/{i["cafename"]}.html"
        with open(file_path_c, "r", encoding="utf-8") as f:
            html=  f.read()
        soup = BeautifulSoup(html, 'html.parser') 
        div_elements = soup.find_all("div", class_="jftiEf fontBodyMedium")
        lenghtb =len(div_elements)
        print(i)
        print(lenghtb)
        for r in range(len(div_elements)):
             
            exp1 = div_elements[r].find("span", class_="wiI7pd")
            rating = div_elements[r].find("span", class_="kvMYJc")
            
            print(exp1)
            
            if exp1 is not None and rating is not None:
                exp2 = exp1.get_text()   
            
           
                rating2 = rating['aria-label']
                print(rating2)
                rating_3 = int(re.sub(r'\D', '',rating2))
                print(rating_3)
                ratin_10= rating_3 * 2
                print(ratin_10)
                itune= str(i["_id"])
                remove_br= itune.replace("ObjectId","").replace("(","").replace(")","").strip()
                r_list = {
                    
                    "review": exp2,
                    "ratingAmbience": ratin_10,
                    "ratingFood": ratin_10,
                    "ratingDrink": ratin_10,
                    "ratingService": ratin_10,
                    "cafeId": {
                        "$oid": remove_br
                    },
                    "comments": [],
                    "userId": [
                        {
                        "$oid": "67c9497b6a31d6241c359b93"
                        }
                    ],
                    "createdAt": {
                        "$date": "2024-12-24T13:12:56.785Z"
                    },
                    "updatedAt": {
                        "$date": "2025-02-03T09:16:06.991Z"
                    },
                    "__v": 0,
                    "reviewWeight": 0,
                    "reviewWeightA": 0,
                    "reviewWeightD": 0,
                    "reviewWeightF": 0,
                    "reviewWeightS": 0
                            }
                print(r_list)
                file_path = "rrr_list.json"
                with open(file_path, "a", encoding="utf-8") as f:
                     f.write(json.dumps(r_list, ensure_ascii=False, indent=4) + ",\n")
                

#with open("file.html", "r") as f:
    #html = f.read()

    #soup = BeautifulSoup(html, 'html.parser')

    #print(soup.prettify())

    #print(soup.title.text)