from django.shortcuts import render
import requests
import datetime
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def index(request):
    
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'İzmir'    
    
    appid = '8dc024d11e5cad90fe564ff6c2b72b61'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    response = r.json()
    description = response['weather'][0]['description']
    icon = response['weather'][0]['icon']
    temp = response['main']['temp']
    day = datetime.date.today()

    
    
    return render(request, 'weathapp/index.html', {'description':description, 'icon':icon, 
        'temp':temp, 'day':day, 'city':city  })







