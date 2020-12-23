class Enemies:
    """Describing the basic parameters of an enemy: """
    def __init__(self, name, health, damage, speed,):
        self.name = name
        self.enemy_health = health
        self.damage = damage
        self.speed = speed
        self.defense = 0

    def enemy_Attack(self):
        """This is the function for the enemy attacking the player. """
        if self.speed > 10:
            player_health -= self.damage * 2
        elif self.speed > 20:
            player_health -= self.damage * 3
        elif self.speed > 30:
            player_health -= self.damage * 4
        elif self.speed > 40:
            player_health -= self.damage * 5
        else:
            player_health -= self.damage

    def enemy_Defend(self):
        """This is the function for the enemy defending against the player. """
        if humanEnemies:
            if self.health > 10:
                self.defense += 1
            elif self.health >= 20:
                self.defense += 2
            elif self.health >= 30:
                self.defense += 3
            elif self.health >= 40:
                self.defense += 4
            elif self.health >= 50:
                self.defense += 5
            elif self.health >= 60:
                self.defense += 7
            elif self.health >= 70:
                self.defense += 9
            elif self.health >= 80:
                self.defense += 12
            elif self.health >= 90:
                self.defense += 15
            elif self.health >= 100:
                self.defense += 20
        
class humanEnemies(Enemies):
    """Initializing the super class"""
    def __init__(self, name, health, damage, speed):
        super().__init__(name, health, damage, speed)

class animalEnemies(Enemies):
    """Initializing the super class"""
    def __init__(self, name, health, damage, speed):
        super().__init__(name, health, damage, speed)

class undeadEnemies(Enemies):
    """Initializing the super class"""
    def __init__(self, name, health, damage, speed):
        super().__init__(name, health, damage, speed)

class demonicEnemies(Enemies):
    """Initializing the super class"""
    def __init__(self, name, health, damage, speed):
        super().__init__(name, health, damage, speed)

# Enemy Types:
regular_boar = Enemies('boar', 10, 1, 'slow')
thief = Enemies(humanEnemies('thief', 15, 3, 'slow'))