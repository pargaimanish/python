from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://www.python.org/')

#print(r.html.links)

about = r.html.find('.tier-2', first=True)
print(about)