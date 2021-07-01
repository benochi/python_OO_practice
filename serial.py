"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Make new generator, set starting value"""
        self.start = self.next = start

    def __repr__():
        "Representation of class"
        return f"<SerialGenerator> {start} {nxt}"
    
    def generate(self):
        "Return next serial by incrementing"
        self.next += 1
        return self.next - 1
    
    def reset(self):
        """resets start value to original start value"""
        self.next = self.start

    
