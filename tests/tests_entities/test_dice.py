from src.entities.dice import Dice


def test_seed_set():
    dice = Dice(seed_num=142)
    assert dice.seed == 142


def test_simple_result():
    dice = Dice()
    assert all(dice.throw() in range(1, 7) for _ in range(100))


def test_repr():
    dice = Dice(123)
    assert "123" in repr(dice)
