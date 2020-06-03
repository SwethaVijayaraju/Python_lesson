# 5. Create a class called Robot which takes an initial position x,y coordinate.
# Add method up, down, left, right which moves the robot in that direction by 1 unit.
# Add a method called position which returns the current position of the robot
# e.g; r = Robot((0,0)); r.up(); r.position() # (0,1);
# r.down(); r.position() # (0,0)

# 5b. Add another method called distance which returns the total distance travelled by the robot since the beginning
# r.distance() # 2 because it moved up once and down once. even though the starting and current position are same.

# 5c. As an extension to the question 5. Take another input parameter called fuel which creating the robot r = Robot(
# (0,0), 10) The robot can only move if it has fuel left. Assume 1/2 unit of fuel is consumed for every other
# movement r.up() r.up() now fuel is 9 since the robot has moved twice. When up()(or any movement) is called 20
# times, it can not move any further, so calling up 21th time will not do anything ; r.up() # called 20 or more times
# r.position() # will always be (0,20)

# 5d. Add a method called movements which takes a destination coordinate returns a list of movements to be performed
# by the robot to reach there. Return empty list if the robot can not reach that destination(fuel not sufficient)
# r = Robot((0,0), 10)
# r.movements((1,5)) # returns [right, up, up, up, up, up]
# there can be many ways to reach that destination(e.g [up, right, up, up, up, up]), just return any valid sequence
# r.movements((1,100)) # returns [], since with fuel 10, the robot can not reach that destination.
# (0,8) to (1,5) ans=[right,down,down,down]
# dis_hor= -ve, then des>source; dis_hor= +ve, then des<source
# dis_ver= -ve, then des>source; dis_ver= +ve, then des<source

class Robot:

    def __init__(self, xcoor, ycoor, fuel):
        self.x = xcoor
        self.y = ycoor
        self.f = fuel
        self.dis = 0

    def up(self):
        if self.f > 0:
            self.y = self.y + 1
            self.dis = self.dis + 1
            self.f = self.f - 0.5

    def down(self):
        if self.f > 0:
            self.y = self.y - 1
            self.dis = self.dis + 1
            self.f = self.f - 0.5

    def right(self):
        if self.f > 0:
            self.x = self.x + 1
            self.dis = self.dis + 1
            self.f = self.f - 0.5

    def left(self):
        if self.f > 0:
            self.x = self.x - 1
            self.dis = self.dis + 1
            self.f = self.f - 0.5

    def position(self):

        return self.x, self.y

    def distance(self):

        return self.dis

    def fuel(self):

        return self.f

    def movements(self, des_x, des_y):
        move = []

        dis_ver = self.y - des_y
        dis_hor = self.x - des_x

        if dis_hor < 0:
            mod_hor = dis_hor * -1
        else:
            mod_hor = dis_hor

        if dis_ver < 0:
            mod_ver = dis_ver * -1
        else:
            mod_ver = dis_ver

        fuel_req = (mod_ver + mod_hor) / 2

        if self.f >= fuel_req:

            self.x = des_x
            self.y = des_y
            self.f = self.f - fuel_req
            self.dis = self.dis + mod_hor + mod_ver

            if dis_hor < 0:
                while mod_hor > 0:
                    move.append("right")
                    mod_hor = mod_hor - 1

            elif dis_hor > 0:
                while mod_hor > 0:
                    move.append("left")
                    mod_hor = mod_hor - 1

            if dis_ver < 0:
                while mod_ver > 0:
                    move.append("up")
                    mod_ver = mod_ver - 1

            elif dis_ver > 0:
                while mod_ver > 0:
                    move.append("down")
                    mod_ver = mod_ver - 1

        return move


r = Robot(0, 0, 20)
r.up()
print(r.position())
r.down()
print(r.position())
print(r.distance())
r.right()
print(r.position())
r.left()
print(r.position())
print(r.distance())
print(r.fuel())
r.up()
r.up()
print(r.position())
print(r.distance())
print(r.fuel())
print(r.movements(1, 5))
print(r.movements(-1, 9))
print(r.movements(0, 0))
print(r.movements(1, 100))
print(r.position())
print(r.distance())
print(r.fuel())
