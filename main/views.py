from django.http import response
from django.shortcuts import render
from django.http.response import BadHeaderError, JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from smtplib import SMTPException
import requests
import datetime
from .models import ClientDetails
#Views for Main app 

#Get Emoji Related to Temperature
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

#The main function to get temperature from the weather API and send email
def sendEmail(request):
    apiKey = settings.API_KEY #APIKey
    #Get Input From Request 
    city = request.GET['city'] 
    name = request.GET['name']
    email = request.GET['email']
    #Generating API Endpoint
    apiUrl = 'http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={APIkey}'.format(cityName = city,APIkey = apiKey)
    resp = requests.get(apiUrl)
    #Parsing into JSON
    weather = resp.json()
    temperature = weather['main']['temp']
    temperatureInC = temperature - 273 #API Returns temperature in K which is converted to C.
    #formating time
    cTime = datetime.datetime.now()
    fTime = str(cTime.hour) + ":" + str(cTime.minute) + ":" + str(cTime.second) + " IST"
    
    #Getting Emoji
    emoji = getEmoji(temperatureInC)
    #Generating Mail Content
    subject = 'Hi {name}, interested in our services.'.format(name=name)
    message = 'Temperature in {city} is {temp:.2f} C {emoji} at {time}'.format(city=city,temp=temperatureInC,emoji=emoji,time=fTime)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    #Sendig Mail through Django's Inbuilt Mailing System
    try:
        send_mail( subject, message, email_from, recipient_list,fail_silently=False )
        #Saving Client Details to Database
        c = ClientDetails(username = name,email=email,temperature=temperatureInC,timeRequested = cTime)
        c.save()
        return response.HttpResponse("<p>Email Sent</p><a href='/'>Go Back</a> ")
    except BadHeaderError:
        return response.HttpResponse("<p>Invalid Header Error</p><a href='/'>Go Back</a> ")
    except SMTPException as e:
        return response.HttpResponse("<p>There was an error sending email</p><p>Error:- {error}</p><a href='/'>Go Back</a>".format(error = e))
    except:
        return response.HttpResponse("<p>Could not send mail. Try Again Later</p><a href='/'>Go Back</a>")
#View to get Input
def getInput(request):
    return render(request,'index.html')

