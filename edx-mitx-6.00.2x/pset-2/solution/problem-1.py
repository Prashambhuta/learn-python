import math
import random
import pylab

from ps2_verify_movement37 import testRobotMovement


class Position(object):
    """
    A representation of location in two dimensional space.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        """
        After each tick the position of the robot changes in accordance with
        the angle and the speed.

        angle:// float value between 0 & 360.
        speed:// any float value

        Returns:// a position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        new_x = old_x + speed * (math.sin(math.radians(angle)))
        new_y = old_y + speed * (math.cos(math.radians(angle)))
        return Position(new_x, new_y)

    def __str__(self):
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# Testing getNewPosition method
# robot_test = Position(0.0, 0.0)
# new_position = robot_test.getNewPosition(90, 2)
# print(new_position)

##### Problem 1 - RectangularRoom Class
class RectangularRoom(object):
    """
    Represents rectangular room with clean and dirty tiles.

    A room has width*height tiles, and at any movement of time the tile is
    either clean of dirty.
    for eg. the room with 2/3 has 6 tiles of 1x1. Visualise in the way of 2x3
    grid.
    """

    def __init__(self, width, height):
        """
        Initialise the room with particular width and height. Initially no
        tiles are cleaned.

        width:// int > 0
        height:// int > 0
        """
        self.width = width
        self.height = height
        # list to save clean tiles, might have to use dict or tuple. Let's see
        self.clean_tiles = []

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getCleanTiles(self):
        return self.clean_tiles

    def cleanTileAtPosition(self, pos):
        """
        Mark the current position (pos) as cleaned. given that the pos is
        inside the room.

        pos:// a Position
        """
        if pos.getX() > self.width or pos.getY() > self.height:
            raise ValueError("Position out of the room, cannot CLEAN!")
        else:
            x_cord = math.floor(pos.getX())
            y_cord = math.floor(pos.getY())
            if not self.isTileCleaned(x_cord, y_cord):
                self.clean_tiles.append(Position(x_cord, y_cord))

    def isTileCleaned(self, m, n):
        """
        Assuming tiles (m,n) lies in the RectangularRoom, returns True if
        tile(m,n) is cleaned.

        m:// int > 0, <= width of room.
        n:// int > 0, <= height of room

        returns:// TRUE if tile(m,n) is clean; FALSE otherwise
        """
        clean_tiles = self.getCleanTiles()
        for i in clean_tiles:
            if int(m) == i.getX() and int(n) == i.getY():
                return True
        else:
            return False


    def getNumTiles(self):
        """
        returns the total number of tiles in the room.

        returns:// width x height (an integer)
        """
        return self.getWidth()*self.getHeight()

    def getNumCleanedTiles(self):
        """
        returns the integer representing the number of clean tiles.

        returns:// an integer
        """
        return len(self.getCleanTiles())

    def getRandomPosition(self):
        """
        returns a random position inside the room.

        returns:// Position(m,n) such that m,n <= width, height
        """
        x_coord = round(random.uniform(0, self.getWidth()-0.01), 2)
        y_coord = round(random.uniform(0, self.getHeight()-0.01), 2)
        return Position(x_coord, y_coord)

    def isPositionInRoom(self, pos):
        """
        returns True if position is inside the room, False otherwise.

        @returns:// True if 'pos' inside the room, False otherwise.
        """
        x_coord = math.floor(pos.getX())
        y_coord = math.floor(pos.getY())
        if x_coord < 0 or y_coord < 0:
            return False
        if x_coord >= self.getWidth() or y_coord >= self.getHeight():
            return False
        else:
            return True

    # CODE TO CHECK THE LIST OF CLEAN TILES
    # def cleanTiles(self):
    #     return self.clean_tiles


class Robot(object):
    """
    Represents a robot inside a room, doing the cleaning.

    At all times the robot has a speed and direction, and it cleans the tile
    it is on at currently.

    This is an abstract class, and subclasses will have method for the movement.
    """
    def __init__(self, room, speed):
        """
        A robot is initialised inside the room, with particular speed. The
        position and direction are random.

        @arguments
        room:// A RectangularRoom object
        speed:// an float
        """
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = random.randint(0, 360)

    def getSpeed(self):
        return self.speed

    def getRoom(self):
        return self.room

    def getRobotPosition(self):
        """
        Returns the robot's position.

        @returns:// Position object with robot's position
        """
        return self.position

    def getRobotDirection(self):
        """
        Returns robot's direction.

        @returns:// Int between 0, to 360 degrees
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Sets the position of the robot to the new position.

        @parameters:
        @position:// A Position object.

        @returns:// nothing
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Sets the direction of the robot to the new value.

        @parameters:
        @direction:// a int between (0, 360)

        @returns:// nothing
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of single time unit.

        Move the object to the new tile, and mark the tile as having cleaned
        INSTANTLY!
        """
        raise NotImplementedError

# Problem 3 - STANDARD ROBOT
class StandardRobot(Robot):
    """
    StandardRobot is a standard robot that moves in the direction given,
    and if it hits a wall, it will randomly choose new direction.
    """

    def updatePositionAndClean(self):
        """
        Update the position of the robot after the given time-step, and clean
        the tile it lands on.
        """
        current_position = self.getRobotPosition()
        current_direction = self.getRobotDirection()
        speed = self.getSpeed()
        room = self.getRoom()
        # cleaning current position
        position = current_position.getNewPosition(current_direction,
                                                        speed)
        # new_position = self.getRobotPosition()
        # print(new_position)
        if room.isPositionInRoom(position):
            self.setRobotPosition(position)
            room.cleanTileAtPosition(position)
        else:
            self.direction = random.randint(0, 360)

# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    time_taken = 0
    for t in range(num_trials):
        # initialising the room
        room = RectangularRoom(width, height)
        # initialising the robot
        robots = [robot_type(room, speed) for x in range(num_robots)]
        t_trial = 0
        while room.getNumCleanedTiles()/room.getNumTiles() < min_coverage:
            for rob in robots:
                rob.updatePositionAndClean()
            t_trial += 1
        # print(t_trial)
        time_taken += t_trial
    return time_taken/num_trials

# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        current_position = self.getRobotPosition()
        # current_direction = self.getRobotDirection()
        speed = self.getSpeed()
        room = self.getRoom()
        # cleaning current position
        position = current_position.getNewPosition(random.randint(0, 360),
                                                        speed)
        # new_position = self.getRobotPosition()
        # print(new_position)
        if room.isPositionInRoom(position):
            self.setRobotPosition(position)
            room.cleanTileAtPosition(position)
            self.direction = random.randint(0, 360)
        else:
            self.direction = random.randint(0, 360)



# -----------------------------------------------------------------------
# TESTING CODES HERE | DEBUGGING | TRIALS | ETC
# Testing cleanTileAtPosition
room_test = RectangularRoom(30, 20)
# robot_test = Position(0.0, 0.0)
robot_test = StandardRobot(room_test, 2)
robot_test.setRobotPosition(Position(2, 2))
robot_test.setRobotDirection(45)
# new_position = robot_test.getNewPosition(90, 3.0)
print(robot_test.updatePositionAndClean())
# for tiles in room_test.clean_tiles:
#     print

# Testing for isTileClean:
# print(room_test.isTileCleaned(3, 0))

print(runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot))

