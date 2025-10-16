from bs4 import BeautifulSoup
import os
import json
import pymongo
from pymongo import MongoClient
import re
from bson import ObjectId


exp_ = MongoClient("mongodb://noddles1_7L:aJU02Xiio4gZcbE@88.222.241.149:27017")
data = exp_["exp"]
cafes_list = data["cafes"]
review_list = data["reviews"]

cafes_data = list(cafes_list.find({}, {"reviews": 1, "_id": 1}))  # Fetch cafes once

for i in review_list.find({}, {"cafeId": 1, "_id": 1}):  # Loop through each review
    for j in cafes_data:  # Use the pre-fetched list instead of making new DB queries
        rrr=ObjectId(str(i["_id"]))

        if i["cafeId"] == j["_id"] and rrr not in j["reviews"]:
            if i["cafeId"] == j["_id"]:  # No need for rrr not in j["reviews"]
                        exp_.exp.cafes.update_one( { "_id": j["_id"] },
                            { "$addToSet": { "reviews": rrr } }  )

    #if c_r in cafes_list["_id"]

#with open("file.html", "r") as f:
    #html = f.read()

    #soup = BeautifulSoup(html, 'html.parser')

    #print(soup.prettify())

    #print(soup.title.text)