class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass

# It is best to picture the circular buffet as a clock where the hands
# move forward to write and move backward to read and to overwrite
# Maintaining a property to called head will tell you which index corresponds
# to your 12:00


class CircularBuffer:

    def __init__(self, size):
        # size lets you know how many slots to create in your circular buffer
        # You can detect if a buffer is full when all slots have been filled
        self.size = size
        self.head = 0
        self.values = [None for i in range(size)]

    def write(self, element):
        # Write the element to the next empty slot
        # and move the head to the next empty one
        # if the head points to a position outside the given slots
        # then the buffer is full and an exception can be raised.
        if self.head == self.size:
            raise BufferFullException
        self.values[self.head] = element
        self.head += 1

    def read(self):
        # read the element the oldest element in the buffer
        # which would be the element in the first position
        # reading removes the oldest element and adds an empty
        # slot unto the stack
        if self.head == 0:
            raise BufferEmptyException
        prev = self.head - 1
        self.head = prev if prev >= 0 else 0
        self.values.append(None)
        element = self.values.pop(0)
        return element

    def overwrite(self, element):
        # if the buffer is not really full overwrite must
        # behave like a normal write
        # else overwrite is equivalent to reading and then
        # writing an element unto the buffer
        if self.head == self.size:
            self.read()
        self.write(element)

    def clear(self):
        # Get back to how things were in the beginning
        self.__init__(self.size)
