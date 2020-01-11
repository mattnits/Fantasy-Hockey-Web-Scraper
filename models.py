from django.db import models, connection
from pages.scraping import *
from pages.player import Player
from pages.goalie import Goalie

# Create your models here.


class Temp(models.Model):
    pid = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp'

def custom_sql():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM player")
        row = cursor.fetchone()

        return row

def add_player_data():
    cnt = 1
    with connection.cursor() as cursor:
        player_list = getOtherData()
        for i in player_list:
            sql = """
            INSERT INTO player_stats
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            params = [1, i.goals, i.assists, i.points, i.pm, i.shp, i.ppp, i.gwg, i.hit, i.blk, i.sog, i.pim, cnt]
            cursor.execute(sql, params)
            cnt = cnt + 1

def add_goalie_data():
    cnt = 810
    with connection.cursor() as cursor:
        goalie_list = getOtherGoalieData()
        for i in goalie_list:
            sql = """
            INSERT INTO goalie_stats
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            params = [2, i.wins, i.losses, i.ga, i.sv, i.sho, cnt, i.otl, i.svpct, i.gaa]
            cursor.execute(sql, params)
            cnt = cnt + 1

def get_full_table():
     with connection.cursor() as cursor:
        sql = """
        SELECT name, position, fpoints, avgfpoints, gamesplayed, goals, assists, points, plusminus, penaltyminutes, powerplaypoints, shorthandedpoints, 
        gamewinninggoals, shots, hits, blocks FROM player AS P
        INNER JOIN player_stats as ps
        ON ps.playerid = p.playerid AND ps.positionid = p.positionid
        ORDER BY fpoints DESC, avgfpoints DESC, points, goals, assists
        limit 50
        """
        cursor.execute(sql)
        rows = cursor.fetchall()

        return rows

def get_top_players():
    with connection.cursor() as cursor:
        sql = """
        SELECT name, position, gamesplayed, fpoints, goals, assists, points FROM player AS P
        INNER JOIN player_stats as ps
        ON ps.playerid = p.playerid AND ps.positionid = p.positionid
        ORDER BY fpoints DESC, gamesplayed, points, goals, assists
        limit 10
        """
        cursor.execute(sql)
        rows = cursor.fetchall()

        return rows

def get_top_goalies():
    with connection.cursor() as cursor:
        sql = """
        SELECT name, position, fpoints, gamesplayed, wins, losses, savepercentage FROM player AS P
        INNER JOIN goalie_stats as gs
        ON gs.playerid = p.playerid AND gs.positionid = p.positionid
        ORDER BY fpoints DESC, gamesplayed, wins, losses, savepercentage
        limit 10
        """
        cursor.execute(sql)
        rows = cursor.fetchall()

        return rows

def alter_player():
    getData()
    player_list = getOtherData()
    with connection.cursor() as cursor:
        sql = """
        UPDATE player as p
        SET gamesplayed = %s, fpoints = %s, avgfpoints = %s,
        WHERE p.positionid = "1" AND name = %s
        """
        params = [player_list.gp, player_list.fpoints, player_list.avgfpoints, player_list.name]
        cursor.execute(sql, params)

    
        