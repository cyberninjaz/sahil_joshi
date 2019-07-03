import random

class Enemy:
    health = None
    damage = None

    def __init__(self, health, damage):
        self.health = health
        self.damage = damage 

class EnemyRoom:
    enemies = None

    def __init__(self):
        self.enemies = list() 
        for i in range(0, random.randint(1,10)):
            self.enemies.append( Enemy( random.randint(1, 6), random.randint(1, 10) ) )

class LootRoom:
    gear = None

    def __init__(self, gear):
        self.gear = gear

class BossRoom:
    enemy = None

    def __init__(self, enemy):
        self.enemy = enemy

class Player:
    health = None

    def __init__(self, health):
        self.health = health

def randomroom():
    number = random.randint(1, 3)
    if number == 1:
        return EnemyRoom()
    if number == 2:
        return LootRoom( random.randint(0, 6) )
    if number == 3:
        return BossRoom( Enemy( random.randint(10,50), random.randint(10,20) ) )

print("welcome to the game")

roomimgoingin = randomroom()

