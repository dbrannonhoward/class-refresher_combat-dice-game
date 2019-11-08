import null
import random


class Combatant:
    def __init__(self, name, combat_class, attack:float, defense:float, strength:float, luck:float):
        self.name = name
        self.combat_class = combat_class
        self.attack = attack
        self.defense = defense
        self.strength = strength
        self.luck = luck

    @staticmethod
    def get_combatant_name(self):
        return self.name

    def set_name(self):
        self.name = input("Test")

    def set_combat_class(self, user_input_combat_class):
        self.combat_class = input(user_input_combat_class)

    def set_attack(self, user_input_attack):
        self.attack = input(user_input_attack)

    def set_defense(self, user_input_defense):
        self.defense = input(user_input_defense)

    def set_strength(self, user_input_strength):
        self.strength = input(user_input_strength)

    def set_luck(self, user_input_luck):
        self.luck = input(user_input_luck)

    def strike_damage_calc(self):
        # Combatant gets self.luck rolls to improve their damage
        strike_damage_best = self.attack * self.strength * random.random()
        while self.luck > 0:
            strike_damage_temp = self.attack * self.strength * random.random()
            if strike_damage_temp > strike_damage_best:
                strike_damage_best = strike_damage_temp
            self.luck -= 1
        return strike_damage_best


class Fight:
    def __init__(self, challenger_one: Combatant, challenger_two: Combatant):
        self.challenger_one = challenger_one
        self.challenger_two = challenger_two

    @staticmethod
    def announcement(self, challenger_one, challenger_two):
        print("Fight initiated between " + challenger_one.name + " with " + str(
            challenger_one.defense) + " defense " + " and " + challenger_two.name + " with " + str(
            challenger_two.defense) + " defense!")

    @staticmethod
    def calc_result(self, attacker, defender):
        attacker = attacker
        defender = defender
        damage = attacker.strike_damage_calc()
        defender.defense = defender.defense - damage
        # print(attacker.name + " the " + attacker.combat_class + " attacks " + defender.name + " for " + \
        # str(damage) + " damage!")
        # print(defender.name + " has " + str(defender.defense) + " defense remaining!")

    @staticmethod
    def combat_loop(self, challenger_one, challenger_two):
        round_number = 1
        while challenger_one.defense > 0 and challenger_two.defense > 0:
            Fight.round_of_combat(null, challenger_one, challenger_two, round_number)
            round_number += 1

    @staticmethod
    def declare_winner(self, challenger_one, challenger_two):
        if challenger_one.defense > challenger_two.defense:
            print("The winner is " + challenger_one.name + "!")
        else:
            print("The winner is " + challenger_two.name + "!")

    @staticmethod
    def round_of_combat(self, challenger_one, challenger_two, round_number):
        # Alternating attacks, note that while challenger_one always attacks first, even if challenger_two \
        # is defense<0 they get to attack as well
        Fight.calc_result(null, challenger_one, challenger_two)
        Fight.calc_result(null, challenger_two, challenger_one)
        # print("Round " + str(round_number) + " of combat complete!\n")


test_number = 15
while test_number > 0:
    enemy = Combatant("defaultname", "defaultclass", 1, 1, 1, 1)
    ally = Combatant("defaultname", "defaultclass", 1, 1, 1, 1)
    enemy.set_name
    Fight.announcement(null, enemy, ally)
    Fight.combat_loop(null, enemy, ally)
    Fight.declare_winner(null, enemy, ally)
    test_number -= 1
# end
