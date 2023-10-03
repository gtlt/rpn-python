import unittest

from calculator.rpn import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def tearDown(self) -> None:
        self.calculator.clean_stack()

    def test_add_operand(self):
        assert len(self.calculator.get_elements()) == 0
        self.calculator.add_operand(1.01)
        assert self.calculator.element_list[0] == 1.01

    def test_compute(self):
        self.calculator.add_operand(3)
        self.calculator.add_operand(7)
        result = self.calculator.calculate("+")
        assert result == 10.0
        assert self.calculator.get_elements() == [10.0]

    def test_remove_last(self):
        self.calculator.add_operand(8)
        self.calculator.remove_last()
        assert len(self.calculator.get_elements()) == 0
