bicycles = ['trek','cannondale','redline','specialezed']
print(bicycles)
print(bicycles[0].title())
print(bicycles[3])

print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])


#3-2
friends = ['giacomo','rachele']

print (f'Hello, {friends[0].title()}')
print (f'Hello, {friends[1].title()}')

cars = ['honda','ferrari','mustang']

print (f'I woud like to have a {cars[-1].title()}')
print (f'I woud like to drive a {cars[1].title()}')
print (f'I wouldnt like to have a {cars[0].title()}')

motorcycles = ['honda',"yamaha",'suzuki']
motorcycles[0] = 'gremio'
print (motorcycles)

motorcycles = ['honda']

football_teams = []
football_teams.append('gremio')
football_teams.append('gremio1')
football_teams.append('gremio2')
football_teams.append('gremio3')
print(football_teams)

football_teams.insert(0,'gremio is the only team worth mentioning')
print(football_teams)

del football_teams[0]
print(football_teams)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#pop()
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")