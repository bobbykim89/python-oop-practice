from Enemy import *
from Lovebird import *
from Cockatiel import *
from Hero import *
from Weapon import *


def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print('---------------')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()}: {e1.health_points} HP left')
        print(f'{e2.get_type_of_enemy()}: {e2.health_points} HP left')
        e2.attack()
        e1.health_points -= e2.attack_damage
        e2.health_points -= e1.attack_damage
    print('---------------')
    if e1.health_points > 0:
        print(f'{e1.get_type_of_enemy()} wins!')
    else:
        print(f'{e2.get_type_of_enemy()} wins!')


def hero_battle(hero: Hero, enemy: Enemy):

    while hero.health_points > 0 and enemy.health_points > 0:
        print('---------------')
        enemy.special_attack()
        print(f'Hero: {hero.health_points} HP left')
        print(f'{enemy.get_type_of_enemy()}: {enemy.health_points} HP left')
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        enemy.health_points -= hero.attack_damage
    print('---------------')
    if hero.health_points > 0:
        print('Hero wins!')
    else:
        print(f'{enemy.get_type_of_enemy()} wins!')


lovebird = Lovebird(20, 10)
cockatiel = Cockatiel(30, 5)
hero = Hero(20, 5)
weapon = Weapon('Millet', 10)
hero.weapon = weapon
hero.equip_weapon()

# battle(lovebird, cockatiel)
hero_battle(hero, lovebird)
