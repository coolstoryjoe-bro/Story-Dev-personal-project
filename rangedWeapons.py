# A short list of the ranged weapons that i've listed in chapter one.
ranged_weapons = ['longbow', 'shortbow', 'crossbow', 'thrownrock', 'musket',]

class rangedWeapons:
    def __init__(self):
        self.attack_dmg = 1
        self.attack_range = 115
        self.attack_rate = 1
        self.status_effect = []


class longBow(rangedWeapons):
    def __init__(self, attack_dmg, attack_range, attack_rate, status_effect):
        super().__init__(attack_dmg, attack_range, attack_rate, status_effect)

class shortBow(rangedWeapons):
    def __init__(self, attack_dmg, attack_range, attack_rate, status_effect):
        super().__init__(attack_dmg, attack_range, attack_rate, status_effect)

class crossBow(rangedWeapons):
    def __init__(self, attack_dmg, attack_range, attack_rate, status_effect):
        super().__init__(attack_dmg, attack_range, attack_rate, status_effect)

class thrownRock(rangedWeapons):
    def __init__(self, attack_dmg, attack_range, attack_rate, status_effect):
        super().__init__(attack_dmg, attack_range, attack_rate, status_effect)

class musket(rangedWeapons):
    def __init__(self, attack_dmg, attack_range, attack_rate, status_effect):
        super().__init__(attack_dmg, attack_range, attack_rate, status_effect)
