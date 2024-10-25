import unittest
import tests_12_3

tournamentTS = unittest.TestSuite()
tournamentTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
tournamentTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournamentTS)