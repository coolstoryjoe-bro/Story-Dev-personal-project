class passiveDamage():
    """This class described the passive damage the player gets."""
    def __init__(self, poison, blunt, slash, burning, freezing, electric, random):
        self.poison = poison
        self.burning = burning
        self.freezing = freezing
        self.electric = electric
        self.random = random

    def poison_damage(self):
        print("You have been poisoned.")
        timer_poison = 0
        poison_dmg = 2
        while timer_poison <= 7:
            timer_poison += 1
            poison_dmg -= self.health
            continue

    def burning_damage(self):
        print("You are suffering from burning. ")
        timer_burning = 0
        burning_dmg = 5
        while timer_burning <= 5:
            timer_burning += 1
            burning_dmg -= self.health
            continue

    def freezing_damage(self):
        print("You are currently freezing. ")
        timer_freezing = 0
        freezing_dmg = 5
        while timer_freezing <= 3:
            timer_freezing += 1
            freezing_dmg -= self.health
            continue
        freezing_slow = 2
        freezing_slow -= self.player_hitrate

    def electric_damage(self):
        print("You are suffering from electrical currents. ")
        timer_electric = 0
        electric_dmg = 3
        while timer_electric <= 5:
            timer_electric += 1
            electric_dmg -= self.health
            continue