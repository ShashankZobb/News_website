from django.shortcuts import render
import requests
from django.contrib import messages
key = "9c88f996ef7b2aa0135a3c0341d83c68"
country_code = {"argentina":"ar", "australia":"au","austria":"at","belgium":"be","brazil":"br","belgium":"be","canada":"ca","china":"cn","colombia":"co", "czech republic": "cz", "egypt":"eg","frace":"fr","germany":"gr","hong kong":"hk","hunrgy":"hu","india":"id","indonesia":"id","ireland":"ie","israel":"il","italy":"it","japan":"jp","latavia":"lv","mexico":"mx","united states":"us", "united kingdom":"gb","sweden":"se","switzerland":"ch","south korea":"kr","singapore":"sg","taiwan":"tw","norway":"no","ukraine":"ua", "uae":"ae","thailand":"th","poland":"pl"}
def index(request):
    country = "in"
    if request.method == "POST":
        country1 = request.POST.get("countryname")
        print(country1)
        if country1 != None and len(country1) > 0:
            if country1 in country_code:
                country = country_code[country1.lower()]
            else:
                messages.info(request, "Sorry the country is not available")
        else:
            messages.info(request, "Sorry the country is not available")
        
    news_url = "http://api.mediastack.com/v1/news?access_key="+key+"&countries="+country
    title = []
    url = []
    image = []
    description = []
    news_data = {}
    news_data = requests.get(news_url).json()
    if news_data.get('data') != None:
        data = news_data['data']
        for i in data:
            title.append(i['title'])
            url.append(i['url'])
            if i.get('image') != None:
                image.append(i['image'])
            else:
                image.append('https://thumbs.dreamstime.com/b/no-image-available-icon-flat-vector-no-image-available-icon-flat-vector-illustration-132482953.jpg')
            description.append(i['description'])
    else:
        messages.info(request, "Sorry the country is not available")
    news = zip( title, url,image, description)
    return render(request, 'index.html', context={'news': news})

