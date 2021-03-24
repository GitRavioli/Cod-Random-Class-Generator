import random

weaponone = ['XM4', 'Krig 6', 'AK-47', 'QBZ-83', 'FFAR 1', 'MP5', 'Milano 821', 'AK-74u', 'KSP 45',
             'Bullfrog', 'M16', 'Type 63', 'AUG', 'DMR 14', 'RPD', 'Stoner 63', 'M60', 'LW3Tundra', 'Pellington 703']
weapontwo = ['1911', 'Diamatti', 'Magnum',
             'Hauer 77', 'Gallo SA12', 'Cigma 2', 'RPG 7']
killstreak = ['RCXD', 'Spyplane', 'Counter Spyplane', 'Sentry Turret',
              'Napalm Strike', 'Artillery', 'Air Patrol', 'War Machine', 'Attack Helicopter', 'Chopper Gunner', 'Death Machine']
perkOne = ['Engineer ', 'Tactical Mask ',
           'Flak Jacket ', 'Paranoia ', 'Forward Intel']
perkTwo = ['Scavenger ', 'Quartermaster ', 'Tracker', 'Assassin', 'Gear Head']
perkThree = ['Cold Blooded ', 'Ghost ', 'Ninja ', 'Gung-Ho ', 'Spycraft']
wildcards = ['Danger Close', 'Law Breaker', 'Gunfighter', 'Perk Greed']
lethalEquipment = ['Frag', 'Semtex', 'C4', 'Tomahawk', 'Molotov']
tacticalEquipment = ['Smoke Grenade',
                     'Stun Grenade', 'Stimshot', 'Flashbang', 'Decoy']

primaryWeapon = random.choice(weaponone)
secondaryWeapon = random.choice(weapontwo)
killstreak1 = random.choice(killstreak)
killstreak2 = random.choice(killstreak)
killstreak3 = random.choice(killstreak)
perkOne = random.choice(perkOne)
perkTwo = random.choice(perkTwo)
perkThree = random.choice(perkThree)
wildcard = random.choice(wildcards)
lethalEquipment = random.choice(lethalEquipment)
tacticalEquipment = random.choice(tacticalEquipment)

print("Welcome to Jake's Class Gen!")
print
print

print('PRIMARY WEAPON: ')
print(primaryWeapon)
print
print('SECONDARY WEAPON: ')
print(secondaryWeapon)
print
print('KILLSTREAK 1: ')
print(killstreak1)
print
print('KILLSTREAK 2: ')
print(killstreak2)
print
print('KILLSTREAK 3: ')
print(killstreak3)
print
print('PERK 1: ')
print(perkOne)
print
print('PERK 2: ')
print(perkTwo)
print
print('PERK 3: ')
print(perkThree)
print
print('WILDCARD: ')
print(wildcard)
print

if wildcard == 'Law Breaker':
    print("Congrats! Law Breaker has been chosen for you!\n Feel free to do whatever you would like.")
    print

if wildcard == 'Perk Greed':
    print("Here are your extra perks! ")
    print(perkOne)
    print(perkTwo)
    print(perkThree)

    print

if wildcard == 'Gunfighter':
    print("Enjoy the extra attachment slots!")

if wildcard == 'Danger Close':
    print("Enjoy the extra piece of lethal and tactical equipment,\n as well as extra ammunition!")


print('Lethal: ')
print(lethalEquipment)
print
print('Tactical: ')
print(tacticalEquipment)
