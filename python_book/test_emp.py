import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests the 'raise' method in the Employee class"""

    def setUp(self):
        """
        Create an employee with a salary to use in all test methods
        """
        self.default_raise = 5000
        self.custom_raise = 20000
        self.initial_salary = 120000

        self.me = Employee('Tom', 'Harned', self.initial_salary)        

    def test_give_default_raise(self):
        """Test that the method correctly gives a default raise"""
        self.me.get_raise()
        self.assertEqual(self.me.salary, self.initial_salary + self.default_raise)

    def test_give_custom_raise(self):
        """Test that the method correctly gives a default raise"""
        self.me.get_raise(self.custom_raise)
        self.assertEqual(self.me.salary, self.initial_salary + self.custom_raise)
unittest.main()
