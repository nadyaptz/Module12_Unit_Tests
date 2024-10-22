import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_runner = Runner('Vasya')
        for i in range(0, 10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    def test_run(self):
        test_runner = Runner('Petya')
        for i in range(0, 10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    def test_challenge(self):
        test_runner1 = Runner('Petya')
        test_runner2 = Runner('Vasya')
        for i in range(0, 10):
            test_runner1.walk()
            test_runner2.run()
        self.assertNotEqual(test_runner1.distance, test_runner2.distance)

if __name__ == "__main__":
    unittest.main()
