from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_addition_makes_bigger(x, y):
    print(x, y)
    assert x + y >= x

test_addition_makes_bigger()

