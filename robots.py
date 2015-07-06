# Assumptions:
# Input 4th line is blank and from then on every third is blank.

import sys

# Scents
scents = []

# Limits
limitX = 0
limitY = 0

# Robot class
class Robot:

    # Is the robot lost?
    is_lost = False

    # Initializer
    def __init__(self, xCoordinate, yCoordinate, orientation):
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.orientation = orientation

    # Move method
    def move(self):
        # Moves only if it's safe and it is not lost
        if self.is_safe() and not self.is_lost:
            if(self.orientation == 'N'):
                self.yCoordinate += 1
            elif (self.orientation == 'S'):
                self.yCoordinate -= 1
            elif (self.orientation == 'E'):
                self.xCoordinate += 1
            elif (self.orientation == 'W'):
                self.xCoordinate -= 1
        # If the move is unsafe check if there's a scent, if not then he is lost
        elif not self.is_scent():
            self.is_lost = True
            scents.append((self.xCoordinate,self.yCoordinate))


    # Orientation rotator method
    def rotate(self, direction):
        if direction == 'L':
            if self.orientation == 'N':
                self.orientation = 'W'
            elif self.orientation == 'S':
                self.orientation = 'E'
            elif self.orientation == 'E':
                self.orientation = 'N'
            elif self.orientation == 'W':
                self.orientation = 'S'
        elif direction == 'R':
            if self.orientation == 'N':
                self.orientation = 'E'
            elif self.orientation == 'S':
                self.orientation = 'W'
            elif self.orientation == 'E':
                self.orientation = 'S'
            elif self.orientation == 'W':
                self.orientation = 'N'

    # Check if move is safe
    def is_safe(self):
        # print "Calling is_safe with orientation " + self.orientation
        if self.orientation == 'W':
            if self.xCoordinate - 1 < 0:
                return False
        if self.orientation == 'E':
            if self.xCoordinate + 1 > limitX:
                return False
        if self.orientation == 'S':
            if self.yCoordinate - 1 < 0:
                return False
        if self.orientation == 'N':
            if self.yCoordinate + 1 > limitY:
                return False
        # print "This is safe"
        return True

    # Checks if location has scent
    def is_scent(self):
        # print "Looking for " + str(self.xCoordinate) + " " + str(self.yCoordinate) + " in " + str(scents)
        if (self.xCoordinate, self.yCoordinate) in scents:
            # print True
            return True
        else:
            # print False
            return False

    # Makes a string of robot's status
    def toString(self):
        string = str(self.xCoordinate) + " " + str(self.yCoordinate) + " " + str(self.orientation) + "\n"
        if self.is_lost:
            string = str(self.xCoordinate) + " " + str(self.yCoordinate) + " " + str(self.orientation) + " LOST \n"
        return string

    # Debugging methods
    def print_coordinate(self):
        print "Current coordinates are now: " + str(self.xCoordinate) + " " + str(self.yCoordinate)
    def print_orientation(self):
        print "Current orientation is now: " + self.orientation

# The program starts here

# Read the argument from terminal
name_of_file = sys.argv[1] + ".txt"
name_of_output = sys.argv[1] + "_output.txt"

# Opens the file and saves the lines in a list
try:
    f = open(name_of_file, 'r')
    commands = f.readlines()
    f.close()
except IOError:
    print "There is no such file"
    sys.exit()

# print commands

# The size of the grid is taken from the first line
limitX = int(commands[0][0])
limitY = int(commands[0][2])

# Open the writer
f = open(name_of_output,'w')

# This loop traverses the rest of the lines and parses the instructions
counter = 0
for i in range(1,len(commands)):
    # Create a robot
    if counter == 0:
        robot = Robot(int(commands[i][0]),int(commands[i][2]),commands[i][4])
        # print "This robot has been created " + robot.toString()
    # Operate robot
    elif counter == 1:
        for char in commands[i]:
            print char,
            if char == 'F':
                # print "I'm moving"
                robot.move()
            else:
                # print "I'm rotating"
                robot.rotate(char)
        f.write(robot.toString())
    # Empty line
    elif counter == 2:
        counter = -1
    counter += 1

# Close writer
f.close()

# Signal success
print("The results have been saved in a file named " + name_of_output)
