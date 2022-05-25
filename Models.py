class Spaceship():
    __protection = True

    def __init__(self, name, health):
        self.name = name
        self.health = int(health)

    def serialize(self):
        return{"name": self.name, "health": self.health}

    def state(self):
        return "Destroyed" if self.health <= 0 else "Still working"

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
            spaceship.health -= 1
            spaceship.active_protection()
        

spaceships = []