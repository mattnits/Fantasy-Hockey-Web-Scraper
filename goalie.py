
WINS_POINTS = 5
LOSS_POINTS = -4
GA_POINTS = -1
SV_POINTS = 0.25
SHO_POINTS = 5

metropolitan = ["WSH", "NYI", "PHI", "PIT", "CAR", "CBJ", "NYR", "NJD"]
atlantic = ["BOS", "TOR", "MTL", "FLA", "BUF", "TBL", "OTT", "DET"]
pacific = ["ARI", "VGK", "EDM", "CGY", "VAN", "ANA", "SJS", "LAK"]
central = ["STL", "COL", "WPG", "DAL", "NSH", "MIN", "CHI"]

class Goalie:
    def __init__(self, name, gp, wins, losses, otl, ga, sv, sho, svpct, gaa, team):
        self.name = name
        self.gp = gp
        self.wins = wins
        self.losses = losses
        self.ga = ga
        self.sv = sv
        self.sho = sho
        self.positionid = 2
        self.otl = otl
        self.position = "G"
        self.svpct = round(svpct, 3)
        self.gaa = round(gaa, 2)
        self.team = team
        self.teamid = 0
        self.fpoints = 0
        self.avgfpoints = 0
        self.calculate_fpoints()
        self.get_team_info()
        

    def calculate_fpoints(self):
        self.fpoints = 0
        self.avgfpoints = 0
        self.fpoints = (self.wins * WINS_POINTS) + (self.losses * LOSS_POINTS) + (self.ga * GA_POINTS) + (self.sv * SV_POINTS) + (self.sho * SHO_POINTS)
        avgfpoints = round((self.fpoints / self.gp), 2)

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