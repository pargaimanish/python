import requests
import time
from fake_useragent import UserAgent 


url = "https://www.flipkart.com/"

session = requests.session() 
proxy_auth = '3c617fdc66b92fe43e6f:9ca3640b1de7273f@gw.dataimpulse.com:823'

proxies = {
    'https': f'https://{proxy_auth}', 'http': f'http://{proxy_auth}'
}

headers = {
'User-Agent': UserAgent().random,

'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

'Accept-Language': 'en-US,en;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Referer': 'https://google.com/'

}
time.sleep(2)
r = session.get(url)
#print(r.text)
with open ("file.html", "w") as f :
    f.write(r.text)
