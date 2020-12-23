import cqcWeapons

class Player:
    def __init__(self, health, defense, hit_rate, speed, damage):
        self.player_health = health
        self.player_defense = defense
        self.player_hit_rate = hit_rate
        self.player_speed = speed
        self.player_damage = damage
        self.player_inventory_cqc = [{
            'Long Swords': ['']},
            {
            'Short Swords': ['']},
            {
            'Daggers': ['']},
            {
            'Staffs': ['']},
            {
            'Mace': ['']},
            {

        }]
        self.equipped_inventory = [{
            'Head': '',
            'Body': '',
            'Legs': '',
            'Feet': '',
            'Arms': '',
            'Hands': '',
            'CQC Weapon': '',
            'Ranged Weapon': '',

        }]

        cqc_weapons = [{'long swords': ['Basic Long Sword']},
                       {'short swords': ['Basic Short Sword']},
                       ]

    def equip_cqcWeapon(self):
        self.equipped_inventory['CQC Weapon'] = ''

    def unequip_cqcWeapon(self):
        self.unequipped_cqcWeapon = self.equipped_inventory.pop[-2]('')
        for weapons in range(len(cqc_weapons)):
            for weapon_names in cqc_weapons[weapons]:
                if weapon_names == self.unequipped_cqcWeapon:
                    self.player_inventory_cqc[0]['Long Swords'] = [f'{self.unequipped_cqcWeapon}']
                    break
                elif weapon_names == self.unequipped_cqcWeapon:
                    self.player_inventory_cqc[0]['Short Swords'] = [f'{self.unequipped_cqcWeapon}']
                    break
                elif weapon_names == self.unequipped_cqcWeapon:
                    self.player_inventory_cqc[0]['Daggers'] = [f'{self.unequipped_cqcWeapon}']
                    break
                elif weapon_names == self.unequipped_cqcWeapon:
                    self.player_inventory_cqc[0]['Staffs'] = [f'{self.unequipped_cqcWeapon}']
                    break
                elif weapon_names == self.unequipped_cqcWeapon:
                    self.player_inventory_cqc[0]['Maces'] = [f'{self.unequipped_cqcWeapon}']
                    break


    def use_equipped_cqcWeapon(self):
        if self.weapon_type == 'staff':
            self.enemy_health -= self.base_damage * 2
        elif self.weapon_type == 'shortSword':
            self.enemy_health -= self.base_damage * 3
        elif self.weapon_type == 'dagger':
            self.enemy_health -= self.base_damage * 4
        elif self.weapon_type == 'longSword' or self.weapon_type == 'mace':
            self.enemy_health -= self.base_damage
        print(f"You have done {self.base_damage} damage!")



# class player:
#     def __init__(self, player_health=100, player_defense=10, player_hitrate=10):
#         self.player = player_0
#         self.player_health = player_health
#         self.player_defense = player_defense
#         self.player_hitrate = player_hitrate
#
# class playerCondition(player):
#     """This class simply describes the condition of the player."""
#     def __init__(self, player, health, defense, player_hitrate):
#         """Initialize attributes of the parent class."""
#         super().__init__(player, health, defense, player_hitrate)
#
# class playerStatus(player):
#     """This is the status of the player. """
#     def __init__(self, player, health, defense, player_hitrate):
#         """Initialize attributes of the parent class."""
#         super().__init__(player, health, defense, player_hitrate)