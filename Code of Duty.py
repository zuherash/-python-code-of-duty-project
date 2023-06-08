import random
import sys

class Player:
    def __init__(self, name, health, attack, defense, weapon_type):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.weapon_type = weapon_type

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0


class Weapon:
    def __init__(self, name, damage, weapon_type):
        self.name = name
        self.damage = damage
        self.weapon_type = weapon_type


class Game:
    def set_players(self, player1, player2):
        if len(player1) > 10 or len(player2) > 10:
            print("Player name must be 10 characters or less.")
            sys.exit()
        self.player1 = Player(player1, 100, 30, 10, 'melee')
        self.player2 = Player(player2, 100, 25, 15, 'ranged')
        self.distance = 0

    def calculate_distance(self):
        self.distance = random.randint(1, 10)

    def play(self):
        while self.player1.is_alive() and self.player2.is_alive():
            print("Player 1:", self.player1.name)
            print("Health:", self.player1.health)
            print("Player 2:", self.player2.name)
            print("Health:", self.player2.health)
            print("Distance:", self.distance)
            print("-----------------------------")

            self.calculate_distance()

            if self.distance > 5:
                attacker = self.player1
                defender = self.player2
            else:
                attacker = self.player2
                defender = self.player1

            print(attacker.name, "is attacking", defender.name, "should", attacker.name, "attack or", defender.name, "should defend")
            try:
                action = int(input("Choose your action: (1) Attack {0}, (2) Defend {1} ".format(defender.name, attacker.name)))

                if action == 1:
                    weapon_type = int(input("Choose your weapon type: (1) Melee, (2) Ranged: "))

                    if weapon_type == 1:
                        print("Available melee weapons:")
                        for index, weapon in enumerate(melee_weapons):
                            print(f"{index + 1}. {weapon.name} (Damage: {weapon.damage})")
                        weapon_index = int(input("Choose a melee weapon by index: ")) - 1

                        if 0 <= weapon_index < len(melee_weapons):
                            weapon = melee_weapons[weapon_index]
                            print("You chose", weapon.name)
                        else:
                            print("Invalid weapon index. Skipping turn.")
                            print("-----------------------------")
                            continue

                    elif weapon_type == 2:
                        print("Available ranged weapons:")
                        for index, weapon in enumerate(ranged_weapons):
                            print(f"{index + 1}. {weapon.name} (Damage: {weapon.damage})")
                        weapon_index = int(input("Choose a ranged weapon by index: ")) - 1

                        if 0 <= weapon_index < len(ranged_weapons):
                            weapon = ranged_weapons[weapon_index]
                            print("You chose", weapon.name)
                        else:
                            print("Invalid weapon index. Skipping turn.")
                            print("-----------------------------")
                            sys.exit()

                    else:
                        print("Invalid weapon type. Skipping turn.")
                        print("-----------------------------")
                        sys.exit()

                    damage = weapon.damage
                    print(attacker.name, "used", weapon.name, "and dealt", damage, "damage.")

                elif action == 2:
                    damage = max(0, attacker.attack - defender.defense)
                    print(defender.name, "chose to defend and reduced the damage by", damage, "points.")

                else:
                    print("Invalid action. Skipping turn.")
                    print("-----------------------------")
                    sys.exit()

            except ValueError:
                print("Invalid input. Skipping turn.")
                print("-----------------------------")
                continue

            defender.take_damage(damage)

            if not defender.is_alive():
                print(defender.name, "has been defeated!")
                break

            print("-----------------------------")

        print("Game Over!")
        sys.exit()


melee_weapons = [
    Weapon("Sword", 20, 'melee'),
    Weapon("Axe", 25, 'melee')
]

ranged_weapons = [
    Weapon("AK-47", 20, 'ranged'),
    Weapon("Crossbow", 18, 'ranged'),
    Weapon("Throwing knives", 10, 'ranged')
]

try:
    player1_name = input("Enter Player 1's Name: ")
    player2_name = input("Enter Player 2's Name: ")
except:
    sys.exit()

game = Game()
game.set_players(player1_name, player2_name)
game.play()
