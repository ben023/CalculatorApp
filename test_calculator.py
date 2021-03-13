import calculator1

class TestCalculator:
    def test_add(self):
        assert 6 == calculator1.add(1,5)

        assert 2 == calculator1.subtract(4,2)