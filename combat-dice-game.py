import null
import random


class combatant:
    def __init__(self, name, combat_class, attack: float, defense: float, strength: float, luck: float):
        self.name = name
        self.combat_class = combat_class
        self.attack = attack
        self.defense = defense
        self.strength = strength
        self.luck = luck

    def strike_damage_calc(self):
        # combatant gets self.luck rolls to improve their damage
        strike_damage_best = self.attack * self.strength * random.random()
        while self.luck > 0:
            strike_damage_temp = self.attack * self.strength * random.random()
            if strike_damage_temp > strike_damage_best:
                strike_damage_best = strike_damage_temp
            self.luck -= 1
        return strike_damage_best


class fight:
    def __init__(self, challenger_one: combatant, challenger_two: combatant):
        self.challenger_one = challenger_one
        self.challenger_two = challenger_two

    def announcement(self, challenger_one, challenger_two):
        print("Fight initiated between " + challenger_one.name + " with " + str(
            challenger_one.defense) + " defense " + " and " + challenger_two.name + " with " + str(
            challenger_two.defense) + " defense!")

    def calc_result(self, attacker, defender):
        attacker = attacker
        defender = defender
        damage = attacker.strike_damage_calc()
        defender.defense = defender.defense - damage
        # print(attacker.name + " the " + attacker.combat_class + " attacks " + defender.name + " for " + str(damage) + " damage!")
        # print(defender.name + " has " + str(defender.defense) + " defense remaining!")

    def combat_loop(self, challenger_one, challenger_two):
        round_number = 1
        while challenger_one.defense > 0 and challenger_two.defense > 0:
            fight.round_of_combat(null, challenger_one, challenger_two, round_number)
            round_number += 1

    def declare_winner(self, challenger_one, challenger_two):
        if challenger_one.defense > challenger_two.defense:
            print("The winner is " + challenger_one.name + "!")
        else:
            print("The winner is " + challenger_two.name + "!")

    def round_of_combat(self, challenger_one, challenger_two, round_number):
        # Alternating attacks, note that while challenger_one always attacks first, even if challenger_two is defense<0 they get to attack as well
        fight.calc_result(null, challenger_one, challenger_two)
        fight.calc_result(null, challenger_two, challenger_one)
        # print("Round " + str(round_number) + " of combat complete!\n")


test_number = 15
while test_number > 0:
    enemy = combatant("Name_one", "Moonmaster", 2, 100, 4, 9)
    ally = combatant("Name_two", "Suncaster", 2, 100, 4, 1)
    fight.announcement(null, enemy, ally)
    fight.combat_loop(null, enemy, ally)
    fight.declare_winner(null, enemy, ally)
    test_number -= 1
# end
