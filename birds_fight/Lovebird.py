from Enemy import *
import random


class Lovebird(Enemy):
    def __init__(self, health_points, attack_damage) -> None:
        super().__init__(type_of_enemy='Lovebird',
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self) -> None:
        print('Pio Pio (angry noise..)')

    def preen(self) -> None:
        print(f'{self.get_type_of_enemy()} is trying to preen some feathers!')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            self.health_points += 2
            print(f'{self.get_type_of_enemy()} regenerated 2HP!')
