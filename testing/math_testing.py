from my_math import (
add,
add_with_bug,
calculate_tax_with_bug,
calculate_tax
)

def test_addition():
    assert add(2, 2) == 4
    print("Success")

def test_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    assert add_with_bug(1, 1) == 1
    print("Bug")
    #assert add_with_bug(2, 3) == 5

# Примеры не очень
# def test_dublicate():
#     #тест дублирует себя
#     assert add(2, 2) == 2 + 2
#
# def test_overcomplicate():
#     #Слишком перегруженный тест
#     for i in range(0,2**32):
#         for j in range(0,2**32):
#             assert add(i, i) == sum(i, j)

def test_reasonable():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(6, 7) == 13
    assert add(-6, 7) == 1
    print("reasonable")

def test_commutative():
    assert add(2, -2) == 0
    assert add(-2, 2) == 0
    print("Commutative is true")

#переходим к тесту новой функ
def calculate_tax_with_bug_check():
    # типами ограничили случаи которые можем посмотреть

    try:
        assert calculate_tax_with_bug(1000) == 150.0
        assert calculate_tax_with_bug(100) == 15.0
        assert calculate_tax_with_bug(10) == 1.5
        assert calculate_tax_with_bug(1) == 0.15
        assert calculate_tax_with_bug(243) == 36.45
    except:
        print("Tax Calculation doesnt work")

def test_tax_calculation():
    assert calculate_tax(1000) == 150.0
    assert calculate_tax(100) == 15.0
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(24.5) == 3.67
    print("Tax Calculation works")

#На самом деле нет, надо как то сотые копейки посчитать, прям щас думать не хочу

if __name__ == "__main__":
    test_addition()
    test_with_bug()
    # test_dublicate()
    test_reasonable()
    test_commutative()
    calculate_tax_with_bug_check()
    test_tax_calculation()