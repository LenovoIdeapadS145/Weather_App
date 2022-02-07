import requests
from django.shortcuts import render
from .forms import CityForm
from .models import City
# Create your views here.

def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=04b873d0975d6895c5a4310023e3dd74"
    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    City_Name = City.objects.all()
    Weather_Data = []
    for i in City_Name:
        try:
            R = requests.get(url.format(i)).json()
            City_Weather = {"City" : i.name,
                            "Temperature" : R["main"]["temp"],
                            "Description" : R["weather"][0]["description"],
                            "Icon" : R["weather"][0]["icon"]}
        except:
            pass
        else:
            Weather_Data.append(City_Weather)
    
    X = {"Weather_Data" : Weather_Data,
         "form" : form}


    return render(request,"Weather/Weather.html", X)