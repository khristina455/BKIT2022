from func import sort_2
from pytest_bdd import scenario, given, when, then

@scenario('/home/khristina/repos/BKIT2022/tests/bdd/features/f3.feature','Data need to be sorted by abs with lambda expression')
def test_sort_2():
    pass

@given('some data', target_fixture= 'data')
def data():
    return [4, -30, 100, -100, 123, 1, 0, -1, -4]

@when('data get sorted with sort_2', target_fixture='sorted_data')
def sorted_data(data):
    return sort_2(data)

@then('data is sorted')
def sorted_data(sorted_data):
    assert sorted_data == [123, 100, -100, -30, 4, -4, 1, -1, 0]  



