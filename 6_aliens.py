#字典列表
#alien_0 = {'color': 'green', 'points': 5}
#alien_1 = {'color': 'yellow', 'points': 10}
#alien_2 = {'color': 'red', 'points': 15}

#aliens = [alien_0, alien_1, alien_2]
#for alien in aliens:
#    print(alien)

#aliens = []

#for alien_number in range(30):
#    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#    aliens.append(new_alien)

#for alien in aliens[0:3]:
#    if alien['color'] == 'green':
#        alien['color'] = 'yellow'
#        alien['speed'] = 'medium'
#        alien['points'] = 10
#    elif alien['color'] == 'yellow':
#        alien['color'] = 'red'
#        alien['speed'] = 'fast'
#        alien['points'] = 15

#for alien in aliens[:5]:
#    print(alien)
#print("...")
#print("Total number of aliens: " + str(len(aliens)))

#列表字典
#favorite_languages = {
#    'jen': ['python', 'ruby'],
#    'sarah': ['c'],
#    'edward': ['ruby', 'go'],
#    'phil': ['python', 'haskell'],
#    }
#for name, languages in favorite_languages.items():
    
#    if len(languages) > 1:
#        for language in languages:
#            print(name.title() + "'s favorite languages are:""\t" + language.title())
#    else:
#        for language in languages:
#            print(name.title() + "'s favorite languages are:""\t" + language.title())

#字典字典
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