from enum import Enum


class Point(Enum):
    """
    An enum to define the supported point types
    """
    good = 1
    excellent = 2
    need_improvement = 3
    naughty = 4


class Ladder(object):
    """
    A point tracking system that implements a ladder where points are collected and stores in-order
    max_points: The maximum number of points supported in this ladder
    """
    def __init__(self, max_points=10):
        self.max_points = max_points
        self.ladder = list()

    def __str__(self):
        output = '|'
        if len(self.ladder) == 0:
            output =  '\tEMPTY\t|'
        else:
            for point in self.ladder:
                output += '\t{}\t|'.format(point.name)
        return output

    def add_point(self, point):
        """
        Add a point to the ladder
        """
        # if not isinstance(point, Point):
        #     raise Exception("Cannot add an item that isn't of support type 'Point'")
        
        if len(self.ladder) >= self.max_points:
            raise Exception("The maximum number of points ({}) for this ladder has been reached".format(self.max_points))

        self.ladder.append(point)

    def reset(self):
        """
        Reset this ladder to contain no points
        """
        self.ladder = list()