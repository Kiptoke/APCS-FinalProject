# Andrew Zhou
# Dungeon Crawler - Final Project

import random
import sys
import math

print("\t------ InfiniDungeon ------\n")

class Entity():                                 
        
    def __init__(self, hp=10, attack=1.0, defense=1.0):
        self.health = hp
        self.atk = attack
        self.defn = defense
        
    def setHealth(self, hp):
        if self.health <= 0:
            self.health = 0
        else:
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
        print("2. Sword Upgrade (from " + str(self.getAttack()) + " to " + str(self.getAttack() + 0.5) + ")")
        print("3. Shield Upgrade (from " + str(self.getDefense()) + " to " + str(self.getDefense() + 0.5) + ")")

        choice = input("1, 2 or, 3: ")

        return choice
        
    def isPlayer(self):
        return True

    def toString(self):
        print("Player statistics:\nHealth: " + str(self.getHealth()) + "\nAttack Modifier: " + str(self.getAttack()) + "\nDefense Modifier: " + str(self.getDefense()) +"\n")
        
class Enemy(Entity):
    'The enemy - objective: to kill you'
        
    def isPlayer(self):
        return False

    def toString(self):
        print("Enemy statistics:\nHealth: " + str(self.getHealth()) + "\nAttack Modifier: " + str(self.getAttack()) + "\nDefense Modifier: " + str(self.getDefense()) +"\n")
       
        
class Dungeon():
    'what do I put here'    #actually find something to put here
    playedGames = 0

    def __init__(self):
        self.level = 1

        self.hero = Player()
    
        Dungeon.playedGames += 1

    def createEncounter(self):
        self.monster = Enemy()

        self.monster.setHealth(random.randint(self.level * 5, (self.level * 5) + 10))
        self.monster.setAttack(random.randint(self.level, self.level * 5) / 10) 
        self.monster.setDefense(random.randint(self.level, self.level * 5) / 10)

        print("You encounter a monster!\n")
        self.monster.toString()
        self.fight_flight()
                          
    def fight_flight(self):
        print("Will you fight the enemy, or will you run away? (write 'f' or 'r')\n")
        fight = input("CHOICE: ")
        print

        if fight == "f":
            self.fight(self.hero, self.monster)
        elif fight == "r":
            print("You attempt to run!\n")
            self.run()

    def run(self):
        chance = random.randint(1, 10)
        if chance >= 7:
            print("You ran away!\n")
            self.level += 1
            print("You delve deeper into the dungeons. Welcome to level " + str(self.level) + "\n")

            self.createEncounter()
        else:
            print("You trip and fall flat on your face.\n")
            self.fight(self.monster, self.hero)

    def fight(self, attacker, target):

        attacker.toString()
        target.toString()
        
        rawAttack = random.randint(1, 10) * attacker.getAttack()
        enemyDefense = random.randint(1, 5) * target.getDefense()
        totalAttack = math.floor(rawAttack - enemyDefense)

        if totalAttack <= 0:
            totalAttack = 0

        if attacker.isPlayer() == True:
            print("You attack for " + str(totalAttack) + " damage!\n")
        elif attacker.isPlayer() == False:
            print("The monster attacks for " + str(totalAttack) + " damage!\n")
        
        target.setHealth(target.getHealth() - totalAttack)

        if target.isPlayer() == True:
            print("You are at " + str(target.getHealth()) + " health!\n")
        elif target.isPlayer() == False:
            print("The monster is at " + str(target.getHealth()) + " health!\n")
            
        self.checkDeath(target)

    def checkDeath(self, entity):
        health = entity.getHealth()
        if (health <= 0):
            if (entity.isPlayer() == True):
                print("You have been slain!")
                sys.exit()
            elif (entity.isPlayer() == False):
                print("You have defeated the enemy!\n")
                self.level += 1
                self.victoryUpgrade()
        elif (health > 0):
            if (entity.isPlayer() == False):
                print("The monster counterattacks!\n")
                self.fight(self.monster, self.hero)
            elif (entity.isPlayer() == True):
                self.fight_flight()
                
    def victoryUpgrade(self):

        option = self.hero.upgrade()

        if option == "1":
            self.hero.setHealth(self.hero.getHealth() + 5)
            print("You are now at " + str(self.hero.getHealth()) + " health!\n")
        elif option == "2":
            self.hero.setAttack(self.hero.getAttack() + 0.5)
            print("You now have a " + str(self.hero.getAttack()) + " attack modifier!\n")
        elif option == "3":
            self.hero.setDefense(self.hero.getDefense() + 0.5)
            print("You now have a " + str(self.hero.getDefense()) + " attack modifier!\n")

        print("You delve deeper into the dungeons. Welcome to level " + str(self.level) + "\n")

        self.createEncounter()
            
# ---- Main Code ----

infiniDungeon = Dungeon()
infiniDungeon.createEncounter()
