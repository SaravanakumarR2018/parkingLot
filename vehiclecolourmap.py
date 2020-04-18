"""
This file contains two maps
vehicle_registation_num_map -
   Vehicle registration number : Slot Number under a Node

Vehicle Colour map
   vehicle colour: set of slot numbers

"""
import logging

logger = logging.getLogger('ParkingLot')

from vehicle import Vehicle
from slot import Slot


class VehicleColourMap:
    def __init__(self):
        self.vehicle_registation_num_map = {}
        self.vehicle_colour_map = {}

    def get_slot(self, registration_number):
        return self.vehicle_registation_num_map.get(registration_number)

    def get_set_of_slots(self, colour):
        if colour not in self.vehicle_colour_map:
            return {}
        car_slot_set = self.vehicle_colour_map[colour]
        return car_slot_set

    def __str__(self):
        output = 'Vechicle Registation Map \n'
        for key in self.vehicle_registation_num_map:
            output += str(key) + ':' + str(self.vehicle_registation_num_map[key]) + '\n'
        output += '\nVehicle colour map \n'
        for key in self.vehicle_colour_map:
            output += str(key) + ':' + str(self.vehicle_colour_map[key]) + '\n'
        return output

    def insert(self, slot):
        colour_map = self.vehicle_colour_map.get(slot.vehicle.colour)
        if colour_map is None:
            colour_map = {slot.slot}
            self.vehicle_colour_map[slot.vehicle.colour] = colour_map
        else:
            colour_map.add(slot.slot)
        self.vehicle_registation_num_map[slot.vehicle.registration_number] = slot.slot

    def delete(self, slot):
        slot_number = slot.slot
        colour = slot.vehicle.colour
        colour_map = self.vehicle_colour_map.get(colour, None)
        if colour_map is not None:
            colour_map.remove(slot_number)
            if len(colour_map) == 0:
                del self.vehicle_colour_map[colour]
        del self.vehicle_registation_num_map[slot.vehicle.registration_number]


if __name__ == '__main__':
    log_handler = logging.FileHandler('parkingLot.log')
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)
    vcm = VehicleColourMap()
    v1 = Vehicle('KA01PY1111', 'White')
    s1 = Slot(1, v1)
    v2 = Vehicle('KA02PY1111', 'Blue')
    s2 = Slot(2, v2)
    v3 = Vehicle('KA03PY1111', 'White')
    s3 = Slot(3, v3)
    v4 = Vehicle('KA04PY1111', 'Blue')
    s4 = Slot(4, v4)
    v5 = Vehicle('KA05PY1111', 'Ash')
    s5 = Slot(5, v5)
    vcm.insert(s1)
    vcm.insert(s2)
    vcm.insert(s3)
    vcm.insert(s4)
    vcm.insert(s5)
    logger.debug(vcm)

    logger.debug('\n REMOVING SLOT 4 \n')
    vcm.delete(s4)
    logger.debug(vcm)
    logger.debug('\n REMOVING SLOT 2 \n')
    vcm.delete(s2)
    logger.debug(vcm)
    logger.debug('\n REMOVING SLOT 5 \n')
    vcm.delete(s5)
    logger.debug(vcm)
    logger.debug('\n REMOVING SLOT 1 \n')
    vcm.delete(s1)
    logger.debug(vcm)
    logger.debug('\n REMOVING SLOT 3 \n')
    vcm.delete(s3)
    logger.debug(vcm)
