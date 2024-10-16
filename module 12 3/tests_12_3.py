import runner_and_tournament as rat
import unittest, runner


class TournamentError(Exception):
    pass

is_frozen= False


class RunnerTest(unittest.TestCase): # это тест-кейс
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        self.r1 = runner.Runner('Langsamer Karl')
        for i in range(10):
            self.r1.walk()
        self.assertEqual(self.r1.distance, 50)
        #self.assertEqual(self.r1.distance, 60)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        self.r2 = runner.Runner('Schneller Otto')
        for i in range(10):
            self.r2.run()
        self.assertEqual(self.r2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.r3 = runner.Runner('Stille Moritz')
        self.r4 = runner.Runner('Geschwindiger Siegfried')
        for i in range(10):
            self.r3.walk(), self.r4.run()
        self.assertNotEqual(self.r3.distance, self.r4.distance)


class Tournament_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        cls.is_frozen = True
    def setUp(self):
        self.r1 = rat.Runner('Усэйн', 10)
        self.r2 = rat.Runner('Андрей', 9)
        self.r3 = rat.Runner('Ник', 3)

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge_1(self):
        self.tour = rat.Tournament(90, self.r1, self.r3)
        test_1 = self.tour.start()
        Tournament_test.all_results['test_1'] = test_1
        self.assertTrue(test_1[max(test_1.keys())] == 'Ник')

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge_2(self):
        self.tour = rat.Tournament(90, self.r2, self.r3)
        test_2 = self.tour.start()
        Tournament_test.all_results['test_2'] = test_2
        self.assertTrue(test_2[max(test_2.keys())] == 'Ник')

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge_3(self):
        self.tour = rat.Tournament(81, self.r1, self.r2, self.r3)
        test_3 = self.tour.start()
        Tournament_test.all_results['test_3'] = test_3
        self.assertTrue(test_3[max(test_3.keys())] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)

if __name__ == '__main__':
    unittest.main()