# The CQC class that contains all the weapons as classes and subclasses for their own OOP.
class cqcWeapons:
    def __init__(self, base_damage, base_durability, base_hitrate):
        self.base_damage = base_damage
        self.base_durability = base_durability
        self.base_hitrate = base_hitrate

class longSword(cqcWeapons):
    """Status for longsword"""
    def __init__(self, base_damage, base_durability, base_hitrate):
        super().__init__(base_damage, base_durability, base_hitrate)

        self.longSword_dmg = 25
        self.base_hitrate = 10
        self.base_durability = 100

    def use_longSword(self):
        total_dmgLS = self.longSword_dmg
        print("You have done 25 damage!")

class mace(cqcWeapons):
    """Status for mace"""
    def __init__(self, base_damage, base_durability, base_hitrate):
        super().__init__(base_damage, base_durability, base_hitrate)

        self.mace_dmg = 15

    def use_mace(self):
        total_dmgM = self.mace_dmg
        print("You have done 15 damage!")

class shortSword(cqcWeapons):
    """Status for shortSword. """
    def __init__(self, base_damage, base_durability, base_hitrate):
        super().__init__(base_damage, base_durability, base_hitrate)

        self.shortSword_dmg = 10

    def use_shortSword(self):
        total_dmgSS = self.shortSword_dmg * 2
        print(f"You have swung your shortsword twice to deal a total of {total_dmgSS} damage!")

class dagger(cqcWeapons):
    """Status for dagger"""
    def __init__(self, base_damage, base_durability, base_hitrate):
        super().__init__(base_damage, base_durability, base_hitrate)

        self.dagger_dmg = 5

    def use_Dagger(self):
        total_dmgD = self.dagger_dmg * 5
        print(f"You have swung your 5 times to deal a total of {total_dmgD} damage!")

class staff(cqcWeapons):
    """Status for staff. """
    def __init__(self, base_damage, base_durability, base_hitrate):
        super().__init__(base_damage, base_durability, base_hitrate)

        self.staff_dmg = 10

    def use_staff_melee(self):
        total_DmgS = self.staff_dmg * 2
        print("You have decided to use your staff in a melee to deal a total of 20 damage!")