from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from .models import PlayersModel, GameModel, WinnerModel
from .forms import SignupForm
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from random import randint
from django.core import serializers

@csrf_exempt

# Create your views here.

def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            players = PlayersModel.objects.filter(username=data['username'])
            if len(players) == 0:
                print players
                player = PlayersModel(firstname=data['firstname'], lastname=data['lastname'], email=data['email'],
                                      username=data['username'], password=data['password'])
                player.save()
                return HttpResponse("You have created a User")
            return HttpResponse("User Already Exists", status=250)
        except:
            return HttpResponse("There was an error", status=201)

    else:
        return HttpResponse("Not a valid request.", status=201)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        player = PlayersModel.objects.filter(username=data['username'], password=data['password'])
        if len(player) == 1:
            print player.values('username')[0]['username']
            return HttpResponse(player.values('username')[0]['username'])
        return HttpResponse("Invalid Username", status=250)
    else:
        return HttpResponse("Not a valid request.", status=201)

@csrf_exempt
def click(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        newClick = GameModel(username=data['username'])
        newClick.save()
        return HttpResponse("Clicked!")
    else:
        return HttpResponse("Not a valid request.", status=201)

@csrf_exempt
def myclicks(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        allclicks = GameModel.objects.all()
        playerslength = len(allclicks.values()) / 1000 * 1000
        playerclicks = GameModel.objects.filter(username=data['username']).filter(id__gt=playerslength)
        return HttpResponse((len(playerclicks.values())))
    else:
        return HttpResponse("Not a valid request.", status=201)

@csrf_exempt
def totalclicks(request):
    if request.method == 'POST':
        playerclicks = GameModel.objects.all()
        playerslength = len(playerclicks.values()) % 1000
        return HttpResponse(playerslength)
    else:
        return HttpResponse("Not a valid request.", status=201)

@csrf_exempt
def checkwinner(request):
    if request.method == 'POST':
        playerclicks = GameModel.objects.all()
        playerslength = len(playerclicks.values())
        if playerslength % 1000 == 0:
            winningnumber = randint(playerslength / 1000 * 1000 - 1000,playerslength / 1000 * 1000)
            print winningnumber
            print playerclicks.values('username')[winningnumber]['username']
            winner = WinnerModel(username=playerclicks.values('username')[winningnumber]['username'])
            winner.save()
            HttpResponse('There has been a new winner!')
        return HttpResponse('No Winner')
    else:
        return HttpResponse("Not a valid request.", status=201)

@csrf_exempt
def gamewinners(request):
    if request.method == 'POST':
        winners = serializers.serialize('json', WinnerModel.objects.all())
        return HttpResponse(winners)
    else:
        return HttpResponse("Not a valid request.", status=201)