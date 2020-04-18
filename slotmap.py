"""
This class stores the vehicle in a particular slot within a hash map
slot_map

slot number : (slot number, vehicle number and colour)
"""
import logging

logger = logging.getLogger('ParkingLot')

from vehicle import Vehicle
from slot import Slot


class SlotMap:
    def __init__(self):
        self.slot_map = {}

    def insert(self, slot):
        self.slot_map[slot.slot] = slot

    def delete(self, slot_number):
        del self.slot_map[slot_number]

    def get_slot_object(self, slot_number):
        return self.slot_map.get(slot_number)

    def display_status(self):
        slot_list = []
        for slot in self.slot_map:
            slot_list.append(slot)
        logger.debug('Slot No.    Registration No    Colour')
        print('Slot No.    Registration No    Colour')
        slot_list.sort()
        for slot in slot_list:
            slot_obj = self.slot_map[slot]
            registration_num = slot_obj.vehicle.registration_number
            colour = slot_obj.vehicle.colour
            logger.debug('{}           {}      {}'.format(slot, registration_num, colour))
            print('{}           {}      {}'.format(slot, registration_num, colour))
        return

    def __str__(self):
        output = 'SlotMap \n'
        for key in self.slot_map:
            output += str(key) + ':' + str(self.slot_map[key]) + '\n'
        return output


if __name__ == '__main__':
    log_handler = logging.FileHandler('parkingLot.log')
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)
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
    sm = SlotMap()
    sm.insert(s4)
    sm.insert(s2)
    sm.insert(s5)
    sm.insert(s3)
    sm.insert(s1)
    logger.debug(sm)
    logger.debug('REMOVING SLOT 3')
    sm.delete(3)
    logger.debug(sm)
    logger.debug('GET SLOT NUMBER 10 {}'.format(sm.get_slot_object(10)))
    logger.debug('GET SLOT NUMBER 2 {}'.format(sm.get_slot_object(2)))
    logger.debug('REMOVING SLOT 5')
    sm.delete(5)
    logger.debug(sm)
    logger.debug('REMOVING SLOT 2')
    sm.delete(2)
    logger.debug(sm)
    logger.debug('REMOVING SLOT 1')
    sm.delete(1)
    logger.debug(sm)
    logger.debug('REMOVING SLOT 4')
    sm.delete(4)
    logger.debug(sm)
