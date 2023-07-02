
class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

from unittest import TestCase,main

class TestWorker(TestCase):
    def test_worker_instance_attributes_check(self):
        work1 = Worker('Ivan', 100, 10)
        self.assertEqual('Ivan', work1.name)
        self.assertEqual(100, work1.salary)
        self.assertEqual(10, work1.energy)

    def test_if_rest_working(self):
        work1 = Worker('Ivan', 100, 10)
        work1.rest()
        self.assertEqual(11, work1.energy)

    def test_if_raise_error_if_work_with_zero_energy(self):
        work1 = Worker('Ivan', 100, 0)
        with self.assertRaises(Exception) as ex:
            work1.work()

    def test_if_raise_error_if_work_with_negative_energy(self):
        work1 = Worker('Ivan', 100, -1)
        with self.assertRaises(Exception) as ex:
            work1.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_salary_increase_when_work_method(self):
        work1 = Worker('Ivan', 100, 2)
        self.assertEqual(0, work1.money)
        work1.work()
        self.assertEqual(100, work1.money)

    def test_if_the_workers_energy_was_decrease_when_work(self):
        work1 = Worker('Ivan', 100, 1)
        self.assertEqual(1, work1.energy)
        work1.work()
        self.assertEqual(0, work1.energy)

    def test_if_get_info_return_correct_information(self):
        work1 = Worker('Ivan', 100, 1)
        self.assertEqual('Ivan has saved 0 money.', work1.get_info())
        work1.work()
        self.assertEqual('Ivan has saved 100 money.', work1.get_info())

if __name__ == '__main__':
    main()


