"""
This file stores metadata about the vehicle
"""


class Vehicle:
    def __init__(self, registration_number, colour):
        self.registration_number = registration_number
        self.colour = colour

    def __str__(self):
        return 'Vehicle {} {}'.format(self.registration_number, self.colour)
