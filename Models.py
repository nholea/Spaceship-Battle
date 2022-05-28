from exceptions import DestroyedSpaceship, NotEnoughPower

class Weapon():
    def __init__(self,weapon_power_needed,power_consumed_by_weapon ):
        if (weapon_power_needed > 0) and (power_consumed_by_weapon > 0) and power_consumed_by_weapon <= weapon_power_needed:
            self.weapon_power_needed = weapon_power_needed
            self.power_consumed_by_weapon = power_consumed_by_weapon 
        else:
            raise ValueError("Power needed and consumed must be > 0. Power consumed must be <= Power needed")
        
    def shoot(self, target):
        if self.power_consumed_by_weapon == self.weapon_power_needed:
            if target.health > 0:
                target.health -= 1
        else:
            raise NotEnoughPower("The weapon does not have enough power to shoot.")

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

    power_not_in_use = 0
    

    def serialize(self):
        return{"name": self.name, "health": self.health, "weapon": self.weapon.serialize(), "generator":self.generator.serialize()}

    def state(self):
        return "Destroyed" if self.health == 0 else "Still working"


    def shoot_at(self, target):
        if self.health > 0:
            if self.weapon.power_consumed_by_weapon <= self.generator.total_power:
                self.weapon.shoot(target)
                self.power_not_in_use = self.generator.total_power - self.weapon.power_consumed_by_weapon
            else:
                raise NotEnoughPower("The total power is not enough")
        else:
            raise DestroyedSpaceship("The Spaceship is destroyed. Cannot shoot")

spaceships = []
