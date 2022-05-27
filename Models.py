from exceptions import DestroyedSpaceship

class Weapon():
    def __init__(self,weapon_power_needed,power_consumed_by_weapon ):
        if weapon_power_needed > 0 and power_consumed_by_weapon > 0:
            self.weapon_power_needed = weapon_power_needed
            self.power_consumed_by_weapon = power_consumed_by_weapon 
        else:
            raise ValueError("Power needed and consumend must be > 0")
        
    def shoot(self, target):
        if target.health > 0:
            target.health -= 1

    def serialize(self):
        return {"power needed":self.weapon_power_needed, "power consumed": self.power_consumed_by_weapon}

class Generator():
    def __init__(self,total_power):
        if total_power >= 0:
            self.total_power = total_power
        else:
            raise ValueError("Total power must be an integer >=0")

    def serialize(self):
        return {"total power":self.total_power}


class Spaceship():
    def __init__(self, name, health, weapon, generator):
        if type(health) == int and health >= 0:
            self.name=name
            self.health = health
            self.weapon = weapon
            self.generator = generator
        else:
            raise ValueError("Health must be an integer and never <0")

    def serialize(self):
        return{"name": self.name, "health": self.health, "weapon": self.weapon.serialize(), "generator":self.generator.serialize()}

    def state(self):
        return "Destroyed" if self.health == 0 else "Still working"

    def shoot_at(self, target):
        if self.health > 0:
            self.weapon.shoot(target)
        else:
            raise DestroyedSpaceship("The Spaceship is destroyed. Cannot shoot")

spaceships = []

holi = Spaceship("A", 0, Weapon(6,3),Generator(15))
holi2 = Spaceship("A",5,Weapon(4,1),Generator(2))
print(holi.serialize())
holi2.shoot_at(holi)







