class Employee():
    """Collect info about an employee"""
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def get_raise(self, sal_increase=5000):
        self.salary += sal_increase 
