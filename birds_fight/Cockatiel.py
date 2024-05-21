from Enemy import *
import random


class Cockatiel(Enemy):
    def __init__(self, health_points, attack_damage) -> None:
        super().__init__(type_of_enemy='Cockatiel',
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        print('Dubbi dub dubi dub dubi dub!')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.attack_damage += 2
            print(f'{self.get_type_of_enemy()} gets angry and increases attack by 2')
