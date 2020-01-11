import requests
import csv
import json
import operator
from pages.player import Player
from pages.goalie import Goalie
#https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database
#https://linuxize.com/post/how-to-create-mysql-user-accounts-and-grant-privileges/
#https://www.computerhope.com/issues/ch001662.htm


def getData():
    a1 = "https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goals%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22assists%22,%22direction%22:%22DESC%22%7D%5D&start=0&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    a2 = "https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goals%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22assists%22,%22direction%22:%22DESC%22%7D%5D&start=100&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    a3 = "https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goals%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22assists%22,%22direction%22:%22DESC%22%7D%5D&start=200&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    a4 = "https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goals%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22assists%22,%22direction%22:%22DESC%22%7D%5D&start=300&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    a5 = "https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goals%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22assists%22,%22direction%22:%22DESC%22%7D%5D&start=400&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    a6 = "https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goals%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22assists%22,%22direction%22:%22DESC%22%7D%5D&start=500&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    a7 = "https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goals%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22assists%22,%22direction%22:%22DESC%22%7D%5D&start=600&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    a8 = "https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goals%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22assists%22,%22direction%22:%22DESC%22%7D%5D&start=700&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    a9 = "https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goals%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22assists%22,%22direction%22:%22DESC%22%7D%5D&start=800&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"

    b1 = "https://api.nhle.com/stats/rest/en/skater/realtime?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22hits%22,%22direction%22:%22DESC%22%7D%5D&start=0&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    b2 = "https://api.nhle.com/stats/rest/en/skater/realtime?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22hits%22,%22direction%22:%22DESC%22%7D%5D&start=100&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    b3 = "https://api.nhle.com/stats/rest/en/skater/realtime?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22hits%22,%22direction%22:%22DESC%22%7D%5D&start=200&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    b4 = "https://api.nhle.com/stats/rest/en/skater/realtime?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22hits%22,%22direction%22:%22DESC%22%7D%5D&start=300&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    b5 = "https://api.nhle.com/stats/rest/en/skater/realtime?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22hits%22,%22direction%22:%22DESC%22%7D%5D&start=400&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    b6 = "https://api.nhle.com/stats/rest/en/skater/realtime?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22hits%22,%22direction%22:%22DESC%22%7D%5D&start=500&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    b7 = "https://api.nhle.com/stats/rest/en/skater/realtime?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22hits%22,%22direction%22:%22DESC%22%7D%5D&start=600&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    b8 = "https://api.nhle.com/stats/rest/en/skater/realtime?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22hits%22,%22direction%22:%22DESC%22%7D%5D&start=700&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    b9 = "https://api.nhle.com/stats/rest/en/skater/realtime?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22hits%22,%22direction%22:%22DESC%22%7D%5D&start=800&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"

    file_handle = csv.writer(open("stats.csv", "w+", newline = ""))
    addresses = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
    file_handle.writerow(["PLAYERS"])
    for j in addresses:
        stuff = requests.get(j).content

        json_data = json.loads(stuff)['data']
        
        for i in json_data:
            team = i["teamAbbrevs"]
            t = team.split(",")
            if len(t) > 1:
                t = t[1].strip("[',']")
            else:
                t = t[0].strip("[',']")
            file_handle.writerow([i["skaterFullName"], i["gamesPlayed"] ,i["goals"], i["assists"], i["points"], \
            i["plusMinus"], i["penaltyMinutes"], i["ppPoints"], i["shPoints"], i["gameWinningGoals"], i["shots"], "0", "0",t , i["positionCode"]])

    file_handle2 = csv.writer(open("stats0.csv", "w+", newline = ""))
    addresses2 = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    
    for x in addresses2:
        stuff2 = requests.get(x).content

        json_data2 = json.loads(stuff2)['data']
        for y in json_data2:
            file_handle2.writerow([y["skaterFullName"], y["hits"], y["blockedShots"]])

def getOtherData():
    
    player_list2 = []
    temp_list = []
    cnt = 0
    with open("stats.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if (cnt != 0):
                name = ""
                num = 0
                s = str(row)
                t = s.split()
                temp = t[num].strip("[','\"")
                if not temp.isalpha():
                    temp = temp.replace(".", "")
                    temp = temp.replace("-", "")
                while temp.isalpha():
                    if (name == ""):
                        name = name + t[num].strip("[','\"")
                    else:
                        name = name + " " + t[num].strip("[','\"")
                    num = num + 1
                    temp = t[num].strip("[','\"")
                    temp = temp.replace("'", "")
                    temp = temp.replace("-", "")
                    
                temp2 = Player(name, float(t[num].strip("' ',]")), int(t[num + 1].strip("' ',]")), int(t[num + 2].strip("' ',")), \
                    int(t[num + 3].strip("' ',")), int(t[num + 4].strip("' ',")), int(t[num + 5].strip("' ',")), int(t[num + 6].strip("' ',")), int(t[num + 7].strip("' ',")), \
                        int(t[num + 8].strip("' ',")), int(t[num + 9].strip("' ',")), int(t[num + 10].strip("' ',")), int(t[num + 11].strip("' ',]")), (t[num + 12].strip("' ',]")), \
                             (t[num + 13].strip("' ',]")))
                
                player_list2.append(temp2)
            cnt = cnt + 1
        player_list2 = sorted(player_list2, key=operator.attrgetter("name"))

    with open("stats0.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if (cnt != 0):
                name = ""
                num = 0
                s = str(row)
                t = s.split()
                temp = t[num].strip("[','\"")
                if not temp.isalpha():
                    temp = temp.replace(".", "")
                    temp = temp.replace("-", "")
                while temp.isalpha():
                    if (name == ""):
                        name = name + t[num].strip("[','\"")
                    else:
                        name = name + " " + t[num].strip("[','\"")
                    num = num + 1
                    temp = t[num].strip("[','\"")
                    temp = temp.replace("'", "")
                    temp = temp.replace("-", "")
                temp_list.append(Player(name, 0, 1, 2,3,4,5,6,7,8,9,int(t[num + 1].strip("' ',]")), int(t[num].strip("' ',]")), "null", "null"))
            cnt = cnt + 1
        temp_list = sorted(temp_list, key=operator.attrgetter("name"))

    for i in range(0, len(player_list2) -1, 1):
        player_list2[i].update_blocks_hits(temp_list[i].hit, temp_list[i].blk)


    return player_list2


def getGoalieData():
    address = "https://api.nhle.com/stats/rest/en/goalie/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22wins%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22savePct%22,%22direction%22:%22DESC%22%7D%5D&start=0&limit=76&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020"
    stuff = requests.get(address).content
    file_handle = csv.writer(open("stats1.csv", "w+", newline = ""))
    json_data = json.loads(stuff)['data']
    
    for i in json_data:
        file_handle.writerow([i["goalieFullName"], i["gamesPlayed"], i["wins"], i["losses"], i["otLosses"], i["goalsAgainst"], i["saves"], \
            i["shutouts"], i["savePct"], i["goalsAgainstAverage"], i["teamAbbrevs"]])

def getOtherGoalieData():
    goalie_list = []
    with open("stats1.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = ""
            num = 0
            s = str(row)
            t = s.split()
            temp = t[num].strip("[','\"")
            if not temp.isalpha():
                temp = temp.replace(".", "")
                temp = temp.replace("-", "")
            while temp.isalpha():
                if (name == ""):
                    name = name + t[num].strip("[','\"")
                else:
                    name = name + " " + t[num].strip("[','\"")
                num = num + 1
                temp = t[num].strip("[','\"")
                temp = temp.replace("'", "")
                temp = temp.replace("-", "")
            temp2 = Goalie(name, int(t[num].strip("' ',]")), int(t[num + 1].strip("' ',]")), int(t[num + 2].strip("' ',")), \
                    int(t[num + 3].strip("' ',")), int(t[num + 4].strip("' ',")), int(t[num + 5].strip("' ',")), int(t[num + 6].strip("' ',")), float(t[num + 7].strip("' ',")), \
                        float(t[num + 8].strip("' ',")), (t[num + 9].strip("' ',]")))
            
            goalie_list.append(temp2)
        goalie_list = sorted(goalie_list, key=operator.attrgetter("name"))

        return goalie_list

def getTeamInfo():
    address = "https://d290qmen6zswb.cloudfront.net/web_standings?league=nhl&season=2019"
    team = []

    with open("stats.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)