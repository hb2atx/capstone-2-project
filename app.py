import requests
from bs4 import BeautifulSoup as bs
from flask import Flask
from models import db, connect_db, PlayerInfo, PlayerStats
from pprint import pprint

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///overpaid'


connect_db(app)

all_info = {}

url = "https://www.basketball-reference.com/contracts/players.html"
r = requests.get(url)

soup = bs(r.text, "html.parser")
rows = soup.find_all("td", {'class': 'left', 'data-stat': 'player'})
player_names = [td.find('a').text for td in rows if td.find('a')]

current_salaries = soup.find_all("td", {'class': 'right', 'data-stat': 'y1'})
current_salaries = [td.text for td in current_salaries if td.text]

players_with_salaries = dict(zip(player_names, current_salaries))
pprint(players_with_salaries)
stats_request = requests.get("https://www.basketball-reference.com/leagues/NBA_2024_per_game.html")

soup_two = bs(stats_request.text, "html.parser")
stats = soup_two.find_all("tr", {'class': 'full_table'})

my_set = set()

for row in stats:
    name = row.find("td", {'data-stat': 'player'}).text
    if not name or not players_with_salaries.get(name):
        continue
    if name in my_set:
        continue
    my_set.add(name)

    all_info[name] = {
        'salary': players_with_salaries[name],
        'stats': {
            'games_played': row.find("td", {'data-stat': "g"}).text,
            'points_per_game': row.find("td", {'data-stat': 'pts_per_g'}).text,
            'assists_per_game': row.find("td", {'data-stat': 'ast_per_g'}).text,
            'defensive_rebounds_per_game': row.find("td", {'data-stat': 'drb_per_g'}).text,
            'offensive_rebounds_per_game': row.find("td", {'data-stat': 'orb_per_g'}).text,
            'total_rebounds_per_game': row.find("td", {'data-stat': 'trb_per_g'}).text,
            'steals_per_game': row.find("td", {'data-stat': 'stl_per_g'}).text,
            'turnovers_per_game': row.find("td", {'data-stat': 'tov_per_g'}).text,
            'blocks_per_game': row.find("td", {'data-stat': 'blk_per_g'}).text,
            'turnovers_per_game': row.find("td", {'data-stat': 'tov_per_g'}).text,
            'minutes_per_game': row.find("td", {'data-stat': 'mp_per_g'}).text,
            'two_point_field_goals_per_game': row.find("td", {'data-stat': 'fg2_per_g'}).text,
            'two_point_field_goal_attempts_per_game': row.find("td", {'data-stat': 'fg2a_per_g'}).text,
            'two_point_field_goal_percentage': row.find("td", {'data-stat': 'fg2_pct'}).text,
            'field_goals_per_game': row.find("td", {'data-stat': 'fg_per_g'}).text,
            'field_goal_attempts_per_game': row.find("td", {'data-stat': 'fga_per_g'}).text,
            'field_goal_percentage': row.find("td", {'data-stat': 'fg_pct'}).text,
            'three_point_percentage': row.find("td", {'data-stat': 'fg3_pct'}).text,
            'three_point_field_goal_attempts_per_game': row.find("td", {'data-stat': 'fg3a_per_g'}).text,
            'three_point_field_goals_per_game': row.find("td", {'data-stat': 'fg3_per_g'}).text,
            'free_throw_attempts_per_game': row.find("td", {'data-stat': 'fta_per_g'}).text,
            'free_throws_per_game': row.find("td", {'data-stat': 'ft_per_g'}).text,
            'free_throw_percentage': row.find("td", {'data-stat': 'ft_pct'}).text,
            'players_name': row.find("td", {'data-stat': 'player'}).text,
            'position': row.find("td", {'data-stat': 'pos'}).text,
            'age' : row.find("td", {'data-stat': 'age'}).text,
            'team_id' : row.find("td", {'data-stat': 'team_id'}).text,
            'name': row.find("td", {'data-stat': 'player'}).text
            
            }
            
            }
    for key, value in all_info.items():
   
        players_stats = PlayerStats(
            position = value['stats'].get('position', 'no_position'),
            games_played = value['stats'].get('games_played', 'no_games_played'),
            points_per_game = value['stats'].get('points_per_game', 'no points per game'),
            assists_per_game = value['stats'].get('assists_per_game', 'no assists'),
            turnovers_per_game = value['stats'].get('turnovers_per_game', 'no turnovers'),
            defensive_rebounds_per_game = value['stats']['defensive_rebounds_per_game'] or 0,
            offensive_rebounds_per_game = value['stats']['offensive_rebounds_per_game'] or 0,
            total_rebounds_per_game = value['stats']['total_rebounds_per_game'] or 0,
            steals_per_game = value['stats']['steals_per_game'] or 0,
            blocks_per_game = value['stats']['blocks_per_game'] or 0,
            minutes_per_game = value['stats']['minutes_per_game'] or 0,
            two_point_field_goals_per_game = value['stats']['two_point_field_goals_per_game'] or 0,
            two_point_field_goal_percentage = value['stats']['two_point_field_goal_percentage'] or 0,
            two_point_field_goal_attempts_per_game = value['stats']['two_point_field_goal_attempts_per_game'] or 0,
            field_goal_percentage = value['stats']['field_goal_percentage'] or 0,
            field_goal_attempts_per_game = value['stats']['field_goal_attempts_per_game'] or 0,
            field_goals_per_game = value['stats']['field_goals_per_game'] or 0,
            three_point_field_goal_attempts_per_game = value['stats']['three_point_field_goal_attempts_per_game'] or 0,
            three_point_field_goals_per_game = value['stats']['three_point_field_goals_per_game'] or 0,
            three_point_percentage = value['stats']['three_point_percentage'] or 0,
            free_throw_attempts_per_game = value['stats']['free_throw_attempts_per_game'] or 0,
            free_throws_per_game = value['stats']['free_throws_per_game'] or 0,
            free_throw_percentage = value['stats']['free_throw_percentage'] or 0
    )
        db.session.add(players_stats)
        db.session.commit()

        salary_string = players_with_salaries.get(name, '0')
        salary_numeric = float(salary_string.replace('$', '').replace(',', ''))

        players_name = value['stats'].get('name', 'no name')
        existing_player = PlayerInfo.query.filter_by(players_name=players_name).first()
        if existing_player is None:
            players_info = PlayerInfo(
                players_name=players_name,
                age = value['stats'].get('age', 'no age'),
                position = value['stats'].get('position', 'no position'),
                team = value['stats'].get('team_id', 'no team'),
                player_salary= salary_numeric
                )
            db.session.add(players_info)
            db.session.commit()

        


       



  
  

   
    




