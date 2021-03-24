import random

weaponone = ['XM4', 'Krig 6', 'AK-47', 'QBZ-83', 'FFAR 1', 'MP5', 'Milano 821', 'AK-74u', 'KSP 45',
             'Bullfrog', 'M16', 'Type 63', 'AUG', 'DMR 14', 'RPD', 'Stoner 63', 'M60', 'LW3 – Tundra', 'Pellington 703']
weapontwo = ['XM4', 'Krig 6', 'AK-47', 'QBZ-83', 'FFAR 1', 'MP5', 'Milano 821', 'AK-74u', 'KSP 45',
             'Bullfrog', 'M16', 'Type 63', 'AUG', 'DMR 14', 'RPD', 'Stoner 63', 'M60', 'LW3 – Tundra', 'Pellington 703']
killstreak = ['RCXD', 'Spyplane', 'Counter Spyplane', 'Sentry Turret',
              'Napalm Strike', 'Artillery', 'Air Patrol', 'War Machine', 'Attack Helicopter', 'Chopper Gunner', 'Death Machine']
perkOne = ['Engineer ', 'Tactical Mask ',
           'Flak Jacket ', 'Paranoia ', 'Forward Intel']
perkTwo = ['Scavenger ', 'Quartermaster ', 'Tracker', 'Assassin', 'Gear Head']
perkThree = ['Cold Blooded ', 'Ghost ', 'Ninja ', 'Gung-Ho ', 'Spy-craft']
lethalEquipment = ['Frag', 'Semtex', 'C4', 'Tomahawk', 'Molotov']
tacticalEquipment = ['Smoke Grenade',
                     'Stun Grenade', 'Stimshot', 'Flashbang', 'Decoy']

primaryWeapon = random.choice(weaponone)
secondaryWeapon = random.choice(weapontwo)
killstreak1 = random.choice(killstreak1)
killstreak2 = random.choice(killstreak2)
killstreak3 = random.choice(killstreak3)
perkOne = random.choice(perkOne)
perkTwo = random.choice(perkTwo)
perkThree = random.choice(perkThree)
lethalEquipment = random.choice(lethalEquipment)
tacticalEquipment = random.choice(tacticalEquipment)

print("Welcome to Jake's Class Gen!")
print
print

print('Primary Weapon: ' + weaponone)
print('Secondary Weapon: ' + weapontwo)
print('Killstreak 1: ' + killstreak)
print('Killstreak 2: ' + killstreak)
print('Killstreak 3: ' + killstreak)
print('Perk 1: ' + perkOne)
print('Perk 2: ' + perkTwo)
print('Perk 3: ' + perkThree)
print('Lethal: ' + lethalEquipment)
print('Tactical: ' + tacticalEquipment)
