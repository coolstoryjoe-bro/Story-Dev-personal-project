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

        self.longSword = [self.longSword_dmg, self.base_hitrateLS, self.base_durabilityLS]
        self.longSword_dmg = 25
        self.base_hitrateLS = 10
        self.base_durabilityLS = 125

    def equip_longSword(self):
        player_usable_inventory.append(self.longSword)

    def unqeuip_longSword(self):
        player_usable_inventory.remove(self.longSword)
        player_inventory.append(self.longSword)

    def use_longSword(self):
        total_dmgLS = self.longSword_dmg
        print("You have done 25 damage!")

class mace(cqcWeapons):
    """Status for mace"""
    def __init__(self, base_damage, base_durability, base_hitrate):
        super().__init__(base_damage, base_durability, base_hitrate)

        self.mace = [self.mace_dmg, self.base_hitrateM, self.base_durabilityM]
        self.mace_dmg = 15
        self.base_hitrateM = 8
        self.base_durabilityM = 150

    def equip_mace(self):
        player_usable_inventory.append(self.mace)

    def unequip_mace(self):
        player_usable_inventory.remove(self.mace)
        player_inventory.append(self.mace)

    def use_mace(self):
        total_dmgM = self.mace_dmg
        print("You have done 15 damage!")

class shortSword(cqcWeapons):
    """Status for shortSword. """
    def __init__(self, base_damage, base_durability, base_hitrate):
        super().__init__(base_damage, base_durability, base_hitrate)

        self.shortSword = [self.shortSword_dmg, self.base_durabilitySS, self.base_hitrateSS]
        self.shortSword_dmg = 10
        self.base_hitrateSS = 25
        self.base_durabilitySS = 85

    def equip_shortSword(self):
        player_usable_inventory.append(self.shortSword)

    def unequip_shortSword(self):
        player_usable_inventory.remove(self.shortSword)
        player_inventory.append(self.shortSword)

    def use_shortSword(self):
        total_dmgSS = self.shortSword_dmg * 2
        print(f"You have swung your shortsword twice to deal a total of {total_dmgSS} damage!")

class dagger(cqcWeapons):
    """Status for dagger"""
    def __init__(self, base_damage, base_durability, base_hitrate):
        super().__init__(base_damage, base_durability, base_hitrate)

        self.dagger = [self.dagger_dmg, self.base_hitrateD, self.base_durabilityD]
        self.dagger_dmg = 5
        self.base_hitrateD = 35
        self.base_durabilityD = 60

    def equip_dagger(self):
        player_usable_inventory.append(self.dagger)

    def unequip_dagger(self):
        player_usable_inventory.remove(self.dagger)
        player_inventory.append(self.dagger)

    def use_Dagger(self):
        total_dmgD = self.dagger_dmg * 5
        print(f"You have swung your 5 times to deal a total of {total_dmgD} damage!")

class staff(cqcWeapons):
    """Status for staff. """
    def __init__(self, base_damage, base_durability, base_hitrate):
        super().__init__(base_damage, base_durability, base_hitrate)

        self.staff = [self.staff_dmg, self.base_durabilityS, self.base_hitrateS]
        self.staff_dmg = 10
        self.base_hitrateS = 20
        self.base_durabilityS = 60

    def equip_staff(self):
        player_usable_inventory.append(self.staff)

    def unequip_staff(self):
        player_usable_inventory.remove(self.staff)
        player_inventory.append(self.staff)

    def use_staff_melee(self):
        total_DmgS = self.staff_dmg * 2
        print("You have decided to use your staff in a melee to deal a total of 20 damage!")