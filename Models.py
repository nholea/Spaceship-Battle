class Spaceship():
    __protection = True

    def __init__(self, name, health):
        if type(health) == int and health >=0:
            self.name=name
            self.health = health
        else:
            raise ValueError("Health must be an integer and never <0")

    def serialize(self):
        return{"name": self.name, "health": self.health}

    def state(self):
        return "Destroyed" if self.health == 0 else "Still working"

    def active_protection(self):
        self.__protection = True

    def remove_protection(self):
        self.__protection= False

    def protection(self):
        return self.__protection

    def battle(self, spaceship):
        if spaceship.protection():
            spaceship.remove_protection()
        else:
            if spaceship.health >0:
                spaceship.health -= 1
                spaceship.active_protection()
        

spaceships = []
