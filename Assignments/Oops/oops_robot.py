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


r = Robot(0, 0, 20)
r.up()
print("position =", r.position())
r.down()
print("position =", r.position())
print("total distance =", r.distance(), "units")
r.right()
print("position =", r.position())
r.left()
print("position =", r.position())
print("total distance =", r.distance(), "units")
print("fuel left =", r.fuel_left(), "units")
r.up()
r.up()
print("position =", r.position())
print("total distance =", r.distance(), "units")
print("fuel left =", r.fuel_left(), "units")
print("route =", r.movements(1, 5))
print("route =", r.movements(-1, 9))
print("route =", r.movements(0, 0))
print("route =", r.movements(1, 100))
print("position =", r.position())
print("total distance =", r.distance(), "units")
print("fuel left =", r.fuel_left(), "units")
print("fuel consumed =", r.fuel_consumed(), "units")
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
