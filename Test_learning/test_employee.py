from unittest import TestCase
from Test_learning.Employee import Employee


class TestEmployee(TestCase):
    def setUp(self):
        self.new_employee = Employee('Vadim', 'Bardier', 120000)

    def test_give_raise_default(self):
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.money, 125000)

    def test_give_raise_no_default(self):
        self.new_employee.give_raise(0)
        self.assertEqual(self.new_employee.money, 120000)
