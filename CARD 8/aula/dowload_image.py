# task 4 do video 
# so fiz os imports peguei o HTML dnv e depois extrai a imagem lake do site
import requests
from bs4 import BeautifulSoup as bs

url = 'https://keithgalli.github.io/web-scraping/'
r = requests.get(url + 'webpage.html') 

webpage = bs(r.content)

images = webpage.select("div.row div.column img")
image_url = images[0]['src']
full_url = url + image_url
# tudo acima só foi para organizar a url
img_data = requests.get(full_url).content # faz a requisiç~çao e pega a url
with open('lake_como.jpg', 'wb') as handler: # cria o lake_como.jpeg e escreve o wb write binary escrever em binário
    handler.write(img_data) # salava o arquivo

