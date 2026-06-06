from Sales import read_data, total

def test_row_parses_valid_line():
    result = read_data("coffee,drinks,12.5,3\n")

    assert result == {
        "n": "coffee",
        "c": "drinks",
        "a": 12.5,
        "q": 3,
    }


def test_total_calculates_sum_with_discount():
    data = [
        {"n": "coffee", "c": "drinks", "a": 10.0, "q": 2},
        {"n": "tea", "c": "drinks", "a": 5.0, "q": 4},
    ]

    assert total(data) == 40.0
    assert total(data, 10) == 36.0  

test_row_parses_valid_line()
test_total_calculates_sum_with_discount()
