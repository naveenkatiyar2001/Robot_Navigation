import unittest
from src.robot import Robot

class TestRobot(unittest.TestCase):
    def test_movement(self):
        robot = Robot(0, 0, 0)
        robot.move_forward()
        self.assertEqual((robot.x, robot.y), (1, 0))

if __name__ == "__main__":
    unittest.main()    
