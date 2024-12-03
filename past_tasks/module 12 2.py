import runner_and_tournament as rat
import unittest

class TournamentError(Exception):
    pass

class Tournament_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        self.r1 = rat.Runner('Усэйн', 10)
        self.r2 = rat.Runner('Андрей', 9)
        self.r3 = rat.Runner('Ник', 3)

    def test_challenge_1(self):
        self.tour = rat.Tournament(90, self.r1, self.r3)
        test_1 = self.tour.start()
        Tournament_test.all_results['test_1'] = test_1
        self.assertTrue(test_1[max(test_1.keys())] == 'Ник')

    def test_challenge_2(self):
        self.tour = rat.Tournament(90, self.r2, self.r3)
        test_2 = self.tour.start()
        Tournament_test.all_results['test_2'] = test_2
        self.assertTrue(test_2[max(test_2.keys())] == 'Ник')

    def test_challenge_3(self):
        self.tour = rat.Tournament(90, self.r1, self.r2, self.r3)
        test_3 = self.tour.start()
        Tournament_test.all_results['test_3'] = test_3
        self.assertTrue(test_3[max(test_3.keys())] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)

if __name__ == '__main__':
    unittest.main(verbosity=2)