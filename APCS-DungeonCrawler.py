# Andrew Zhou
# Dungeon Crawler - Final Project

# ------ Importing Libraries ------

import random
import sys
import math

# ------ Class Definitions ------

# Entity Superclass

class Entity():                                                                                    
        
    def __init__(self, hp=10, attack=1.0, defense=1.0):             # Initializes Entity - w/o parameters, it designates its own parameters
        self.health = hp
        self.atk = attack
        self.defn = defense
        
    def setHealth(self, hp):                                        # Health Mutator
        if self.health <= 0:
            self.health = 0
        else:
            self.health = hp
    def setAttack(self, attack):                                    # Attack Modifier Mutator
        self.atk = attack
    def setDefense(self, defense):                                  # Defense Modifier Mutator
        self.defn = defense
        
    def getHealth(self):                                            # Health Accessor
        return self.health
    def getAttack(self):                                            # Attack Modifier Mutator
        return self.atk
    def getDefense(self):                                           # Defense Modifier Mutator
        return self.defn

# Player Subclass (subclass of Entity)

class Player(Entity):                                               

    def upgrade(self):                                              # Upgrade Method - occurs after successful combat
        print("You enter a shop and inspect the wares:\n")
        print("1. Health Upgrade (from " + str(self.getHealth()) + " to " + str(self.getHealth() + 10) + ")")
        print("2. Sword Upgrade (from " + str(self.getAttack()) + " to " + str(self.getAttack() + 0.5) + ")")
        print("3. Shield Upgrade (from " + str(self.getDefense()) + " to " + str(self.getDefense() + 0.5) + ")")

        choice = input("1, 2 or, 3: ")

        return choice
        
    def isPlayer(self):                                             # Returns True if Player
        return True

    def toString(self):                                             # Returns stats
        print("Player statistics:\nHealth: " + str(self.getHealth()) + "\nAttack Modifier: " + str(self.getAttack()) + "\nDefense Modifier: " + str(self.getDefense()) +"\n")

# Enemy Subclass (subclass of Entity)

class Enemy(Entity):
        
    def isPlayer(self):                                             # Returns False since Enemy is not a Player
        return False

    def toString(self):                                             # Returns stats
        print("Enemy statistics:\nHealth: " + str(self.getHealth()) + "\nAttack Modifier: " + str(self.getAttack()) + "\nDefense Modifier: " + str(self.getDefense()) +"\n")

# Dungeon Class
        
class Dungeon():

    playedGames = 0                                                 # Number of Games Played

    def __init__(self):
        self.level = 1                                              # Level of dungeon

        self.hero = Player()                                        # Creates Player Character
    
        Dungeon.playedGames += 1                                    # Adds 1 to number of games played                                   
        print("Game: " + str(Dungeon.playedGames))                  # Prints # of games played

    def createEncounter(self):                                      # Creates an Enemy using randomized stats based off dungeon level
        self.monster = Enemy()

        self.monster.setHealth(random.randint(self.level * 5, (self.level * 5) + 10))
        self.monster.setAttack(random.randint(self.level, self.level * 5) / 10) 
        self.monster.setDefense(random.randint(self.level, self.level * 5) / 10)

        print("You encounter a monster!\n")
        self.monster.toString()
        self.fight_flight()                                     
                          
    def fight_flight(self):                                         # Asks if user wants to fight the monster or run
        print("Will you fight the enemy, or will you run away? (write 'f' or 'r')\n")
        fight = input("CHOICE: ")
        print

        if fight == "f":
            self.fight(self.hero, self.monster)
        elif fight == "r":
            print("You attempt to run!\n")
            self.run()

    def run(self):                                                  # Run Method - based off random chance
        chance = random.randint(1, 10)
        if chance >= 7:
            print("You ran away!\n")
            self.level += 1
            print("You delve deeper into the dungeons. Welcome to level " + str(self.level) + "\n")

            self.createEncounter()
        else:
            print("You trip and fall flat on your face.\n")
            self.fight(self.monster, self.hero)

    def fight(self, attacker, target):                              # Fight Method

        print("\t------ Statistics ------\n")
        attacker.toString()                                         # Print Player and Enemy Stats
        target.toString()
        
        rawAttack = random.randint(1, 10) * attacker.getAttack()    # Total Attack is Raw Attack (random) minus Enemy Defense (random)
        enemyDefense = random.randint(1, 5) * target.getDefense()
        totalAttack = math.floor(rawAttack - enemyDefense)

        if totalAttack <= 0:                                        # Ensuring there can't be a negative total attack
            totalAttack = 0

        print("\t------ Actions ------\n")                          # Writing Changes for whether a Player or Enemy is attacking
        if attacker.isPlayer() == True:
            print("You attack for " + str(totalAttack) + " damage!\n")
        elif attacker.isPlayer() == False:
            print("The monster attacks for " + str(totalAttack) + " damage!\n")
        
        target.setHealth(target.getHealth() - totalAttack)

        if target.isPlayer() == True:                               # Writing Changes for whether a Player or Enemy is defending
            print("You are at " + str(target.getHealth()) + " health!\n")
        elif target.isPlayer() == False:
            print("The monster is at " + str(target.getHealth()) + " health!\n")
            
        self.checkDeath(target)                                    

    def checkDeath(self, entity):                                   # Checks if target has died
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
                
    def victoryUpgrade(self):                                       # Upgrades the Player

        option = self.hero.upgrade()

        if option == "1":
            self.hero.setHealth(self.hero.getHealth() + 10)
            print("You are now at " + str(self.hero.getHealth()) + " health!\n")
        elif option == "2":
            self.hero.setAttack(self.hero.getAttack() + 0.5)
            print("You now have a " + str(self.hero.getAttack()) + " attack modifier!\n")
        elif option == "3":
            self.hero.setDefense(self.hero.getDefense() + 0.5)
            print("You now have a " + str(self.hero.getDefense()) + " defense modifier!\n")

        print("You delve deeper into the dungeons. Welcome to level " + str(self.level) + "\n")

        self.createEncounter()
            
# ------ Main Code ------

print("\t------ InfiniDungeon ------\n")

infiniDungeon = Dungeon()
infiniDungeon.createEncounter()
