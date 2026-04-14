
from orchestrator.result import Result, Success, Failure

NUMERIC = int | float



def divide(num: NUMERIC, den: NUMERIC, rounding_scale: int = 2) -> Success[float] | Failure:
    # if not isinstance(num, NUMERIC) or not isinstance(den, NUMERIC):
    #     return Failure("Either the numerator or the Denominator is not of Numeric Value (integer, float)")
    if den == 0:
        return Failure("The denominator cannot be zero")
    else:
        return Success(round(num / den, rounding_scale))


def test_success():
    try:
        assert divide(10, 2) == Success(5.00)
    except AssertionError:
        print("Test 1: Failed")
    else:
        print("Test 1: OK")

def main():
    test_success()


if __name__ == "__main__":
    main()
