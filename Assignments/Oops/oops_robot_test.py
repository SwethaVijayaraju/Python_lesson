import unittest

from Assignments.Oops.oops_robot import Robot


class RobotCase(unittest.TestCase):
    def test_already_ip1(self):
        # print("already at intersection point")
        r1 = Robot(0, 4, 10)
        r2 = Robot(0, 4, 8)
        result = r1.intersection_point(r2)
        self.assertEqual("Robots are already at the intersection point", result)

    def test_already_ip2(self):
        # print("insufficient fuel")
        r1 = Robot(0, 0, 2)
        r2 = Robot(0, 10, 1)
        result = r1.intersection_point(r2)
        self.assertEqual("Fuel not sufficient", result)

    def test_already_ip3(self):
        # print("x,y-int and midpoint")
        r1 = Robot(1, 7, 10)
        r2 = Robot(3, -7, 8)
        result = r1.intersection_point(r2)
        self.assertEqual((2, 0), result)

    def test_already_ip4(self):
        # print("x,y-int and self robot with insufficient fuel")
        r1 = Robot(1, 7, 1)
        r2 = Robot(3, -7, 10)
        result = r1.intersection_point(r2)
        self.assertEqual((3, 7), result)

    def test_already_ip5(self):
        # print("x,y-int and other robot with insufficient fuel")
        r1 = Robot(1, 7, 10)
        r2 = Robot(3, -7, 1)
        result = r1.intersection_point(r2)
        self.assertEqual((1, -7), result)

    def test_already_ip6(self):
        # print("x,y-float and midpoint")
        r1 = Robot(1, 3, 10)
        r2 = Robot(2, -4, 8)
        result = r1.intersection_point(r2)
        self.assertEqual((2, 0), result)

    def test_already_ip7(self):
        # print("x,y-float and self robot with insufficient fuel")
        r1 = Robot(1, 3, 1)
        r2 = Robot(2, -4, 8)
        result = r1.intersection_point(r2)
        self.assertEqual((2, 2), result)

    def test_already_ip8(self):
        # print("x,y-float and other robot with insufficient fuel")
        r1 = Robot(1, 3, 8)
        r2 = Robot(2, -4, 1)
        result = r1.intersection_point(r2)
        self.assertEqual((1, -3), result)

    def test_already_ip9(self):
        # print("x - float, y-int and 1st midpoint")
        r1 = Robot(1, 4, 2)
        r2 = Robot(2, -4, 2.5)
        result = r1.intersection_point(r2)
        self.assertEqual((1, 0), result)

    def test_already_ip10(self):
        # print("x - float, y-int and 2nd midpoint")
        r1 = Robot(1, 4, 2.5)
        r2 = Robot(2, -4, 2)
        result = r1.intersection_point(r2)
        self.assertEqual((2, 0), result)

    def test_already_ip11(self):
        # print("x - float, y-int and self robot with insufficient fuel")
        r1 = Robot(1, 4, 1)
        r2 = Robot(2, -4, 5)
        result = r1.intersection_point(r2)
        self.assertEqual((2, 3), result)

    def test_already_ip12(self):
        # print("x - float, y-int and other robot with insufficient fuel")
        r1 = Robot(1, 4, 5)
        r2 = Robot(2, -4, 1)
        result = r1.intersection_point(r2)
        self.assertEqual((1, -3), result)

    def test_already_ip13(self):
        # print("x - int, y-float and 1st midpoint")
        r1 = Robot(4, 1, 2)
        r2 = Robot(-4, 2, 2.5)
        result = r1.intersection_point(r2)
        self.assertEqual((0, 1), result)

    def test_already_ip14(self):
        # print("x - int, y-float and 2nd midpoint")
        r1 = Robot(4, 1, 2.5)
        r2 = Robot(-4, 2, 2)
        result = r1.intersection_point(r2)
        self.assertEqual((0, 2), result)

    def test_already_ip15(self):
        # print("x - int, y-float and self robot with insufficient fuel")
        r1 = Robot(4, 1, 1)
        r2 = Robot(-4, 2, 5)
        result = r1.intersection_point(r2)
        self.assertEqual((2, 1), result)

    def test_already_ip16(self):
        # print("x - int, y-float and other robot with insufficient fuel")
        r1 = Robot(4, 1, 5)
        r2 = Robot(-4, 2, 1)
        result = r1.intersection_point(r2)
        self.assertEqual((-2, 2), result)


if __name__ == '__main__':
    unittest.main()
