import unittest
from src.pathfinding import astar_search

class TestAStar(unittest.TestCase):
    def test_astar(self):
        grid = [[0 for _ in range(5)] for _ in range(5)]
        grid[2][2] = 1 # adding an obstacle
        start, goal = (0,0),  (4,4)
        path = astar_search(start, goal, grid)
        self.assertIsNotNone(path)

if __name__ == "__main__" :
    unittest.main()       