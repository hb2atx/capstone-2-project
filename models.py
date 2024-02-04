from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    with app.app_context():
        db.app = app
        db.init_app(app)
        db.drop_all()
        db.create_all()

    
class PlayerStats(db.Model):

    __tablename__ = "players_stats"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    players_name = db.Column(db.String,nullable=False,unique=True)
    position = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    team = db.Column(db.String)
    games_played = db.Column(db.Float)
    games_started = db.Column(db.Float)
    minutes_per_game = db.Column(db.Float)
    field_goals_per_game = db.Column(db.Float)
    field_goal_attempts_per_game = db.Column(db.Float, nullable=False)
    field_goal_percentage = db.Column(db.Float,nullable=False)
    three_point_field_goals_per_game = db.Column(db.Float, nullable=False)
    three_point_field_goal_attempts_per_game = db.Column(db.Float, nullable=False)
    three_point_percentage = db.Column(db.Float,nullable=False)
    two_point_field_goals_per_game = db.Column(db.Float, nullable=False)
    two_point_field_goal_attempts_per_game = db.Column(db.Float, nullable=False)
    two_point_field_goal_percentage = db.Column(db.Float, nullable=False)
    free_throws_per_game = db.Column(db.Float, nullable=False)
    free_throw_attempts_per_game = db.Column(db.Float, nullable=False)
    free_throw_percentage = db.Column(db.Float,nullable=False)
    offensive_rebounds_per_game = db.Column(db.Float, nullable=False)
    defensive_rebounds_per_game = db.Column(db.Float, nullable=False)
    total_rebounds_per_game = db.Column(db.Float,nullable=False)
    assists_per_game = db.Column(db.Float,nullable=False)
    steals_per_game = db.Column(db.Float,nullable=False)
    blocks_per_game = db.Column(db.Float,nullable=False)
    turnovers_per_game = db.Column(db.Float, nullable=False)
    points_per_game = db.Column(db.Float,nullable=False)

class AvgStats(db.Model):

    __tablename__ = "avg_stats"

    id = db.Column(db.Integer, primary_key=True)
    avg_salary = db.Column(db.Float)
    position = db.Column(db.String(2), unique=True)
    avg_games_played = db.Column(db.Float)
    avg_points_per_game = db.Column(db.Float)
    avg_games_started_per_game = db.Column(db.Float)
    avg_minutes_per_game = db.Column(db.Float)
    avg_field_goals_per_game = db.Column(db.Float)
    avg_field_goal_attempts_per_game = db.Column(db.Float)
    avg_field_goal_percentage = db.Column(db.Float)
    avg_three_point_field_goals_per_game = db.Column(db.Float)
    avg_three_point_field_goal_attempts_per_game = db.Column(db.Float)
    avg_three_point_percentage = db.Column(db.Float)
    avg_two_point_field_goals_per_game = db._game = db.Column(db.Float)
    avg_two_point_field_goal_attempts_per_game = db._game = db.Column(db.Float)
    avg_two_point_field_goal_percentage = db.Column(db.Float)
    avg_free_throw_attempts_per_game = db.Column(db.Float)
    avg_free_throws_per_game = db.Column(db.Float)
    avg_free_throw_percentage_per_game = db.Column(db.Float)
    avg_offensive_rebounds_per_game = db.Column(db.Float)
    avg_defensive_rebounds_per_game = db.Column(db.Float)
    avg_total_rebounds_per_game = db.Column(db.Float)
    avg_assists_per_game = db.Column(db.Float)
    avg_steals_per_game = db.Column(db.Float)
    avg_avg_blocks_per_game = db.Column(db.Float)
    avg_turnovers_per_game = db.Column(db.Float)
    avg_points_per_game = db.Column(db.Float)
    
   
  


 





    



    




    
    
    
    
    


