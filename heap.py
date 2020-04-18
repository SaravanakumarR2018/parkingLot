import logging

logger = logging.getLogger('ParkingLot')


class Heap:
    def __init__(self):
        self.heap_arr = []

    def __str__(self):
        return str(self.heap_arr)

    def insert(self, value):
        self.heap_arr.append(value)
        if len(self.heap_arr) == 1:
            return
        current_index = len(self.heap_arr) - 1
        parent_index = int((current_index - 1) / 2)
        while parent_index >= 0:
            if self.heap_arr[parent_index] > self.heap_arr[current_index]:
                temp = self.heap_arr[parent_index]
                self.heap_arr[parent_index] = self.heap_arr[current_index]
                self.heap_arr[current_index] = temp
                current_index = parent_index
                parent_index = int((current_index - 1) / 2)
            else:
                break

    def get(self):
        if len(self.heap_arr) == 0:
            return None
        if len(self.heap_arr) == 1:
            temp = self.heap_arr[0]
            self.heap_arr.pop()
            return temp

        ret_val = self.heap_arr[0]
        last_index = len(self.heap_arr) - 1

        # copy last element with first element
        self.heap_arr[0] = self.heap_arr[last_index]

        # pop the last element
        self.heap_arr.pop(last_index)
        last_index = len(self.heap_arr) - 1
        node_index = 0
        while True:
            left = node_index * 2 + 1
            right = node_index * 2 + 2
            smallest = node_index
            if left <= last_index:
                if self.heap_arr[left] < self.heap_arr[smallest]:
                    smallest = left
            if right <= last_index:
                if self.heap_arr[right] < self.heap_arr[smallest]:
                    smallest = right
            if smallest == node_index:
                break;
            else:
                temp = self.heap_arr[node_index]
                self.heap_arr[node_index] = self.heap_arr[smallest]
                self.heap_arr[smallest] = temp
                node_index = smallest
        return ret_val

    def show(self):
        logger.debug('Elements {}'.format(self.heap_arr))


if __name__ == '__main__':
    log_handler = logging.FileHandler('parkingLot.log')
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)
    myheap = Heap()
    myheap.insert(5)
    myheap.show()
    myheap.insert(10)
    myheap.show()
    myheap.insert(100)
    myheap.show()
    myheap.insert(75)
    myheap.show()
    myheap.insert(2)
    myheap.show()
    myheap.insert(7)
    myheap.show()
    logger.debug('Sorted Elements ')
    while True:
        temp = myheap.get()
        if temp is not None:
            logger.debug('{} '.format(temp))
        else:
            break
    myheap.insert(3)
    myheap.show()
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    myheap.insert(1000)
    myheap.insert(500)
    myheap.show()
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    myheap.insert(500)
    myheap.insert(1000)
    myheap.show()
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    myheap.insert(5)
    myheap.insert(15)
    myheap.insert(10)
    myheap.show()
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    myheap.insert(5)
    myheap.insert(10)
    myheap.insert(15)
    myheap.show()
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    myheap.insert(10)
    myheap.insert(5)
    myheap.insert(15)
    myheap.show()
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    myheap.insert(10)
    myheap.insert(15)
    myheap.insert(5)
    myheap.show()
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    myheap.insert(15)
    myheap.insert(10)
    myheap.insert(5)
    myheap.show()
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    myheap.insert(15)
    myheap.insert(5)
    myheap.insert(10)
    myheap.show()
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
    logger.debug('Get heap {}'.format(myheap.get()))
