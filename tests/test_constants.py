import pytest
from hypothesis import given
from hypothesis.strategies import integers

from lost_spc.constants import get_c4, get_d


@given(integers(max_value=1))
def test_get_d_error(val):
    with pytest.raises(ValueError):
        get_d(val)


@given(integers(max_value=1))
def test_get_c4_error(val):
    with pytest.raises(ValueError):
        get_c4(val)
