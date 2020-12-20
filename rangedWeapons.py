
# This is the class for ranged weapons.
class rangedWeapons:
    def __init__(self, attack_dmg=1, attack_range=1, attack_rate=1, status_effect={}, ):
        self.attack_dmg = attack_dmg
        self.attack_range = attack_range
        self.attack_rate = attack_rate
        self.status_effect = status_effect


class longBow(rangedWeapons):
    def __init__(self, attack_dmg, attack_range, attack_rate, status_effect):
        super().__init__(attack_dmg, attack_range, attack_rate, status_effect)

        self.attack_dmg = 35
        self.attack_rate = 7
        self.attack_range = 100

    def use_longBow(self):
        self.arrow_vary = input("Would you like to use an arrow effect? (yes/no)")
        if self.arrow_vary.lower() == 'yes' or self.arrow_vary.upper() == 'YES' or self.arrow_vary.title() == 'Yes':
            print(f"This is your list of status affecting arrows: {self.status_effect}")
            for self.status in self.status_effect:
                if self.status_effect.values() == [1] or self.status_effect.values() == [2] \
                        or self.status_effect.values() == [3] or self.status_effect.values() == [4] \
                        or self.status_effect.values() == [5] or self.status_effect.values() == [6]:
                    print(f"You don't have any status effecting arrows. You will use a regular arrow instead!")
                    print(f"You have used {self.status}")
                    break
        elif self.arrow_vary.lower() == 'no' or self.arrow_vary.upper() == 'NO' or self.arrow_vary.title() == 'No':
            print(f"You have used a regular arrow and have done {self.attack_dmg} damage!")



class shortBow(rangedWeapons):
    def __init__(self, attack_dmg, attack_range, attack_rate, status_effect):
        super().__init__(attack_dmg, attack_range, attack_rate, status_effect)

        self.attack_dmg = 15
        self.attack_rate = 3
        self.attack_range = 50

    def use_shortBow(self):
        self.arrow_vary = input("Would you like to use an arrow effect? (yes/no)")
        if self.arrow_vary.lower() == 'yes' or self.arrow_vary.upper() == 'YES' or self.arrow_vary.title() == 'Yes':
            print(f"This is your list of status affecting arrows: {self.status_effect}")
            for self.status in self.status_effect:
                if self.status_effect.values() == [1] or self.status_effect.values() == [2] \
                        or self.status_effect.values() == [3] or self.status_effect.values() == [4] \
                        or self.status_effect.values() == [5] or self.status_effect.values() == [6]:
                    print(f"You don't have any status effecting arrows. You will use a regular arrow instead!")
                    print(f"You have used {self.status}")
                    break
        elif self.arrow_vary.lower() == 'no' or self.arrow_vary.upper() == 'NO' or self.arrow_vary.title() == 'No':
            print(f"You have used a regular arrow and have done {self.attack_dmg} damage!")


class crossBow(rangedWeapons):
    def __init__(self, attack_dmg, attack_range, attack_rate, status_effect):
        super().__init__(attack_dmg, attack_range, attack_rate, status_effect)

        self.attack_dmg = 50
        self.attack_rate = 15
        self.attack_range = 150

    def use_crossBow(self):
        self.arrow_vary = input("Would you like to use an arrow effect? (yes/no)")
        if self.arrow_vary.lower() == 'yes' or self.arrow_vary.upper() == 'YES' or self.arrow_vary.title() == 'Yes':
            print(f"This is your list of status affecting arrows: {self.status_effect}")
            for self.status in self.status_effect:
                if self.status_effect.values() == [1] or self.status_effect.values() == [2] \
                        or self.status_effect.values() == [3] or self.status_effect.values() == [4] \
                        or self.status_effect.values() == [5] or self.status_effect.values() == [6]:
                    print(f"You don't have any status effecting arrows. You will use a regular arrow instead!")
                    print(f"You have used {self.status}")
                    break
        elif self.arrow_vary.lower() == 'no' or self.arrow_vary.upper() == 'NO' or self.arrow_vary.title() == 'No':
            print(f"You have used a regular arrow and have done {self.attack_dmg} damage!")


class thrownRock(rangedWeapons):
    def __init__(self, attack_dmg, attack_range, attack_rate, status_effect):
        super().__init__(attack_dmg, attack_range, attack_rate, status_effect)

        self.attack_dmg = 2
        self.attack_rate = 3
        self.attack_range = 5

    def use_thrownRock(self):
        print(f"You have chosen to throw a rock to deal a total of {self.attack_dmg} damage!")

class musket(rangedWeapons):
    def __init__(self, attack_dmg, attack_range, attack_rate, status_effect):
        super().__init__(attack_dmg, attack_range, attack_rate, status_effect)

        self.attack_dmg = 35
        self.attack_rate = 7
        self.attack_range = 100

    def use_musket(self):
        self.bullet_vary = input("Would you like to use an bullet effect? (yes/no)")
        if self.bullet_vary.lower() == 'yes' or self.bullet_vary.upper() == 'YES' or self.bullet_vary.title() == 'Yes':
            print(f"This is your list of status affecting bullets: {self.status_effect}")
            for self.status in self.status_effect:
                if self.status_effect.values() == [1] or self.status_effect.values() == [2] \
                        or self.status_effect.values() == [3] or self.status_effect.values() == [4] \
                        or self.status_effect.values() == [5] or self.status_effect.values() == [6]:
                    print(f"You don't have any status effecting bullets. You will use a regular bullet instead!")
                    print(f"You have used {self.status}")
                    break
        elif self.bullet_vary.lower() == 'no' or self.bullet_vary.upper() == 'NO' or self.bullet_vary.title() == 'No':
            print(f"You have used a regular bullet and have done {self.attack_dmg} damage!")

