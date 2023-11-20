# a test that fails if we find integer solutions to Pythagoras equation"

from hypothesis import given, strategies as st, settings

# generate small integers, 0...10
smallints = st.integers(min_value=1, max_value=10)

@given(smallints, smallints, smallints)
@settings(max_examples=1000)  # would not easily fail with fewer cases
def test_pythagoras(x, y, z):
    "test fails if we find integer solutions to Pythagoras equation"
    assert x*x + y*y != z*z

    
test_pythagoras()

