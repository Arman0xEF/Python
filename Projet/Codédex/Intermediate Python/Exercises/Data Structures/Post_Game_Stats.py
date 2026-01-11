Chiefs = [
{'name' : 'Matt Araiza','position' : 'P','jersey number' : 14,"yards_gained": 320, "touchdowns": 4},
{'name' : 'Jeffrey Bassa','position' : 'LB','jersey number' : 31,"yards_gained": 120, "touchdowns": 3},
{'name' : 'Nick Bolton','position' : 'LB','jersey number' : 32,"yards_gained": 250, "touchdowns": 1}
]

names = [i['name'] for i in Chiefs]
print("This is the name of the players : ",names)

positions = [i['position'] for i in Chiefs]
print("These are the position of the players : ",positions)

Chiefs[0]['yards_gained'] = 300
Chiefs[0]['touchdowns'] = 5

average_yards = sum(i['yards_gained'] for i in Chiefs) / len(Chiefs)
average_touchdowns = sum(i['touchdowns'] for i in Chiefs) / len(Chiefs)

print("The average of yards gained is :",average_yards)
print("The average of touchdowns is :",average_touchdowns)
