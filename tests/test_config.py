import pytest


class NotInRange(Exception):
    def __init__(self, message="value not in range") -> None:
        self.message = message
        super().__init__(self.message)


def test_generic():
    a = 5
    with pytest.raises(NotInRange):
        if a in range(3, 9):
            raise NotInRange


def test_somthing():
    a = 2
    b = 2
    assert True
