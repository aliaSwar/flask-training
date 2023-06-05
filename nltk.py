from  bs4 import BeautifulSoup as bs
from urllib.request import urlopen
url="https://translate.google.nl/?hl=en&tab=rT&sl=en&tl=ar&op=translate"
clent=urlopen(url)
html=clent.read()
clent.close()
soup=bs(html,'html.parser')
print(soup)
container=soup.find_all("div",{"class":""})
bs.prettify(container[1])




