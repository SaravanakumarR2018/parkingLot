import logging
import sys

from parkinglot import ParkingLot

logger = logging.getLogger('ParkingLot')
LOG_FORMAT = '%(asctime)s  - %(levelname)s - [%(filename)s:%(funcName)s:%(lineno)d] (%(threadName)s) %(message)s'
log_handler = logging.FileHandler('parkingLot.log')
formatter = logging.Formatter(LOG_FORMAT)
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)


class MainExecutor:
    def __init__(self):
        self.create_parking_lot_cmd = 'create_parking_lot'
        self.parking_lot_initialized = False
        if len(sys.argv) == 2:
            # Contains the file to be parsed
            file = sys.argv[1]
            logger.debug('FILE INPUT {}'.format(file))
            self.__parse_file(file)
        else:
            logger.debug('STDIN INPUT')
            self.__get_inputs_from_stdin()

    def __parse_file(self, file):
        try:
            fs = open(file, 'r')
        except Exception as e:
            logger.error('Unable to open file {}'.format(file))
            return
        lines = fs.readlines()
        for cmd in lines:
            self.__execute(cmd)
        logger.debug('Parsed file {}: Exiting the process'.format(file))
        return

    def __execute(self, cmd):
        cmd = cmd.strip()
        if not self.parking_lot_initialized:
            cmd_list = cmd.split()
            if cmd_list[0] == self.create_parking_lot_cmd:
                self.parking_lot = ParkingLot(int(cmd_list[1]))
                self.parking_lot_initialized = True
                logger.debug('Parking lot initialized with slots {}'.format(cmd_list[1]))
                return
            logger.debug('Command seen before initializing Parking lot: {}'.format(cmd))
        else:
            self.parking_lot.execute(cmd)

    def __get_inputs_from_stdin(self):
        while True:
            cmd = sys.stdin.readline()
            cmd = cmd.strip()
            if 'exit' == cmd.lower():
                logger.debug('Obtained Exit from input: Exiting the process')
                return
            self.__execute(cmd)


MainExecutor()
