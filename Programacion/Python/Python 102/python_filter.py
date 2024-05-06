num = [1,2,3,4,5,6,7,8,9,10]
fil = list(filter(lambda x: x % 2 == 0, num))
#aplica filtros basado en una condicion, en este caso si es par
print(fil)

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

lista_ganadores = list(filter(lambda x: x['home_team_result'] == 'Win',matches))
ganadores = list(map(lambda x: x['home_team'], lista_ganadores))
# se hace un filtro de los diccionarios que ganaron, 
# y se extraen el equipo en una lista del diccionario
print(ganadores)