from func import Unique
from pytest_bdd import scenario, given, when, then

@scenario('/home/khristina/repos/BKIT2022/tests/bdd/features/f1.feature','Getting list of unique elements')
def testing_unique():
    pass

@given('some data', target_fixture= 'data')
def data():
    return ['Red', 'bLue', 'pinK', 'reD', 'greeen', 'purple', 'Purple  ', 'green']

@when('data is getting unique', target_fixture='unique_data')
def unique_data(data):
    return list(Unique(data, ignore_case = True))

@then('data is unique')
def res_data(unique_data):
    assert unique_data == ['Red', 'bLue', 'pinK', 'greeen', 'purple', 'green']