class Borehole:
    def __init__(self, borehole_type, level):
        self.speed = None
        self.level = level
        self.borehole_type = borehole_type
        self.contents_volume = 0
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

    def set_parameters(self, contents_volume):
        self.contents_volume = contents_volume

    def show_parameters(self):
        print(f"Well Type: {self.borehole_type}")
        print(f"Contents Volume: {self.contents_volume}")
        print(f"Status: {'Enabled' if self.is_enabled else 'Disabled'}")

    def __str__(self):
        return f'{self.borehole_type} - {self.level}'
