import requests
import pdb
from bs4 import BeautifulSoup as bs
from flask import Flask
from models import db, connect_db, PlayerStats, AvgStats
from pprint import pprint

app = Flask(__name__)
app.app_context().push()
    

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///overpaid'


connect_db(app)

all_info = {}

url = "https://www.basketball-reference.com/contracts/players.html"
r = requests.get(url)
# Scrape data for nba player names
soup = bs(r.text, "html.parser")
rows = soup.find_all("td", {'class': 'left', 'data-stat': 'player'})
player_names = [td.find('a').text for td in rows if td.find('a')]

####################################################################################################
# Nba player current salaries
current_salaries = soup.find_all("td", {'class': 'right', 'data-stat': 'y1'})
current_salaries = [td.text for td in current_salaries if td.text]

####################################################################################################
# Combining player name with their salary
players_with_salaries = dict(zip(player_names, current_salaries))

#####################################################################################################

# Scrape for player stats
stats_request = requests.get("https://www.basketball-reference.com/leagues/NBA_2024_per_game.html")
soup_two = bs(stats_request.text, "html.parser")
stats = soup_two.find_all("tr", {'class': 'full_table'})

my_set = set()

for row in stats:
    name_tags = row.find_all("td", {'data-stat': 'player'})

    if not name_tags:
        continue

    name = name_tags[0].text

    if not name or not players_with_salaries.get(name):
        continue

    if name in my_set:
        continue
    
    my_set.add(name)

    all_info[name] = {
        'salary': players_with_salaries[name],
        'stats': {
            'name' : name,
            'position' : row.find("td", {'data-stat': 'pos'}).text,
            'age' : row.find("td", {'data-stat': 'age'}).text,
            'team' : row.find("td", {'data-stat': 'team_id'}).text,
            'games_played': row.find("td", {'data-stat': "g"}).text,
            'games_started': row.find("td", {'data-stat': 'gs'}).text,
            'minutes_per_game': row.find("td", {'data-stat': 'mp_per_g'}).text,
            'field_goals_per_game': row.find("td", {'data-stat': 'fg_per_g'}).text,
            'field_goal_attempts_per_game': row.find("td", {'data-stat': 'fga_per_g'}).text,
            'field_goal_percentage': row.find("td", {'data-stat': 'fg_pct'}).text,
            'three_point_field_goals_per_game': row.find("td", {'data-stat': 'fg3_per_g'}).text,
            'three_point_field_goal_attempts_per_game': row.find("td", {'data-stat': 'fg3a_per_g'}).text,
            'three_point_percentage': row.find("td", {'data-stat': 'fg3_pct'}).text,
            'two_point_field_goals_per_game': row.find("td", {'data-stat': 'fg2_per_g'}).text,
            'two_point_field_goal_attempts_per_game': row.find("td", {'data-stat': 'fg2a_per_g'}).text,
            'two_point_field_goal_percentage': row.find("td", {'data-stat': 'fg2_pct'}).text,
            'free_throws_per_game': row.find("td", {'data-stat': 'ft_per_g'}).text,
            'free_throw_attempts_per_game': row.find("td", {'data-stat': 'fta_per_g'}).text,
            'free_throw_percentage': row.find("td", {'data-stat': 'ft_pct'}).text,
            'offensive_rebounds_per_game': row.find("td", {'data-stat': 'orb_per_g'}).text,
            'defensive_rebounds_per_game': row.find("td", {'data-stat': 'drb_per_g'}).text,
            'total_rebounds_per_game': row.find("td", {'data-stat': 'trb_per_g'}).text,
            'assists_per_game': row.find("td", {'data-stat': 'ast_per_g'}).text,
            'steals_per_game': row.find("td", {'data-stat': 'stl_per_g'}).text,
            'blocks_per_game': row.find("td", {'data-stat': 'blk_per_g'}).text,
            'turnovers_per_game': row.find("td", {'data-stat': 'tov_per_g'}).text,
            'points_per_game': row.find("td", {'data-stat': 'pts_per_g'}).text,
        }
    }


    for key, value in all_info.items():
        salary = players_with_salaries.get(value['stats']['name'])
        salary_str = players_with_salaries.get(value['stats']['name'])
        salary = float(salary_str.replace('$', '').replace(',', '')) if salary_str else None

        existing_player = PlayerStats.query.filter_by(players_name=value['stats']['name']).first()
    
        if existing_player is None:
            players_stats = PlayerStats (
    
            players_name = value['stats'].get('name') or 0,
            position = value['stats'].get('position') or 0,
            age = value['stats'].get('age') or 0,
            team = value['stats'].get('team') or 0,
            games_played = value['stats'].get('games_played') or 0,
            games_started = value['stats'].get('games_started') or 0,
            minutes_per_game = value['stats'].get('minutes_per_game') or 0,
            field_goals_per_game = value['stats'].get('field_goals_per_game') or 0,
            field_goal_attempts_per_game = value['stats'].get('field_goal_attempts_per_game') or 0,
            field_goal_percentage = value['stats'].get('field_goal_percentage') or 0,
            three_point_field_goals_per_game = value['stats'].get('three_point_field_goals_per_game') or 0,
            three_point_field_goal_attempts_per_game = value['stats'].get('three_point_field_goal_attempts_per_game') or 0,
            three_point_percentage = value['stats'].get('three_point_percentage') or 0,
            two_point_field_goals_per_game = value['stats'].get('two_point_field_goals_per_game') or 0,
            two_point_field_goal_attempts_per_game = value['stats'].get('two_point_field_goal_attempts_per_game') or 0,
            two_point_field_goal_percentage = value['stats'].get('two_point_field_goal_percentage') or 0,
            free_throws_per_game = value['stats'].get('free_throws_per_game') or 0,
            free_throw_attempts_per_game = value['stats'].get('free_throw_attempts_per_game') or 0,
            free_throw_percentage = value['stats'].get('free_throw_percentage') or 0,
            offensive_rebounds_per_game = value['stats'].get('offensive_rebounds_per_game') or 0,
            defensive_rebounds_per_game = value['stats'].get('defensive_rebounds_per_game') or 0,
            total_rebounds_per_game = value['stats'].get('total_rebounds_per_game') or 0,
            assists_per_game = value['stats'].get('assists_per_game') or 0,
            steals_per_game = value['stats'].get('steals_per_game') or 0,
            blocks_per_game = value['stats'].get('blocks_per_game') or 0,
            turnovers_per_game = value['stats'].get('turnovers_per_game') or 0,
            points_per_game = value['stats'].get('points_per_game') or 0,
        )
        
            db.session.add(players_stats)
            db.session.commit()
           


player_stats_list = all_info.items()
positions = ["PG", "SG", "SF", "PF", "C"]
all_position_averages = []

for position in positions:
    avg_games_played = []
    avg_points_per_game = [] 
    avg_games_started_per_game = []
    avg_minutes_per_game = []
    avg_field_goals_per_game = [] 
    avg_field_goal_attempts_per_game = [] 
    avg_field_goal_percentage = []
    avg_three_point_field_goals_per_game = [] 
    avg_three_point_field_goal_attempts_per_game = [] 
    avg_three_point_percentage = []
    avg_two_point_field_goals_per_game = []
    avg_two_point_field_goal_attempts_per_game = []
    avg_two_point_field_goal_percentage = []
    avg_free_throw_attempts_per_game = []
    avg_free_throws_per_game = []
    avg_free_throw_percentage_per_game = []
    avg_offensive_rebounds_per_game = []
    avg_defensive_rebounds_per_game = []
    avg_total_rebounds_per_game = []
    avg_assists_per_game = []
    avg_steals_per_game = []
    avg_avg_blocks_per_game = []
    avg_turnovers_per_game = []
    avg_points_per_game = []
    avg_salary = []

    for key, value in all_info.items():
        salary = players_with_salaries.get(value['stats']['name'])
        salary_str = players_with_salaries.get(value['stats']['name'])
        salary = float(salary_str.replace('$', '').replace(',', '')) if salary_str else None

        if value['stats'].get('position') == position:

            avg_salary.append(salary)
            avg_games_played.append(round(float(value['stats'].get('games_played', 0))))
            avg_points_per_game.append(round(float(value['stats'].get('points_per_game', 0))))
            avg_games_started_per_game.append(round(float(value['stats'].get('games_started', 0))))
            avg_minutes_per_game.append(round(float(value['stats'].get('minutes_per_game', 0))))
            avg_field_goals_per_game.append(round(float(value['stats'].get('field_goals_per_game', 0))))
            avg_field_goal_attempts_per_game.append(round(float(value['stats'].get('field_goal_attempts_per_game', 0))))
            avg_field_goal_percentage.append(round(float(value['stats'].get('field_goal_percentage', 0))))
            avg_three_point_field_goals_per_game.append(round(float(value['stats'].get('three_point_field_goals_per_game', 0))))
            avg_three_point_field_goal_attempts_per_game.append(round(float(value['stats'].get('three_point_field_goal_attempts_per_game', 0))))
            three_point_percentage_value = value['stats'].get('three_point_percentage', '')
            if three_point_percentage_value != '':
                avg_three_point_percentage.append(round(float(three_point_percentage_value)))
            else:
                avg_three_point_percentage.append(0)
            avg_two_point_field_goals_per_game.append(round(float(value['stats'].get('two_point_field_goals_per_game', 0))))
            avg_two_point_field_goal_attempts_per_game.append(round(float(value['stats'].get('two_point_field_goal_attempts_per_game', 0))))
            two_point_percentage_value = value['stats'].get('two_point_field_goal_percentage', '')
            if two_point_percentage_value != '':
                avg_two_point_field_goal_percentage.append(round(float(two_point_percentage_value)))
            else:
                avg_two_point_field_goal_percentage.append(0)
            avg_free_throw_attempts_per_game.append(round(float(value['stats'].get('free_throw_attempts_per_game', 0))))
            avg_free_throws_per_game.append(round(float(value['stats'].get('free_throws_per_game', 0))))
            avg_offensive_rebounds_per_game.append(round(float(value['stats'].get('offensive_rebounds_per_game', 0))))
            avg_defensive_rebounds_per_game.append(round(float(value['stats'].get('defensive_rebounds_per_game', 0))))
            avg_total_rebounds_per_game.append(round(float(value['stats'].get('total_rebounds_per_game', 0))))
            avg_assists_per_game.append(round(float(value['stats'].get('assists_per_game', 0))))
            avg_steals_per_game.append(round(float(value['stats'].get('steals_per_game', 0))))
            avg_avg_blocks_per_game.append(round(float(value['stats'].get('blocks_per_game', 0))))
            avg_turnovers_per_game.append(round(float(value['stats'].get('turnovers_per_game', 0))))

    avg_salary_value = sum(avg_salary) / len(avg_salary) if avg_salary else 0   
    avg_games_played_value = sum(avg_games_played) / len(avg_games_played) if avg_games_played else 0
    avg_games_started_per_game_value = sum(avg_games_started_per_game) / len(avg_games_started_per_game) if avg_games_started_per_game else 0
    avg_minutes_per_game_value = sum(avg_minutes_per_game) / len(avg_minutes_per_game) if avg_minutes_per_game else 0
    avg_points_per_game_value = sum(avg_points_per_game) / len(avg_points_per_game) if avg_points_per_game else 0
    avg_field_goals_per_game_value = sum(avg_field_goals_per_game) / len(avg_field_goals_per_game) if avg_field_goals_per_game else 0
    avg_field_goal_attempts_per_game_value = sum(avg_field_goal_attempts_per_game) / len(avg_field_goal_attempts_per_game) if avg_field_goal_attempts_per_game else 0       
    avg_field_goal_percentage_value = sum(avg_field_goal_percentage) / len(avg_field_goal_percentage) if avg_field_goal_percentage else 0
    avg_three_point_field_goals_per_game_value = sum(avg_three_point_field_goals_per_game) / len(avg_three_point_field_goals_per_game) if avg_three_point_field_goals_per_game else 0
    avg_three_point_field_goal_attempts_per_game_value = sum(avg_three_point_field_goal_attempts_per_game) / len(avg_three_point_field_goal_attempts_per_game) if avg_three_point_field_goal_attempts_per_game else 0          
    avg_three_point_percentage_value = sum(avg_three_point_percentage) / len(avg_three_point_percentage) if avg_three_point_percentage else 0
    avg_two_point_field_goals_per_game_value = sum(avg_two_point_field_goals_per_game) / len(avg_two_point_field_goals_per_game) if avg_two_point_field_goals_per_game else 0              
    avg_two_point_field_goal_attempts_per_game_value = sum(avg_two_point_field_goal_attempts_per_game) / len(avg_two_point_field_goal_attempts_per_game) if avg_two_point_field_goal_attempts_per_game else 0
    avg_two_point_field_goal_percentage_value = sum(avg_two_point_field_goal_percentage) / len(avg_two_point_field_goal_percentage) if avg_two_point_field_goal_percentage else 0
    avg_free_throw_attempts_per_game_value = sum(avg_free_throw_attempts_per_game) / len(avg_free_throw_attempts_per_game) if avg_free_throw_attempts_per_game else 0                  
    avg_free_throws_per_game_value = sum(avg_free_throws_per_game) / len(avg_free_throws_per_game) if avg_free_throws_per_game else 0
    avg_offensive_rebounds_per_game_value = sum(avg_offensive_rebounds_per_game) / len(avg_offensive_rebounds_per_game) if avg_offensive_rebounds_per_game else 0
    avg_defensive_rebounds_per_game_value = sum(avg_defensive_rebounds_per_game) / len(avg_defensive_rebounds_per_game) if avg_defensive_rebounds_per_game else 0              
    avg_total_rebounds_per_game_value = sum(avg_total_rebounds_per_game) / len(avg_total_rebounds_per_game) if avg_total_rebounds_per_game else 0
    avg_assists_per_game_value = sum(avg_assists_per_game) / len(avg_assists_per_game) if avg_assists_per_game else 0
    avg_steals_per_game_value = sum(avg_steals_per_game) / len(avg_steals_per_game) if avg_steals_per_game else 0
    avg_avg_blocks_per_game_value = sum(avg_avg_blocks_per_game) / len(avg_avg_blocks_per_game) if avg_avg_blocks_per_game else 0
    avg_turnovers_per_game_value = sum(avg_turnovers_per_game) / len(avg_turnovers_per_game) if avg_turnovers_per_game else 0
    avg_points_per_game_value = sum(avg_points_per_game) / len(avg_points_per_game) if avg_points_per_game else 0

    position_averages = AvgStats (

        avg_salary=avg_salary_value,
        position=position,
        avg_games_played=avg_games_played_value,
        avg_games_started_per_game=avg_games_started_per_game_value,
        avg_points_per_game=avg_points_per_game_value,
        avg_minutes_per_game=avg_minutes_per_game_value,
        avg_field_goals_per_game=avg_field_goals_per_game_value,
        avg_field_goal_attempts_per_game=avg_field_goal_attempts_per_game_value,
        avg_field_goal_percentage=avg_field_goal_percentage_value,
        avg_three_point_field_goals_per_game=avg_three_point_field_goals_per_game_value,
        avg_three_point_percentage=avg_three_point_percentage_value,
        avg_two_point_field_goals_per_game=avg_two_point_field_goals_per_game_value,
        avg_two_point_field_goal_attempts_per_game=avg_two_point_field_goal_attempts_per_game_value,
        avg_two_point_field_goal_percentage=avg_two_point_field_goal_percentage_value,
        avg_free_throw_attempts_per_game=avg_free_throw_attempts_per_game_value,
        avg_free_throws_per_game=avg_free_throws_per_game_value,
        avg_offensive_rebounds_per_game=avg_offensive_rebounds_per_game_value,
        avg_defensive_rebounds_per_game=avg_defensive_rebounds_per_game_value,
        avg_total_rebounds_per_game=avg_total_rebounds_per_game_value,
        avg_assists_per_game=avg_assists_per_game_value,
        avg_steals_per_game=avg_steals_per_game_value,
        avg_blocks_per_game=avg_avg_blocks_per_game_value,
        avg_turnovers_per_game=avg_turnovers_per_game_value,
    )
    all_position_averages.append(position_averages)
    
db.session.add_all(all_position_averages)
db.session.commit()


# curl -v -X POST "http://localhost:3001/auth/register" -d '{"username": "kklovessummer", "password": "myPassword", "email": "kkmail@mail.com", "firstName": "kalani", "lastName": "kill"}' -H 'content-type: application/json'








      
            
        

        


       



  
  





