import unittest

from calculator import repository


class TestRepositoryMethods(unittest.TestCase):
    def test_two_clients_calculator(self):
        stack1 = repository.create_calculator("an ip")
        stack2 = repository.create_calculator("another ip")
        assert repository.get_calculator("an ip")
        assert repository.get_calculator("another ip")
