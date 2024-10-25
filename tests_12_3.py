import unittest
from pprint import pprint


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def __repr__(self):
        return f"{self.name}"

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_runner = Runner('Vasya')
        for i in range(0, 10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_runner = Runner('Petya')
        for i in range(0, 10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_runner1 = Runner('Petya')
        test_runner2 = Runner('Vasya')
        for i in range(0, 10):
            test_runner1.walk()
            test_runner2.run()
        self.assertNotEqual(test_runner1.distance, test_runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results_list = []

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in range(len(cls.all_results_list)):
            pprint(cls.all_results_list[i])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        self.tournament1 = Tournament(90, self.runner1, self.runner3)
        all_results1 = self.tournament1.start()
        self.assertTrue(all_results1[2] == 'Ник')
        TournamentTest.all_results_list.append(all_results1)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        self.tournament2 = Tournament(90, self.runner2, self.runner3)
        all_results2 = self.tournament2.start()
        self.assertTrue(all_results2[2] == 'Ник')
        TournamentTest.all_results_list.append(all_results2)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        self.tournament3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        all_results3 = self.tournament3.start()
        self.assertTrue(all_results3[3] == 'Ник')
        TournamentTest.all_results_list.append(all_results3)


if __name__ == "__main__":
    unittest.main()
