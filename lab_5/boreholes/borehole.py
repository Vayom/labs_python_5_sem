class Borehole:
    def __init__(self, level):
        self.speed = None
        self.level = level
        self.is_enabled = True
        self.calculate_speed()

    def turn_on(self):
        self.is_enabled = True

    def turn_off(self):
        self.is_enabled = False

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value in [1, 2, 3]:
            self._level = value
            self.calculate_speed()
        else:
            raise ValueError("Level must be 1, 2, or 3")

    def calculate_speed(self):
        if self.level == 1:
            self.speed = 5
        elif self.level == 2:
            self.speed = 15
        elif self.level == 3:
            self.speed = 30

    def set_parameters(self, level):
        self.level = level


if __name__ == '__main__':
    pass
