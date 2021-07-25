from .app import db


# class Pet(db.Model):
#     __tablename__ = 'pets'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))
#     lat = db.Column(db.Float)
#     lon = db.Column(db.Float)

#     def __repr__(self):
#         return '<Pet %r>' % (self.name)


class ADP_DATA(db.Model):
    __tablename__ = 'ADP_DATA'

    FantasyPlayerKey = db.Column(db.text, primary_key=True)
    PlayerID = db.Column(db.bigint)
    Name = db.Column(db.text)
    Team = db.Column(db.text)
    Position = db.Column(db.text)
    AverageDraftPosition = db.Column(db.double precision)
    AverageDraftPositionPPR = db.Column(db.double precision)
    ByeWeek = db.Column(db.double precision)
    LastSeasonFantasyPoints = db.Column(db.double precision)
    ProjectedFantasyPoints = db.Column(db.double precision)
    AuctionValue = db.Column(db.bigint)
    AuctionValuePPR = db.Column(db.bigint)
    AverageDraftPositionIDP = db.Column(db.double precision)
    AverageDraftPositionRookie = db.Column(db.double precision)
    AverageDraftPositionDynasty = db.Column(db.double precision)
    AverageDraftPosition2QB = db.Column(db.double precision)
    
    def __repr__(self):
        return '<ADP_DATA %r>' % (self.name)

class BoxPlot(db.Model):
    __tablename__ = 'BoxPlot'

    NAME = db.Column(db.text, primary_key=True)
    POSITION = db.Column(db.text)
    PROJECTED_POINTS = db.Column(db.double precision)
    
    
    def __repr__(self):
        return '<BoxPlot %r>' % (self.name)

class DEF_Data(db.Model):
    __tablename__ = 'DEF_Data'

    Name = db.Column(db.text)
    Team = db.Column(db.text)
    Position = db.Column(db.text)
    AverageDraftPosition = db.Column(db.double precision)
    AverageDraftPositionPPR = db.Column(db.double precision)
    ByeWeek = db.Column(db.double precision)
    LastSeasonFantasyPoints = db.Column(db.double precision)
    ProjectedFantasyPoints = db.Column(db.double precision)

    def __repr__(self):
        return '<DEF_DATA %r>' % (self.name)

class Highlights_Data(db.Model):
    __tablename__ = 'Highlights_Data'

    Name = db.Column(db.text)
    Team = db.Column(db.text)
    Position = db.Column(db.text)
    AverageDraftPosition = db.Column(db.double precision)
    AverageDraftPositionPPR = db.Column(db.double precision)
    ByeWeek = db.Column(db.double precision)
    LastSeasonFantasyPoints = db.Column(db.double precision)
    ProjectedFantasyPoints = db.Column(db.double precision)

    def __repr__(self):
        return 'Highlights_Data %r>' % (self.name)

class K_Data(db.Model):
    __tablename__ = 'K_Data'

    Name = db.Column(db.text)
    Team = db.Column(db.text)
    Position = db.Column(db.text)
    AverageDraftPosition = db.Column(db.double precision)
    AverageDraftPositionPPR = db.Column(db.double precision)
    ByeWeek = db.Column(db.double precision)
    LastSeasonFantasyPoints = db.Column(db.double precision)
    ProjectedFantasyPoints = db.Column(db.double precision)

    def __repr__(self):
        return 'K_Data %r>' % (self.name)

class Position_dropdown(db.Model):
    __tablename__ = 'Position_dropdown'
    
    Position = db.Column(db.text)
    
    def __repr__(self):
        return 'Position_dropdown %r>' % (self.name)

class QB_Data(db.Model):
    __tablename__ = 'QB_Data'

    Name = db.Column(db.text)
    Team = db.Column(db.text)
    Position = db.Column(db.text)
    AverageDraftPosition = db.Column(db.double precision)
    AverageDraftPositionPPR = db.Column(db.double precision)
    ByeWeek = db.Column(db.double precision)
    LastSeasonFantasyPoints = db.Column(db.double precision)
    ProjectedFantasyPoints = db.Column(db.double precision)

    def __repr__(self):
        return 'QB_Data %r>' % (self.name)

class RB_Data(db.Model):
    __tablename__ = 'RB_Data'

    Name = db.Column(db.text)
    Team = db.Column(db.text)
    Position = db.Column(db.text)
    AverageDraftPosition = db.Column(db.double precision)
    AverageDraftPositionPPR = db.Column(db.double precision)
    ByeWeek = db.Column(db.double precision)
    LastSeasonFantasyPoints = db.Column(db.double precision)
    ProjectedFantasyPoints = db.Column(db.double precision)

    def __repr__(self):
        return 'RB_Data %r>' % (self.name)

class TE_Data(db.Model):
    __tablename__ = 'TE_Data'

    Name = db.Column(db.text)
    Team = db.Column(db.text)
    Position = db.Column(db.text)
    AverageDraftPosition = db.Column(db.double precision)
    AverageDraftPositionPPR = db.Column(db.double precision)
    ByeWeek = db.Column(db.double precision)
    LastSeasonFantasyPoints = db.Column(db.double precision)
    ProjectedFantasyPoints = db.Column(db.double precision)

    def __repr__(self):
        return 'TE_Data %r>' % (self.name)

class WR_Data(db.Model):
    __tablename__ = 'WR_Data'

    Name = db.Column(db.text)
    Team = db.Column(db.text)
    Position = db.Column(db.text)
    AverageDraftPosition = db.Column(db.double precision)
    AverageDraftPositionPPR = db.Column(db.double precision)
    ByeWeek = db.Column(db.double precision)
    LastSeasonFantasyPoints = db.Column(db.double precision)
    ProjectedFantasyPoints = db.Column(db.double precision)

    def __repr__(self):
        return 'WR_Data %r>' % (self.name)

