import random


class bcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'


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

print(bcolors.RED + "Welcome to Jake's Class Gen!" + bcolors.RESET)
print
print

print(bcolors.GREEN + 'PRIMARY WEAPON: ' + bcolors.RESET)
print(primaryWeapon)
print
print(bcolors.GREEN + 'SECONDARY WEAPON: ' + bcolors.RESET)
print(secondaryWeapon)
print
print(bcolors.GREEN + 'KILLSTREAK 1: ' + bcolors.RESET)
print(killstreak1)
print
print(bcolors.GREEN + 'KILLSTREAK 2: ' + bcolors.RESET)
print(killstreak2)
print
print(bcolors.GREEN + 'KILLSTREAK 3: ' + bcolors.RESET)
print(killstreak3)
print
print(bcolors.GREEN + 'PERK 1: ' + bcolors.RESET)
print(perkOne)
print
print(bcolors.GREEN + 'PERK 2: ' + bcolors.RESET)
print(perkTwo)
print
print(bcolors.GREEN + 'PERK 3: ' + bcolors.RESET)
print(perkThree)
print
print(bcolors.GREEN + 'WILDCARD: ' + bcolors.RESET)
print(wildcard)
print

if wildcard == 'Law Breaker':
    print(bcolors.RED + "Congrats! Law Breaker has been chosen for you!\n Feel free to do whatever you would like." + bcolors.RESET)

    print

if wildcard == 'Perk Greed':
    print(bcolors.RED + "Here are your extra perks! " + bcolors.RESET)
    print(perkOne)
    print(perkTwo)
    print(perkThree)

    print

if wildcard == 'Gunfighter':
    print(bcolors.RED + "Enjoy the extra attachment slots!" + bcolors.RESET)

if wildcard == 'Danger Close':
    print(bcolors.RED + "Enjoy the extra piece of lethal and tactical equipment,\n as well as extra ammunition!" + bcolors.RESET)

    print

print(bcolors.GREEN + 'Lethal: ' + bcolors.RESET)
print(lethalEquipment)
print
print(bcolors.GREEN + 'Tactical: ' + bcolors.RESET)
print(tacticalEquipment)
print
