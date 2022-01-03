from django.http import response
from django.shortcuts import render
from django.http.response import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
import requests
import datetime
# Create your views here.
def getEmoji(temperature):
    emoji = ""
    if temperature < 10:
        emoji = "❄️"
    elif temperature < 20:
        emoji = "🥶"
    elif temperature < 30:
        emoji = "😇"
    elif temperature < 40:
        emoji = "😅"
    elif temperature <50:
        emoji = "🥵"
    else:
        emoji = "☠️"
    return emoji
def sendEmail(request):
    apiKey = settings.API_KEY
    city = request.GET['city']
    name = request.GET['name']
    apiUrl = 'http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={APIkey}'.format(cityName = city,APIkey = apiKey)
    resp = requests.get(apiUrl)
    weather = resp.json()
    temperature = weather['main']['temp']
    temperatureInC = temperature - 273
    cTime = datetime.datetime.now()
    fTime = str(cTime.hour) + ":" + str(cTime.minute) + ":" + str(cTime.second) + " IST"
    emoji = getEmoji(temperatureInC)
    
    subject = 'Hi {name}, interested in our services.'.format(name=name)
    message = 'Temperature in {city} is {temp:.2f} C {emoji} at {time}'.format(city=city,temp=temperatureInC,emoji=emoji,time=fTime)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['shashank.srivastava25sks@gmail.com', ]
    send_mail( subject, message, email_from, recipient_list )
    return response.HttpResponse("<p>Email Sent</p><a href='/'>Go Back</a> ")
def getInput(request):
    return render(request,'index.html')

