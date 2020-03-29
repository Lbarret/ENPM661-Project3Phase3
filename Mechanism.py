from math import sqrt, cos, sin, radians, atan2, floor


class Node:
    # Initialize
    def __init__(self, start, env, goal, stepSize, parent=None):
        self.env = env
        self.parent = parent
        self.goal = goal
        if parent is not None:
            self.g = parent.g + stepSize
        else:
            self.g = 0
        # Heuristic function
        self.weight = self.g + sqrt((env[0] - goal[0]) ** 2 + (env[1] - goal[1]) ** 2) + (
                    (env[2] - floor(atan2((goal[1] - start[1]), (goal[0] - start[0])))) / 30) * (stepSize / 5)

    # Solve for path from goal to start node
    def path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    # Get possible actions
    def actions(self):
        if self.action is None:
            return self.env.possibleMoves()
        else:
            return self.env.possibleMoves(self.action)


class Environment:
    # Initialize
    def __init__(self, currentPosition, clearance):
        self.currentPosition = currentPosition
        self.clearance = clearance

     # Check if node is in center cirlce
    def insideCircle1(self, position):
        if (position[0] - 5.1) ** 2 + (position[1] - 5.1) ** 2 <= (2 + self.clearance) ** 2:
            return True
        else:
            return False


    # Check if node is in bottom left cirlce
    def insideCircle2(self, position):
        if (position[0] - 3.1) ** 2 + (position[1] - 2.1) ** 2 <= (2 + self.clearance) ** 2:
            return True
        else:
            return False

    # Check if node is in bottom right cirlce
    def insideCircle3(self, position):
        if (position[0] - 7.1) ** 2 + (position[1] - 2.1) ** 2 <= (2 + self.clearance) ** 2:
            return True
        else:
            return False

    # Check if node is in top right cirlce
    def insideCircle4(self, position):
        if (position[0] - 7.1) ** 2 + (position[1] - 8.1) ** 2 <= (2 + self.clearance) ** 2:
            return True
        else:
            return False

    # Check if node is in top left square using half planes
    def insideSquare1(self, position):
        if position[0] > 2.35 - self.clearance and position[0] < 3.85 + self.clearance and position[1] < 8.85 + self.clearance and position[1] > 7.35 - self.clearance:
            return True
        else:
            return False

    # Check if node is in middle left square using half planes
    def insideSquare2(self, position):
       if position[0] > .35 - self.clearance and position[0] < 1.85 + self.clearance and position[1] < 5.85 + self.clearance and position[1] > 4.35 - self.clearance:
           return True
       else:
           return False

    # Check if node is in middle right square using half planes
    def insideSquare3(self, position):
       if position[0] > 8.35 - self.clearance and position[0] < 9.85 + self.clearance and position[1] < 5.85 + self.clearance and position[1] > 4.35 - self.clearance:
           return True
       else:
           return False

     # Check if node is outside of map using half planes
    def outsideMap(self, position):
       if position[0] < .1 + self.clearance or position[0] > 10.1 - self.clearance or position[1] > 10.1 - self.clearance or position[1] < .1 + self.clearance:
           return True
       else:
           return False

    # Check if position is inside map or inside an object
    def possiblePostion(self, position):
        possiblity = True
        if self.insideCircle1(position):
            possiblity = False
        if self.insideCircle2(position):
            possiblity = False
        if self.insideCircle3(position):
            possiblity = False
        if self.insideCircle4(position):
            possiblity = False
        if self.insideSquare1(position):
            possiblity = False
        if self.insideSquare2(position):
            possiblity = False
        if self.insideSquare3(position):
            possiblity = False
        if self.outsideMap(position):
            possiblity = False
        return possiblity

    # Check if each action is possible
    def possibleMoves(self, start, node, stepSize):
        actions = []
        temp = self.move(start, '1', stepSize, node)
        if temp is not None:
            actions.append(temp)
        temp = self.move(start, '2', stepSize, node)
        if temp is not None:
            actions.append(temp)
        temp = self.move(start, '3', stepSize, node)
        if temp is not None:
            actions.append(temp)
        temp = self.move(start, '4', stepSize, node)
        if temp is not None:
            actions.append(temp)
        temp = self.move(start, '5', stepSize, node)
        if temp is not None:
            actions.append(temp)
        return actions

    # Move robot position according to action
    def move(self, start, val, stepSize, node):
        temp = None
        if val == '1':
            angle = self.currentPosition[2] + 60
            angle = self.angleCheck(angle)
            tempBoolean = True
            for i in range(stepSize):
                x = self.currentPosition[0] + i * cos(radians(angle))
                y = self.currentPosition[1] + i * sin(radians(angle))
                if not self.possiblePostion([x, y]):
                    tempBoolean = False
            if tempBoolean:
                x = self.currentPosition[0] + stepSize * cos(radians(angle))
                y = self.currentPosition[1] + stepSize * sin(radians(angle))
                temp = Node(start, [x, y, angle], node.goal, stepSize, node)
        if val == '2':
            angle = self.currentPosition[2] + 30
            angle = self.angleCheck(angle)
            tempBoolean = True
            for i in range(stepSize):
                x = self.currentPosition[0] + i * cos(radians(angle))
                y = self.currentPosition[1] + i * sin(radians(angle))
                if not self.possiblePostion([x, y]):
                    tempBoolean = False
            if tempBoolean:
                x = self.currentPosition[0] + stepSize * cos(radians(angle))
                y = self.currentPosition[1] + stepSize * sin(radians(angle))
                temp = Node(start, [x, y, angle], node.goal, stepSize, node)
        if val == '3':
            angle = self.currentPosition[2]
            angle = self.angleCheck(angle)
            tempBoolean = True
            for i in range(stepSize):
                x = self.currentPosition[0] + i * cos(radians(angle))
                y = self.currentPosition[1] + i * sin(radians(angle))
                if not self.possiblePostion([x, y]):
                    tempBoolean = False
            if tempBoolean:
                x = self.currentPosition[0] + stepSize * cos(radians(angle))
                y = self.currentPosition[1] + stepSize * sin(radians(angle))
                temp = Node(start, [x, y, angle], node.goal, stepSize, node)
        if val == '4':
            angle = self.currentPosition[2] - 30
            angle = self.angleCheck(angle)
            tempBoolean = True
            for i in range(stepSize):
                x = self.currentPosition[0] + i * cos(radians(angle))
                y = self.currentPosition[1] + i * sin(radians(angle))
                if not self.possiblePostion([x, y]):
                    tempBoolean = False
            if tempBoolean:
                x = self.currentPosition[0] + stepSize * cos(radians(angle))
                y = self.currentPosition[1] + stepSize * sin(radians(angle))
                temp = Node(start, [x, y, angle], node.goal, stepSize, node)
        if val == '5':
            angle = self.currentPosition[2] - 60
            angle = self.angleCheck(angle)
            tempBoolean = True
            for i in range(stepSize):
                x = self.currentPosition[0] + i * cos(radians(angle))
                y = self.currentPosition[1] + i * sin(radians(angle))
                if not self.possiblePostion([x, y]):
                    tempBoolean = False
            if tempBoolean:
                x = self.currentPosition[0] + stepSize * cos(radians(angle))
                y = self.currentPosition[1] + stepSize * sin(radians(angle))
                temp = Node(start, [x, y, angle], node.goal, stepSize, node)
        return temp

    # Keep angle value from 0 to 360
    def angleCheck(self, angle):
        if angle >= 360:
            angle -= 360
        if angle < 0:
            angle = 360 + angle
        return angle
