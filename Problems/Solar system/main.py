# create the planets.txt
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
f = open('planets.txt', 'w', encoding='utf-8')
for planet in planets:
    f.write(planet + '\n')

f.close()
