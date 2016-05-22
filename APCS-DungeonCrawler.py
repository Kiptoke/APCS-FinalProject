# Andrew Zhou
# Dungeon Crawler - Final Project

import random
import sys

print("\t------ NEVERENDING DUNGEON CRAWLER ------\n")

class Entity():                                 # TODO: better get some documentation
    
    def __init__(self, hp, attack, defense):
        self.health = hp
        self.atk = attack
        self.defn = defense
        
    def setHealth(self, hp):
        self.health = hp
    def setAttack(self, attack):
        self.atk = attack
    def setDefense(self, defense):
        self.defn = defense
        
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.atk
    def getDefense(self):
        return self.defn
    
class Player(Entity):
    'The player - bravely fighting their way through the dungeon'

    def upgrade(self):
        print("You enter a shop and inspect the wares:\n")
        print("1. Health Upgrade (from " + str(self.getHealth()) + " to " + str(self.getHealth() + 5) + ")")
        print("2. Sword Upgrade (from " + str(self.getAttack()) + " to " + str(self.getAttack() + 0.1) + ")")
        print("3. Shield Upgrade (from " + str(self.getDefense()) + " to " + str(self.getDefense() + 0.1) + ")")

    def isPlayer(self):
        return True

class Enemy(Entity):
    'The enemy - objective: to kill you'

    def isPlayer(self):
        return False
    
class Dungeon():
    'Welcome. You are forever trapped. Welcome to the Dungeon.'
    playerRound = 0
    
    def __init__(self):
        self.level = 1
        Dungeon.playerRound += 1
        
    def fight_flight(self):                             
        print("You encounter a monster!")
        print("Will you fight it, or will you run away? (write 'f' or 'r')\n")
        fight = input("CHOICE: ")

        if fight == "f":
            print("fight")
            # TODO: find way to put in fight method
        elif fight == "r":
            print("You run!")
            run()
            
    def run(self):
        change = random.randint(1, 10)
        if change >= 7:
            print("You run away!")
            self.level += 1
            fight_flight()
        else:
            print("You trip and fall flat on your face.")
            # TODO: put in fight method
            
    def fight(self, attacker, target):                              # TODO: remove testing code eventually
        print("Health of attacker: " + str(attacker.getHealth()))   # TODO: review fight method
        print("Health of target: " + str(target.getHealth()))
        print("atk mod of attacker: " + str(attacker.getAttack()))
        print("def mod of target: " + str(target.getAttack()))
        rawAttack = random.randint(1, 10) * attacker.getAttack()
        print("raw attack: " + str(rawAttack))
        enemyDefense = random.randint(1, 5) * target.getDefense()
        print("enemy defense: " + str(enemyDefense))
        totalAttack = rawAttack - enemyDefense
        
        if totalAttack <= 0:
            totalAttack = 0

        print(str(totalAttack))
        
        target.setHealth(target.getHealth() - totalAttack)

        print("Health of target: " + str(target.getHealth()))

        self.checkDeath(target)

    def checkDeath(self, entity):
        health = entity.getHealth()
        if (health <= 0) and (entity.isPlayer() == True):
            print("You perish in the dungeons.")
            sys.exit()
        elif (health <= 0) and (entity.isPlayer() == False):
            print("You have vanquished the enemy!")
            
# TODO: remove this test code

testD = Dungeon()


# TODO: write main code
