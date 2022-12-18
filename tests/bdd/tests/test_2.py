from func import sort_1
from pytest_bdd import scenario, given, when, then

@scenario('/home/khristina/repos/BKIT2022/tests/bdd/features/f2.feature','Data need to be sorted by abs with function sorted')
def test_sort_1():
    pass


@given('some data', target_fixture= 'data')
def data():
    return [4, -30, 100, -100, 123, 1, 0, -1, -4]

@when('data get sorted with sort_1', target_fixture='sorted_data')
def sorted_data(data):
    return sort_1(data)

@then('data is sorted')
def sorted_data(sorted_data):
    assert sorted_data == [123, 100, -100, -30, 4, -4, 1, -1, 0]  



