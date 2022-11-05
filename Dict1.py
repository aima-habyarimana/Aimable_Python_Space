teams = {"name": "Chelsea", "color": "blue", 'budget': 50}  # key in '' or "" and value in '' or "" if is of
# text string.
print(teams['name'])
print(teams['color'])
print(teams['budget'])
print(teams)

teams['budget']=75
print(teams)

new_team = teams
print(new_team)

alien_0 = {} # creating an empty dictionary
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# remove the key 'points' from the alien_0 dictionary along with its value:
del alien_0['points']
print(alien_0)

#A dictionary can be of similar objects
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print(favorite_languages)

for key, value in favorite_languages.items():  #Loop through the dictionary key-value pair
 print(f"\n {key.title()} :-> {value}")  #.title() method puts the first letter in capital.


#looping through keys particulary.
friends = ['Robert','Phil']
for key in favorite_languages.keys():
 if key.title() in friends:
  print(f"I have just spotted you {key.title()}")


for name in sorted(favorite_languages.keys()): #Looping Through a Dictionary’s Keys in Order
 print(name.title())

for key, value in favorite_languages.items():
 print(key.title() + " " + value.title())

for key, value in sorted(favorite_languages.items()):  #Looping Through a Dictionary’s Keys, value in Order
 print(key.title() + " " + value.title())

for language in favorite_languages.values(): #Looping Through All Values in a Dictionary
 print(language.title())

#NESTED Dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
 print(alien)

 # A List in a Dictionary
 pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese']
 }

print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
 print("\t" + topping)


print(pizza['toppings'])
print(pizza)

#######################################
favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
for name, languages in favorite_languages.items():
 print("\n" + name.title() + "'s favorite languages are:")

for language in languages:
 print("\t" + language.title())


 # You can nest a dictionary inside another dictionary
 users = {
  'aeinstein': {
   'first': 'albert',
   'last': 'einstein',
   'location': 'princeton',
  },

  'mcurie': {
   'first': 'marie',
   'last': 'curie',
   'location': 'paris',
  },
 }
 for username, user_info in users.items():
  print("\nUsername: " + username)
  full_name = user_info['first'] + " " + user_info['last']
  location = user_info['location']

  print("\tFull name: " + full_name.title())
  print("\tLocation: " + location.title())

