from django.shortcuts import render
from django.http import HttpResponse
from pages.scraping import *
from .models import *

# Create your views here.
def home_view(request, *args, **kwargs):
    #print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")
    player_list = get_top_players()
    goalie_list = get_top_goalies()
    context = {
        "player": player_list,
        "goalie": goalie_list
    }
    return render(request, "index.html", context)

def all_view(request, *args, **kwargs):
    #print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")
    player_list = get_full_table()
    
    context = {
        "list": player_list
    }
    return render(request, "nhl.html", context)

def fantasy_view(request, *args, **kwargs):
    #update_row()
    obj = custom_sql()
    
    context = {
        'test': obj
    }
    return render(request, "fantasy.html", context)
