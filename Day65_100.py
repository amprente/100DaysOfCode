print("🌟=_= Generic RPG =_=🌟\n")
print("Player:\n")


# Base class for all characters in the game
class Character:
    def __init__(self, name, health, magic_points):
        self.name = name
        self.health = health
        self.magic_points = magic_points

    def display(self):
        return f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magic_points}\n"

# Player class inheriting from Character
class Player(Character):
    def __init__(self, name, health, magic_points, lives):
        super().__init__(name, health, magic_points)
        self.lives = lives

    def am_i_alive(self):
        return "Yes" if self.lives > 0 else "No"

    def display(self):
        return super().display() + f"Lives: {self.lives}\nAlive?: {self.am_i_alive()}\n"

# Enemy class inheriting from Character
class Enemy(Character):
    def __init__(self, name, health, magic_points, type, strength):
        super().__init__(name, health, magic_points)
        self.type = type
        self.strength = strength

    def display(self):
        return super().display() + f"Type: {self.type}\nStrength: {self.strength}\n"

# Orc class inheriting from Enemy
class Orc(Enemy):
    def __init__(self, name, health, magic_points, strength, speed):
        super().__init__(name, health, magic_points, "Orc", strength)
        self.speed = speed

    def display(self):
        return super().display() + f"Speed: {self.speed}\n"

# Vampire class inheriting from Enemy
class Vampire(Enemy):
    def __init__(self, name, health, magic_points, strength, day_night):
        super().__init__(name, health, magic_points, "Vampire", strength)
        self.day_night = day_night

    def display(self):
        return super().display() + f"Day/Night?: {self.day_night}\n"

# Instantiating characters
player = Player("Ampry", 100, 50, 3)
vampire1 = Vampire("Gray", 45, 70, 3, "Night")
vampire2 = Vampire("Bety", 70, 10, 75, "Day")
orc1 = Orc("Ugly", 60, 5, 75, 90)
orc2 = Orc("Bidon", 75, 40, 80, 45)
orc3 = Orc("Relu", 35, 40, 49, 50)

# Printing character information
characters = [player, vampire1, vampire2, orc1, orc2, orc3]
for character in characters:
    print(character.display())

