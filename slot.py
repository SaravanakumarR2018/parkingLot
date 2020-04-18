"""
This file contains the Slot class
Each instance of the class stores the slot and the vehicle details which are instances of Vehicle Class
"""


class Slot:
    def __init__(self, slot, vehicle):
        self.slot = slot
        self.vehicle = vehicle

    def __str__(self):
        return 'Slot {} {}'.format(self.slot, self.vehicle)
