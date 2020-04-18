import logging

logger = logging.getLogger('ParkingLot')
from heap import Heap
from slotmap import SlotMap
from vehiclecolourmap import VehicleColourMap
from vehicle import Vehicle
from slot import Slot


class ParkingLot:
    cmds = {'park', 'leave', 'status', 'registration_numbers_for_cars_with_colour', 'slot_numbers_for_cars_with_colour',
            'slot_number_for_registration_number'}

    def __init__(self, total_slots):

        self.num_cmds = 0
        self.total_slots = total_slots
        self.free_slots_heap = Heap()
        self.total_occupied_slots = 0
        self.occupied_slot_map = SlotMap()
        self.vehicle_colour_map = VehicleColourMap()
        logger.debug('Created a parking lot with {} slots'.format(total_slots))
        print('Created a parking lot with {} slots'.format(total_slots))

    def execute(self, command):
        if len(command) == 0:
            logger.debug('Empty command: Executing nothing')
            return
        self.num_cmds += 1
        self.command_handler(command)
        return

    def command_handler(self, cmd):
        cmd_list = cmd.split()
        operation = cmd_list[0]
        if operation in self.cmds:
            return getattr(self, operation)(cmd)
        else:
            logger.debug('Operation not found for cmd {}'.format(cmd))
            print('Operation not found for cmd {}'.format(cmd))

    def __find_free_slot(self):
        if self.total_occupied_slots == self.total_slots:
            return None
        slot = self.free_slots_heap.get()
        logger.debug('Slot obtained from min heap {}'.format(slot))
        if slot is None:
            slot = self.total_occupied_slots + 1
            logger.debug('Getting free slot from incrementing the total occupied slots {}'.format(slot))
        return slot

    def park(self, cmd):
        cmd_list = cmd.split()
        registration_number = cmd_list[1]
        colour = cmd_list[2]
        logger.debug('park command: {} registration number {} colour {}'.format(cmd, registration_number, colour))
        slot = self.__find_free_slot()
        if slot is None:
            logger.debug('Sorry, parking lot is full')
            print('Sorry, parking lot is full')
            return

        vehicle_obj = Vehicle(registration_number, colour)
        slot_obj = Slot(slot, vehicle_obj)
        self.occupied_slot_map.insert(slot_obj)
        self.vehicle_colour_map.insert(slot_obj)
        self.total_occupied_slots += 1

        logger.debug('Free Slots heap \n {}'.format(self.free_slots_heap))
        logger.debug('Occupied Slot Map \n {}'.format(self.occupied_slot_map))
        logger.debug('Vehicle Colour Map \n {}'.format(self.vehicle_colour_map))
        logger.debug('Total occupied slots {}'.format(self.total_occupied_slots))
        logger.debug('Allocated slot number: {}'.format(slot))
        print('Allocated slot number: {}'.format(slot))
        return

    def leave(self, cmd):
        cmd_list = cmd.split()
        slot = int(cmd_list[1])

        logger.debug('leave command: {}: slot {}'.format(cmd, slot))
        if slot > self.total_slots or slot <= 0:
            logger.debug('Sorry, Invalid slot {}: Slot should be less than Total parking slots {}'.format(slot,
                                                                                                          self.total_slots))
            print('Sorry, Invalid slot {}: Slot should be between 1 and Total parking slots {}'.format(slot,
                                                                                                   self.total_slots))
            return

        slot_obj = self.occupied_slot_map.get_slot_object(slot)
        if slot_obj is None:
            print('Slot number {} is free'.format(slot))
            logger.debug('Slot number {} is free'.format(slot))
            logger.debug('Sorry, No Vehicle is parked at slot {}'.format(slot))
            return
        self.occupied_slot_map.delete(slot)
        self.vehicle_colour_map.delete(slot_obj)
        self.total_occupied_slots -= 1
        self.free_slots_heap.insert(slot)

        logger.debug('Free Slots heap \n {}'.format(self.free_slots_heap))
        logger.debug('Occupied Slot Map \n {}'.format(self.occupied_slot_map))
        logger.debug('Vehicle Colour Map \n {}'.format(self.vehicle_colour_map))
        logger.debug('Total occupied slots {}'.format(self.total_occupied_slots))

        logger.debug('Slot number {} is free'.format(slot))
        print('Slot number {} is free'.format(slot))
        return

    def status(self, cmd):
        logger.debug('status command: {}'.format(cmd))
        self.occupied_slot_map.display_status()

    def registration_numbers_for_cars_with_colour(self, cmd):
        cmd_list = cmd.split()
        colour = cmd_list[1]
        logger.debug('registration_numbers_for_cars_with_colour command: {} colour'.format(cmd, colour))
        slot_set = self.vehicle_colour_map.get_set_of_slots(colour)
        sorted_list = sorted(slot_set)
        logger.debug('Slot with {} colour {}'.format(colour, sorted_list))
        if len(sorted_list) == 0:
            print(' ')
            return
        first_slot = sorted_list[0]
        slot_obj = self.occupied_slot_map.get_slot_object(first_slot)
        output_string = slot_obj.vehicle.registration_number
        for slot in sorted_list[1:]:
            slot_obj = self.occupied_slot_map.get_slot_object(slot)
            output_string += ', {}'.format(slot_obj.vehicle.registration_number)
        logger.debug(output_string)
        print(output_string)
        return

    def slot_numbers_for_cars_with_colour(self, cmd):
        cmd_list = cmd.split()
        colour = cmd_list[1]
        logger.debug('slot_numbers_for_cars_with_colour command: {} colour'.format(cmd, colour))
        slot_set = self.vehicle_colour_map.get_set_of_slots(colour)
        sorted_list = sorted(slot_set)
        logger.debug('Slot with {} colour {}'.format(colour, sorted_list))
        if len(sorted_list) == 0:
            print(' ')
            return
        first_slot = sorted_list[0]
        output_string = '{}'.format(first_slot)
        for slot in sorted_list[1:]:
            output_string += ', {}'.format(slot)
        print(output_string)
        logger.debug(output_string)
        return

    def slot_number_for_registration_number(self, cmd):
        cmd_list = cmd.split()
        registration_number = cmd_list[1]

        logger.debug(
            'slot_number_for_registration_number  command: {} registration number'.format(cmd, registration_number))
        slot = self.vehicle_colour_map.get_slot(registration_number)
        if slot is None:
            logger.debug('Not Found: Registration Number : {}'.format(registration_number))
            logger.debug('Not found')
            print('Not found')
            return
        logger.debug('Slot Number: {} for Registration Number: {}'.format(slot, registration_number))
        logger.debug('{}'.format(slot))
        print('{}'.format(slot))
