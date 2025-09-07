import pytest

from app.calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_adding(self):
        result = self.calc.adding(2, 3)
        assert result == 5

    def test_subtraction(self):
        result = self.calc.subtraction(5, 3)
        assert result == 2

    def test_multiply(self):
        result = self.calc.multiply(2, 3)
        assert result == 6

    def test_division(self):
        result = self.calc.division(6, 3)
        assert result == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)
