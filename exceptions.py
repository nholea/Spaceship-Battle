
class DestroyedSpaceship(Exception):
    def __init__(self, message):
        super().__init__(message)

class NotEnoughPower(Exception):
    def __init__(self, message):
        super().__init__(message)
