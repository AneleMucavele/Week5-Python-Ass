# Parent Class
class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.strength = strength

    def introduce(self):
        return f"I am {self.name} and I have the power of {self.power}!"

    def show_strength(self):
        return f"My strength level is {self.strength}/100."

# Child Class demonstrating inheritance
class WaterHero(Superhero):
    def __init__(self, name, strength, special_move):
        super().__init__(name, "Water Control", strength)
        self.special_move = special_move

    def use_special(self):
        return f"{self.name} uses {self.special_move}!"

# Creating objects
hero1 = Superhero("Solar Blaze", "Fire Control", 85)
hero2 = WaterHero("Aqua Storm", 90, "Tsunami Wave")

# Output
print(hero1.introduce())
print(hero1.show_strength())

print(hero2.introduce())
print(hero2.use_special())
