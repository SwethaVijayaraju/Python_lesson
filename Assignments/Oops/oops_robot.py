import math


class Robot:

    def __init__(self, xcoor, ycoor, fuel):
        self.x = xcoor
        self.y = ycoor
        self.f = fuel
        self.fc = 0
        self.dis = 0

    def mileage(self):
        self.dis = self.dis + 1
        self.f = self.f - 0.5
        self.fc = self.fc + 0.5

    def up(self):
        if self.f > 0:
            self.y = self.y + 1
            self.mileage()

    def down(self):
        if self.f > 0:
            self.y = self.y - 1
            self.mileage()

    def right(self):
        if self.f > 0:
            self.x = self.x + 1
            self.mileage()

    def left(self):
        if self.f > 0:
            self.x = self.x - 1
            self.mileage()

    def position(self):
        return self.x, self.y

    def distance(self):
        return self.dis

    def fuel_left(self):
        return self.f

    def fuel_consumed(self):
        return self.fc

    def fuel_required(self, mod_hor, mod_ver):
        return (mod_ver + mod_hor) / 2

    def update_history(self, dis_ver, dis_hor, mod_hor, mod_ver, des_x, des_y, fuel_req):
        self.x = des_x
        self.y = des_y
        self.f = self.f - fuel_req
        self.fc = self.fc + fuel_req
        self.dis = self.dis + mod_hor + mod_ver

    @staticmethod
    def left_movement(mod_hor, route):
        while mod_hor > 0:
            route.append("left")
            mod_hor = mod_hor - 1

    @staticmethod
    def right_movement(mod_hor, route):
        while mod_hor > 0:
            route.append("right")
            mod_hor = mod_hor - 1

    @staticmethod
    def down_movement(mod_ver, route):
        while mod_ver > 0:
            route.append("down")
            mod_ver = mod_ver - 1

    @staticmethod
    def up_movement(mod_ver, route):
        while mod_ver > 0:
            route.append("up")
            mod_ver = mod_ver - 1

    def intersection_point(self, robot):
        if self.x == robot.x and self.y == robot.y:
            return "Robots are already at the intersection point"
        else:
            total_fuel = self.f + robot.f
            dis_hor = robot.x - self.x
            dis_ver = robot.y - self.y

            mod_hor = abs(dis_hor)
            mod_ver = abs(dis_ver)

            fuel_req = self.fuel_required(mod_hor, mod_ver)

            if total_fuel < fuel_req:
                return "Fuel not sufficient"

            else:
                mp_x = (self.x + robot.x) / 2
                mp_y = (self.y + robot.y) / 2
                mp_x1 = math.ceil(mp_x)
                mp_y1 = math.ceil(mp_y)
                mp_x2 = math.floor(mp_x)
                mp_y2 = math.floor(mp_y)

                inter_x = self.x
                inter_y = self.y

                mod_hor_mp1 = abs(mp_x1 - self.x)
                mod_ver_mp1 = abs(mp_y1 - self.y)
                fuel_req_mp1 = self.fuel_required(mod_hor_mp1, mod_ver_mp1)

                mod_hor_mp2 = abs(mp_x2 - self.x)
                mod_ver_mp2 = abs(mp_y2 - self.y)
                fuel_req_mp2 = self.fuel_required(mod_hor_mp2, mod_ver_mp2)

                if mp_x1 == mp_x2 and mp_y1 == mp_y2:  # both midpoints are the same.type(mp_x) = int and type(mp_y)
                    # = int
                    if self.f >= fuel_req_mp1 and robot.f >= fuel_req_mp1:
                        inter_x = mp_x
                        inter_y = mp_y
                        return inter_x, inter_y
                    elif self.f < fuel_req_mp1 <= robot.f:
                        steps_rob1 = self.f * 2

                        if self.x > robot.x:
                            inter_x = self.x - min(steps_rob1, mod_hor)
                            steps_rob1 = steps_rob1 - min(steps_rob1, mod_hor)
                            # (while steps_rob1 > 0 and mod_hor > 0:
                            # self.x = self.x - 1
                            # mod_hor = mod_hor - 1
                            # steps_rob1 = steps_rob1 - 1)
                        elif self.x < robot.x:
                            inter_x = self.x + min(steps_rob1, mod_hor)
                            steps_rob1 = steps_rob1 - min(steps_rob1, mod_hor)

                        if self.y > robot.y:
                            inter_y = self.y - min(steps_rob1, mod_ver)
                        elif self.y < robot.y:
                            inter_y = self.y + min(steps_rob1, mod_ver)

                        return inter_x, inter_y
                    elif self.f >= fuel_req_mp1 > robot.f:
                        steps_rob2 = robot.f * 2

                        if robot.x > self.x:
                            inter_x = robot.x - min(steps_rob2, mod_hor)
                            steps_rob2 = steps_rob2 - min(steps_rob2, mod_hor)
                        elif robot.x < self.x:
                            inter_x = robot.x + min(steps_rob2, mod_hor)
                            steps_rob2 = steps_rob2 - min(steps_rob2, mod_hor)

                        if robot.y > self.y:
                            inter_y = robot.y - min(steps_rob2, mod_ver)
                        elif robot.y < self.y:
                            inter_y = robot.y + min(steps_rob2, mod_ver)

                        return inter_x, inter_y
                elif mp_x1 != mp_x2 and mp_y1 != mp_y2:  # both midpoints are the different .type(mp_x) = float and
                    # type(mp_y) = float
                    if self.f >= fuel_req_mp1 and robot.f >= fuel_req_mp1:
                        inter_x = mp_x1
                        inter_y = mp_y1
                        return inter_x, inter_y
                    elif self.f < fuel_req_mp1 <= robot.f:
                        steps_rob1 = self.f * 2

                        if self.x > robot.x:
                            inter_x = self.x - min(steps_rob1, mod_hor)
                            steps_rob1 = steps_rob1 - min(steps_rob1, mod_hor)
                            # (while steps_rob1 > 0 and mod_hor > 0:
                            # self.x = self.x - 1
                            # mod_hor = mod_hor - 1
                            # steps_rob1 = steps_rob1 - 1)
                        elif self.x < robot.x:
                            inter_x = self.x + min(steps_rob1, mod_hor)
                            steps_rob1 = steps_rob1 - min(steps_rob1, mod_hor)

                        if self.y > robot.y:
                            inter_y = self.y - min(steps_rob1, mod_ver)
                        elif self.y < robot.y:
                            inter_y = self.y + min(steps_rob1, mod_ver)

                        return inter_x, inter_y
                    elif self.f >= fuel_req_mp1 > robot.f:
                        steps_rob2 = robot.f * 2

                        if robot.x > self.x:
                            inter_x = robot.x - min(steps_rob2, mod_hor)
                            steps_rob2 = steps_rob2 - min(steps_rob2, mod_hor)
                        elif robot.x < self.x:
                            inter_x = robot.x + min(steps_rob2, mod_hor)
                            steps_rob2 = steps_rob2 - min(steps_rob2, mod_hor)

                        if robot.y > self.y:
                            inter_y = robot.y - min(steps_rob2, mod_ver)
                        elif robot.y < self.y:
                            inter_y = robot.y + min(steps_rob2, mod_ver)

                        return inter_x, inter_y
                elif mp_x1 == mp_x2 and mp_y1 != mp_y2:  # both midpoints are the different .type(mp_x) = int and
                    # type(mp_y) = float

                    # Associated with just the 2 midpoints
                    if self.f >= fuel_req_mp1 and robot.f >= fuel_req_mp1:
                        inter_x = mp_x1
                        inter_y = mp_y1
                        return inter_x, inter_y
                    elif self.f >= fuel_req_mp1 and robot.f >= fuel_req_mp2:
                        inter_x = mp_x1
                        inter_y = mp_y1
                        return inter_x, inter_y
                    elif self.f >= fuel_req_mp2 and robot.f >= fuel_req_mp1:
                        inter_x = mp_x2
                        inter_y = mp_y2
                        return inter_x, inter_y

                        # Not associated with midpoints. IP allocated based on fuel sufficiency in both robots.
                    elif self.f < fuel_req_mp2 < fuel_req_mp1 <= robot.f:
                        steps_rob1 = self.f * 2

                        if self.x > robot.x:
                            inter_x = self.x - min(steps_rob1, mod_hor)
                            steps_rob1 = steps_rob1 - min(steps_rob1, mod_hor)
                            # (while steps_rob1 > 0 and mod_hor > 0:
                            # self.x = self.x - 1
                            # mod_hor = mod_hor - 1
                            # steps_rob1 = steps_rob1 - 1)
                        elif self.x < robot.x:
                            inter_x = self.x + min(steps_rob1, mod_hor)
                            steps_rob1 = steps_rob1 - min(steps_rob1, mod_hor)

                        if self.y > robot.y:
                            inter_y = self.y - min(steps_rob1, mod_ver)
                        elif self.y < robot.y:
                            inter_y = self.y + min(steps_rob1, mod_ver)

                        return inter_x, inter_y
                    elif self.f >= fuel_req_mp1 > fuel_req_mp2 > robot.f:
                        steps_rob2 = robot.f * 2

                        if robot.x > self.x:
                            inter_x = robot.x - min(steps_rob2, mod_hor)
                            steps_rob2 = steps_rob2 - min(steps_rob2, mod_hor)
                        elif robot.x < self.x:
                            inter_x = robot.x + min(steps_rob2, mod_hor)
                            steps_rob2 = steps_rob2 - min(steps_rob2, mod_hor)

                        if robot.y > self.y:
                            inter_y = robot.y - min(steps_rob2, mod_ver)
                        elif robot.y < self.y:
                            inter_y = robot.y + min(steps_rob2, mod_ver)

                        return inter_x, inter_y
                elif mp_x1 != mp_x2 and mp_y1 == mp_y2:  # both midpoints are the different .type(mp_x) = float and
                    # type(mp_y) = int

                    # Associated with just the 2 midpoints
                    if self.f >= fuel_req_mp1 and robot.f >= fuel_req_mp1:
                        inter_x = mp_x1
                        inter_y = mp_y1
                        return inter_x, inter_y
                    elif self.f >= fuel_req_mp1 and robot.f >= fuel_req_mp2:
                        inter_x = mp_x1
                        inter_y = mp_y1
                        return inter_x, inter_y
                    elif self.f >= fuel_req_mp2 and robot.f >= fuel_req_mp1:
                        inter_x = mp_x2
                        inter_y = mp_y2
                        return inter_x, inter_y

                        # Not associated with midpoints. IP allocated based on fuel sufficiency in both robots.
                    elif self.f < fuel_req_mp2 < fuel_req_mp1 <= robot.f:
                        steps_rob1 = self.f * 2

                        if self.x > robot.x:
                            inter_x = self.x - min(steps_rob1, mod_hor)
                            steps_rob1 = steps_rob1 - min(steps_rob1, mod_hor)
                            # (while steps_rob1 > 0 and mod_hor > 0:
                            # self.x = self.x - 1
                            # mod_hor = mod_hor - 1
                            # steps_rob1 = steps_rob1 - 1)
                        elif self.x < robot.x:
                            inter_x = self.x + min(steps_rob1, mod_hor)
                            steps_rob1 = steps_rob1 - min(steps_rob1, mod_hor)

                        if self.y > robot.y:
                            inter_y = self.y - min(steps_rob1, mod_ver)
                        elif self.y < robot.y:
                            inter_y = self.y + min(steps_rob1, mod_ver)

                        return inter_x, inter_y
                    elif self.f >= fuel_req_mp1 > fuel_req_mp2 > robot.f:
                        steps_rob2 = robot.f * 2

                        if robot.x > self.x:
                            inter_x = robot.x - min(steps_rob2, mod_hor)
                            steps_rob2 = steps_rob2 - min(steps_rob2, mod_hor)
                        elif robot.x < self.x:
                            inter_x = robot.x + min(steps_rob2, mod_hor)
                            steps_rob2 = steps_rob2 - min(steps_rob2, mod_hor)

                        if robot.y > self.y:
                            inter_y = robot.y - min(steps_rob2, mod_ver)
                        elif robot.y < self.y:
                            inter_y = robot.y + min(steps_rob2, mod_ver)

                        return inter_x, inter_y

    def movements(self, des_x, des_y):
        route = []

        dis_hor = des_x - self.x
        dis_ver = des_y - self.y

        mod_hor = abs(dis_hor)
        mod_ver = abs(dis_ver)

        fuel_req = self.fuel_required(mod_hor, mod_ver)

        if self.f >= fuel_req:
            self.update_history(dis_ver, dis_hor, mod_hor, mod_ver, des_x, des_y, fuel_req)

            if dis_hor < 0:
                self.left_movement(mod_hor, route)
            elif dis_hor > 0:
                self.right_movement(mod_hor, route)

            if dis_ver < 0:
                self.down_movement(mod_ver, route)

            elif dis_ver > 0:
                self.up_movement(mod_ver, route)

        return route


class EnergyEfficientRobot(Robot):
    def mileage(self):
        self.dis = self.dis + 1
        self.f = self.f - 0.25
        self.fc = self.fc + 0.25

    def fuel_required(self, mod_hor, mod_ver):
        return (mod_ver + mod_hor) / 4


class FaultyRobot(Robot):
    def up(self):
        print("Error - Up command cannot pass")

    def update_history(self, dis_ver, dis_hor, mod_hor, mod_ver, des_x, des_y, fuel_req):
        if dis_ver < 0:
            mod_ver = 0
        else:
            mod_ver = dis_ver

        fuel_req = (mod_ver + mod_hor) / 2

        if dis_ver >= 0:
            self.y = des_y

        self.x = des_x
        self.f = self.f - fuel_req
        self.fc = self.fc + fuel_req
        self.dis = self.dis + mod_hor + mod_ver

    @staticmethod
    def up_movement(mod_ver, route):
        print("Up command cannot pass")


r1 = Robot(0, 0, 20)
r1.up()
print("position =", r1.position())
r1.down()
print("position =", r1.position())
print("total distance =", r1.distance(), "units")
r1.right()
print("position =", r1.position())
r1.left()
print("position =", r1.position())
print("total distance =", r1.distance(), "units")
print("fuel left =", r1.fuel_left(), "units")
r1.up()
r1.up()
print("position =", r1.position())
print("total distance =", r1.distance(), "units")
print("fuel left =", r1.fuel_left(), "units")
print("route =", r1.movements(1, 5))
print("route =", r1.movements(-1, 9))
print("route =", r1.movements(0, 0))
print("route =", r1.movements(1, 100))
print("position =", r1.position())
print("total distance =", r1.distance(), "units")
print("fuel left =", r1.fuel_left(), "units")
print("fuel consumed =", r1.fuel_consumed(), "units")
print("|" * 90)

print("")
print("Energy Efficient Robot")
print("")
e = EnergyEfficientRobot(1, 3, 8)
e.up()
print("position =", e.position())
e.down()
print("position =", e.position())
print("total distance =", e.distance(), "units")
e.right()
print("position =", e.position())
e.left()
print("position =", e.position())
print("total distance =", e.distance(), "units")
print("fuel left =", e.fuel_left(), "units")
e.up()
e.up()
print("position =", e.position())
print("total distance =", e.distance(), "units")
print("fuel left =", e.fuel_left(), "units")
print("route =", e.movements(1, 5))
print("route =", e.movements(-1, 9))
print("route =", e.movements(0, 0))
print("route =", e.movements(1, 100))
print("position =", e.position())
print("total distance =", e.distance(), "units")
print("fuel left =", e.fuel_left(), "units")
print("fuel consumed =", e.fuel_consumed(), "units")
print("|" * 90)

print("")
print("Faulty Robot")
print("")
f = FaultyRobot(-1, 4, 10)
f.up()
print("position =", f.position())
f.down()
print("position =", f.position())
print("total distance =", f.distance(), "units")
f.right()
print("position =", f.position())
f.left()
print("position =", f.position())
print("total distance =", f.distance(), "units")
print("fuel left =", f.fuel_left(), "units")
f.up()
f.up()
print("position =", f.position())
print("total distance =", f.distance(), "units")
print("fuel left =", f.fuel_left(), "units")
print("route =", f.movements(1, 5))
print("position =", f.position())
print("total distance =", f.distance(), "units")
print("fuel left =", f.fuel_left(), "units")
print("route =", f.movements(-1, 9))
print("position =", f.position())
print("total distance =", f.distance(), "units")
print("fuel left =", f.fuel_left(), "units")
print("route =", f.movements(0, 0))
print("position =", f.position())
print("total distance =", f.distance(), "units")
print("fuel left =", f.fuel_left(), "units")
print("route =", f.movements(1, 100))
print("position =", f.position())
print("total distance =", f.distance(), "units")
print("fuel left =", f.fuel_left(), "units")
print("fuel consumed =", f.fuel_consumed(), "units")
print("|" * 90)

print("")
print("Intersection Point")
print("")

print("")
print("already at intersection point")
r2 = Robot(0, 4, 10)
r3 = Robot(0, 4, 8)
print("**intersection point of (0, 4, 10) & (0, 4, 8) =", r2.intersection_point(r3))

print("")
print("insufficient fuel")
r4 = Robot(0, 0, 2)
r5 = Robot(0, 10, 1)
print("**intersection point of (0, 0, 2) & (0, 10, 1) =", r4.intersection_point(r5))

print("")
print("x,y-int and midpoint")
r6 = Robot(1, 7, 10)
r7 = Robot(3, -7, 8)
print("**intersection point of (1, 7, 10) & (3, -7, 8) =", r6.intersection_point(r7))

print("")
print("x,y-int and self robot with insufficient fuel")
r8 = Robot(1, 7, 1)
r9 = Robot(3, -7, 10)
print("**intersection point of (1, 7, 1) & (3, -7, 10) =", r8.intersection_point(r9))

print("")
print("x,y-int and other robot with insufficient fuel")
r10 = Robot(1, 7, 10)
r11 = Robot(3, -7, 1)
print("**intersection point of (1, 7, 10) & (3, -7, 1) =", r10.intersection_point(r11))

print("")
print("x,y-float and midpoint")
r12 = Robot(1, 3, 10)
r13 = Robot(2, -4, 8)
print("**intersection point of (1, 3, 10) & (2, -4, 8) =", r12.intersection_point(r13))

print("")
print("x,y-float and self robot with insufficient fuel")
r14 = Robot(1, 3, 1)
r15 = Robot(2, -4, 8)
print("**intersection point of (1, 3, 1) & (2, -4, 8) =", r14.intersection_point(r15))

print("")
print("x,y-float and other robot with insufficient fuel")
r16 = Robot(1, 3, 8)
r17 = Robot(2, -4, 1)
print("**intersection point of (1, 3, 8) & (2, -4, 1) =", r16.intersection_point(r17))

print("")
print("x - float, y-int and 1st midpoint")
r18 = Robot(1, 4, 2)
r19 = Robot(2, -4, 2.5)
print("**intersection point of (1, 4, 2) & (2, -4, 2.5) =", r18.intersection_point(r19))

print("")
print("x - float, y-int and 2nd midpoint")
r20 = Robot(1, 4, 2.5)
r21 = Robot(2, -4, 2)
print("**intersection point of (1, 4, 2.5) & (2, -4, 2) =", r20.intersection_point(r21))

print("")
print("x - float, y-int and self robot with insufficient fuel")
r22 = Robot(1, 4, 1)
r23 = Robot(2, -4, 5)
print("**intersection point of (1, 4, 1) & (2, -4, 5) =", r22.intersection_point(r23))

print("")
print("x - float, y-int and other robot with insufficient fuel")
r24 = Robot(1, 4, 5)
r25 = Robot(2, -4, 1)
print("**intersection point of (1, 4, 5) & (2, -4, 1) =", r24.intersection_point(r25))

print("")
print("x - int, y-float and 1st midpoint")
r26 = Robot(4, 1, 2)
r27 = Robot(-4, 2, 2.5)
print("**intersection point of (4, 1, 2) & (-4, 2, 2.5) =", r26.intersection_point(r27))

print("")
print("x - int, y-float and 2nd midpoint")
r28 = Robot(4, 1, 2.5)
r29 = Robot(-4, 2, 2)
print("**intersection point of (4, 1, 2.5) & (-4, 2, 2) =", r28.intersection_point(r29))

print("")
print("x - int, y-float and self robot with insufficient fuel")
r30 = Robot(4, 1, 1)
r31 = Robot(-4, 2, 5)
print("**intersection point of (4, 1, 1) & (-4, 2, 5) =", r30.intersection_point(r31))

print("")
print("x - int, y-float and other robot with insufficient fuel")
r32 = Robot(4, 1, 5)
r33 = Robot(-4, 2, 1)
print("**intersection point of (4, 1, 5) & (-4, 2, 1) =", r32.intersection_point(r33))
