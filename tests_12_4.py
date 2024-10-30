import unittest
import logging

logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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
        try:
            test_runner = Runner('Vasya', -7)
            for i in range(0, 10):
                test_runner.walk()
            self.assertEqual(test_runner.distance, 50)
            logging.info(f'test_walk выполнен успешно')
        except ValueError as err:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test_runner = Runner(2)
            for i in range(0, 10):
                test_runner.run()
            self.assertEqual(test_runner.distance, 100)
            logging.info(f'test_run выполнен успешно')
        except TypeError:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_runner1 = Runner('Petya')
        test_runner2 = Runner('Vasya')
        for i in range(0, 10):
            test_runner1.walk()
            test_runner2.run()
        self.assertNotEqual(test_runner1.distance, test_runner2.distance)


if __name__ == '__main__':
    unittest.main()
first = Runner('Вася', 10)
second = Runner('Илья', 5)
# third = Runner('Арсен', 10)

t = Tournament(101, first, second)
print(t.start())
