from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    with app.app_context():
        db.app = app
        db.init_app(app)
        db.drop_all()
        db.create_all()


class PlayerInfo(db.Model):

    __tablename__ = "players_info"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    players_name = db.Column(db.String,nullable=False,unique=True)
    age = db.Column(db.Integer,nullable=False)
    position = db.Column(db.String,nullable=False)
    team = db.Column(db.String,nullable=False)
    player_salary = db.Column(db.Float, nullable=False)
    
class PlayerStats(db.Model):

    __tablename__ = "players_stats"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    position = db.Column(db.String, nullable=False)
    games_played = db.Column(db.Integer,nullable=False)
    minutes_per_game = db.Column(db.Float,nullable=False)
    field_goal_attempts_per_game = db.Column(db.Float, nullable=False)
    field_goal_percentage = db.Column(db.Float,nullable=False)
    field_goals_per_game = db.Column(db.Float, nullable=False)
    two_point_field_goals_per_game = db.Column(db.Float, nullable=False)
    two_point_field_goal_attempts_per_game = db.Column(db.Float, nullable=False)
    two_point_field_goal_percentage = db.Column(db.Float, nullable=False)
    three_point_field_goal_attempts_per_game = db.Column(db.Float, nullable=False)
    three_point_field_goals_per_game = db.Column(db.Float, nullable=False)
    three_point_percentage = db.Column(db.Float,nullable=False)
    free_throw_attempts_per_game = db.Column(db.Float, nullable=False)
    free_throws_per_game = db.Column(db.Float, nullable=False)
    free_throw_percentage = db.Column(db.Float,nullable=False)
    total_rebounds_per_game = db.Column(db.Float,nullable=False)
    offensive_rebounds_per_game = db.Column(db.Float, nullable=False)
    defensive_rebounds_per_game = db.Column(db.Float, nullable=False)
    assists_per_game = db.Column(db.Float,nullable=False)
    steals_per_game = db.Column(db.Float,nullable=False)
    blocks_per_game = db.Column(db.Float,nullable=False)
    points_per_game = db.Column(db.Float,nullable=False)
    turnovers_per_game = db.Column(db.Float, nullable=False)


    




    
    
    
    
    


