players=[22, 24 , 28 , 22, 41, 89]
print(players[2])
players[3] = 99 
print(players)
players = players + [65, 87, 90]
print(players)
players.append(101)
print(players)
print(players[:4]) #show only list starting from 0 to 3
players[:] = [] # this will overwrite the items in the list
print(players)