class Borehole:
    def __init__(self, level):
        self.speed = None
        self.level = level
        self.is_enabled = False
        self.calculate_speed()

    def turn_on(self):
        self.is_enabled = True

    def turn_off(self):
        self.is_enabled = False

    def calculate_speed(self):
        if self.level == 1:
            self.speed = 5
        elif self.level == 2:
            self.speed = 15
        elif self.level == 3:
            self.speed = 30

    def set_parameters(self, level):
        self.level = level
        self.calculate_speed()
