import requests
import json

# kullanıcıdan hangi şehir veya ülke hava durumunu istediğini soruyoruz.
sehir_ismi = input("lütfen şehir ismi giriniz : ")
# bu api key sizin kişisel apikey numaranız olmalı o yüzden bu şekilde paylaştım 
# nasıl apikey alabilirsiniz bunuda açıklamalar kısmında anlattım.
api_key = ""


# gelen verinin linki
url = f"https://api.openweathermap.org/data/2.5/weather?q={sehir_ismi}&appid={api_key}&lang=tr"


gelen_veri = requests.get(url)
gvj = gelen_veri.json()

if gvj["cod"] != "404":
    temp = gvj["main"]["temp"]
    description = gvj["weather"][0]["description"]
    feels_like = gvj["main"]["feels_like"]

    print("sıcaklık : " +str(round(float(temp)-273.15 , 2)))
    print("hissedilen : " + str(round(float(feels_like)-273.15 , 2)))
    print("hava durumu : " + str(description))
else:
    print("böyle bir şehir bulunamadı") 
