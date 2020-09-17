# read animals.txt
# and write animals_new.txt
animals = open('animals.txt', 'r')
new_animal = open('animals_new.txt', 'w')
new_animal.write(animals.read().replace('\n', ' '))
animals.close()
new_animal.close()
