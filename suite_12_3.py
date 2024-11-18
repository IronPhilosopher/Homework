import unittest
import tests_12_3

ts = unittest.TestSuite()
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

ruu = unittest.TextTestRunner(verbosity=2)
ruu.run(ts)
