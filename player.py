GOAL_POINTS = 3
ASSIST_POINTS = 2
PM_POINTS = 1
PIM_POINTS = -0.5
PPP_POINTS = 2
SHP_POINTS = 3
GWG_POINTS = 2
SOG_POINTS = 0.30
HIT_POINTS = 0.25
BLK_POINTS = 0.5

metropolitan = ["WSH", "NYI", "PHI", "PIT", "CAR", "CBJ", "NYR", "NJD"]
atlantic = ["BOS", "TOR", "MTL", "FLA", "BUF", "TBL", "OTT", "DET"]
pacific = ["ARI", "VGK", "EDM", "CGY", "VAN", "ANA", "SJS", "LAK"]
central = ["STL", "COL", "WPG", "DAL", "NSH", "MIN", "CHI"]

class Player:

    def __init__(self, name, gp, goals, assists, points, pm, pim, ppp, shp, gwg, sog, hit, blk, team, position):
        self.name = name
        self.gp = int(gp)
        self.goals = int(goals)
        self.assists = int(assists)
        self.points = int(points)
        self.pm = int(pm)
        self.pim = int(pim)
        self.ppp = int(ppp)
        self.shp = int(shp)
        self.gwg = int(gwg)
        self.sog = int(sog)
        self.hit = int(hit)
        self.blk = int(blk)
        self.team = team
        self.teamid = 0
        self.position = position
        self.get_team_info()
        self.caluclate_fpoints()
        self.positionid = 1

    def caluclate_fpoints(self):
        self.fpoints = 0
        self.avgfpoints = 0
        self.fpoints = round(((self.goals * GOAL_POINTS) + (self.assists * ASSIST_POINTS) + (self.pm * PM_POINTS) + (self.pim * PIM_POINTS) + (self.ppp * PPP_POINTS) + (self.shp * SHP_POINTS) + (self.gwg * GWG_POINTS) + round((self.sog * SOG_POINTS), 1) + (self.hit * HIT_POINTS) + (self.blk * BLK_POINTS)), 2)
        if (self.gp != 0):
            self.avgfpoints = round(self.fpoints / float(self.gp), 2)
        else:
            self.avgfpoints = 0

    def get_team_info(self):
        cnt = 1
        for i in atlantic:
            if self.team == i:
                self.teamid = cnt
                break
            cnt = cnt + 1
        if self.teamid == 0:
           for i in metropolitan:
                if self.team == i:
                    self.teamid = cnt
                    break
                cnt = cnt + 1
        if self.teamid == 0:
           for i in pacific:
                if self.team == i:
                    self.teamid = cnt
                    break
                cnt = cnt + 1
        if self.teamid == 0:
           for i in central:
                if self.team == i:
                    self.teamid = cnt
                    break
                cnt = cnt + 1
        
    def update_blocks_hits(self, blocks, hits):
        self.blk = blocks
        self.hit = hits
        self.caluclate_fpoints()
