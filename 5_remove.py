import json
import requests

t= "/Users/manishpargai/Documents/scrap/r.test.reviews.json"
r= "/Users/manishpargai/Documents/scrap/exp.reviews.json"

with open(t, "r", encoding="utf-8") as f:
   t_path = json.load(f)

with open(r, "r", encoding="utf-8") as f:
   r_path = json.load(f)

 

#print(r_path)
it=[] 
only_it_id=[] 
for i in range(len(t_path)):
    it = t_path[i]
    only_it_id.append(it["_id"])

for j in range(len(r_path)):
   ir = r_path[j]
   if ir["_id"] not in only_it_id:
        url = 'https://experince.in/bhoe/weight'

        reviewIdd= str(ir["_id"])
        reviewIddd = reviewIdd.replace("{'$oid':","").replace("}","").replace("'","").strip()
        cafesIdd= str(ir["cafeId"])
        cafesIddd = cafesIdd.replace("{'$oid':","").replace("}","").replace("'","").strip()
        revieww = str(ir["review"])
        ratingAmbiencee= int(ir["ratingAmbience"])
        ratingFoodd= int(ir["ratingFood"])
        ratingDrinkk= int(ir["ratingDrink"])
        ratingServicee= int(ir["ratingService"])

        myobj = {
                'cafeId': cafesIddd,
                "reviewId":reviewIddd,
                "ratingAmbience": ratingAmbiencee,
                "ratingFood": ratingFoodd,
                "ratingDrink":ratingDrinkk,
                "ratingService": ratingServicee,
                "review": revieww,
                
               }

        
        x = requests.post(url, json = myobj)
        print(x.text)
        
print("done")
        
            




