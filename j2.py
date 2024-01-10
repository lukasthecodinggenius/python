number_players = int(input())
players = []

starplayers = 0
starteam = 0
startteamstring = ''
total = 0
for i in range(number_players):
    goals = int(input())
    fouls = int(input())
    players.append(goals)


for i in players:

    if ((goals * 5) - (fouls * 3)) > 40:
        starplayers += 1

    if starplayers == number_players:
        starteam += 1

if starteam <= 1:
    starteamstring = '+'
else:
    starteamstring = ''

print(str(starplayers) + str(starteamstring))



