"""
* Description: Test cases for fraud_detection.py
* Collaboration:
"""

import fraud_detection as fd
import math


def test_ones_and_tens_digit_histogram():
    """
    Tests ones_and_tens_digit_histogram function checking actual value
    to expected value. Assertion errors if test fails.
    """
    actual = fd.ones_and_tens_digit_histogram([127, 426, 28, 9, 90])
    expected = [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])
    actual = fd.ones_and_tens_digit_histogram([0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
                                              55, 89, 144, 233, 377, 610, 987,
                                              1597, 2584, 4181, 6765])
    expected = [0.21428571428571427, 0.14285714285714285, 0.047619047619047616,
                0.11904761904761904, 0.09523809523809523, 0.09523809523809523,
                0.023809523809523808, 0.09523809523809523, 0.11904761904761904,
                0.047619047619047616]
    for j in range(len(actual)):
        assert math.isclose(actual[j], expected[j])


def mean_squared_error():
    """
    Tests mean_square_error function checking actual value to expected value.
    Assertion error if test fails.
    """
    actual = fd.mean_squared_error([1, 4, 9], [6, 5, 4])
    expected = 17.0
    assert math.isclose(actual, expected)
    actual = fd.mean_squared_error([0, 0, 0], [0, 0, 0])
    expected = 0.0
    assert math.isclose(actual, expected)
    actual = fd.mean_squared_error([2, 2, 2], [2, 2, 2])
    expected = 0.0


def calculate_mse_with_uniform():
    """
    Tests calculate_mse_with_uniform checking actual value to expected value.
    Assertion errors if test fails.
    """
    iran_candidates = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]
    iran_votes = fd.extract_election_votes("election-iran-2009.csv",
                                           iran_candidates)
    hist_votes_iran = fd.ones_and_tens_digit_histogram(iran_votes)
    actual = fd.calculate_mse_with_uniform(hist_votes_iran)
    expected = 0.000739583333333
    assert math.isclose(actual, expected)

    usa_candidate = ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"]
    votes_usa = fd.extract_election_votes("election-us-2008.csv",
                                          usa_candidate)
    hist_votes_usa = fd.ones_and_tens_digit_histogram(votes_usa)
    actual = fd.calculate_mse_with_uniform(hist_votes_usa)
    expected = 0.0001410025876058068
    assert math.isclose(actual, expected)


def main():
    test_ones_and_tens_digit_histogram()
    mean_squared_error()
    calculate_mse_with_uniform()


if __name__ == "__main__":
    main()
