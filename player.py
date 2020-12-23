class Player:
    def __init__(self, health, defense, hit_rate, speed, damage):
        self.player_health = health
        self.player_defense = defense
        self.player_hit_rate = hit_rate
        self.player_speed = speed
        self.player_damage = damage

    def use_equipped_cqcWeapon(self):
        if self.base_hitrate > 10:
            self.enemy_health -= self.base_damage * 2
        elif self.base_hitrate > 20:
            self.enemy_health -= self.base_damage * 3
        elif self.base_hitrate > 30:
            self.enemy_health -= self.base_damage * 4
        else:
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