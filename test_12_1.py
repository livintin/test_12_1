import module_12_1
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner_1 = module_12_1.Runner('Bob')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = module_12_1.Runner('Alan')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_1 = module_12_1.Runner('Bob')
        runner_2 = module_12_1.Runner('Alan')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()
