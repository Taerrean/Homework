import unittest
import runprog
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r1 = runprog.Runner('Vasya')
        for _ in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)
    def test_run(self):
        r1 = runprog.Runner('Vasya')
        for _ in range(10):
            r1.run()
        self.assertEqual(r1.distance, 100)
    def test_competition(self):
        r1 = runprog.Runner('Vasya')
        r2 = runprog.Runner('Petya')
        for _ in range(10):
            r1.walk()
        for _ in range(10):
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)
