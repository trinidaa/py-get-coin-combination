import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (29, [4, 0, 0, 1]),
        (38, [3, 0, 1, 1]),
    ],
)
def test_get_coin_combination(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result
