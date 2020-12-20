defense_list = ['woodenshield', 'shortshield', 'tallshield', 'leatherarmor',
                 'chainmail', 'ironarmor', 'chainarmor', ]

class defensiveItems:
    def __init__(self, base_defense=1, base_durability=200 ):
        self.base_defense = base_defense
        self.base_durability = base_durability


class woodenShield(defensiveItems):
    def __init__(self, base_defense=1, base_durability=200):
        super().__init__(base_defense, base_durability)

        self.woodenShield_defense = 10

    def equip_woodenShield(self):
        self.woodenShield_defense += self.player_defense
        print(f"You have equiped a wooden shield with {self.woodenShield_defense} defense!")

    def unequip_woodenShield(self):
        self.woodenShield_defense -= self.player_defense
        print(f"You have unequiped a wooden shield. You now have {self.player_defense} defense.")


class shortShield(defensiveItems):
    def __init__(self, base_defense=1, base_durability=200):
        super().__init__(base_defense, base_durability)

        self.shortShield_defense = 15

    def equip_shortShield(self):
        self.shortShield_defense = self.player_defense
        print(f"You have equiped a short shield with {self.shortShield_defense} defense!")
