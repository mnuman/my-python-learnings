"""Functions for Advent of Code 2017, day 13"""
import os


class Layer():
    """Layer objects for the firewall"""

    def __init__(self, depth):
        """Initialize a new layer object, containing pos(ition), depth and move offset
           attributes.
        """
        self.depth = depth
        if depth is not None and depth > 0:
            self.pos = 0
            self.offset = 1
        else:
            self.pos = None
            self.offset = None

    def move(self):
        """ Current position determines the move direction, this is evaluated just
           before the move is executed.
        """
        if self.pos is not None:
            if self.pos == 0:
                self.offset = 1
            elif self.pos == self.depth - 1:
                self.offset = -1
            self.pos += self.offset


class Firewall():
    """ Classs representation of the firewall; the class
        need to be passed an array of Layer object on creation
        and exposes the required move_scanner, move_packet and 
        the operation combining the two, cycle.
        The score is exposed as packet score attribute.
        TO DO: have not taken any precaution to hide attributes
          and/or methods! Caveat emptor ...
    """

    def __init__(self, layers):
        self.layers = layers
        self.packet_position = -1  # still outside firewall
        self.packet_score = 0

    def move_scanners(self):
        """Move all scanners one step"""
        for layer in self.layers:
            layer.move()

    def move_packet(self):
        """Simply move the packet ahead in the firewall ... or outside of if :-) """
        self.packet_position += 1

    def cycle(self):
        """Move packet and if still in firewall,
           determine it has moved onto a scanner.
           If so, increment the score, then move all 
           scanners.
        """
        self.move_packet()
        if self.packet_position < len(self.layers):
            if self.layers[self.packet_position].pos == 0:
                # caught!
                self.packet_score += self.packet_position * \
                    self.layers[self.packet_position].depth
        self.move_scanners()


def read_configuration(filename):
    """Parse configuration file and return a Firewall
       object containing the problem domain, a firewall
       having multiple layers with scanners.
    """
    with open(filename) as f:  # pylint: disable=C0103
        content = f.readlines()
    firewall = []
    for line in content:
        elements = line.split(':')
        pos = int(elements[0].strip())
        depth = int(elements[1].strip())
        while pos > len(firewall):
            firewall.append(Layer(None))
        firewall.append(Layer(depth))
    return Firewall(firewall)


if __name__ == '__main__':
    myfirewall = read_configuration(os.path.join(
        os.path.dirname(__file__), 'day13_input.txt'))
    while myfirewall.packet_position < len(myfirewall.layers):
        myfirewall.cycle()
    print(f"The final score is {myfirewall.packet_score}")
# part1 solution = 1624
