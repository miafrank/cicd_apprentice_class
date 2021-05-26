from cicd_class.phonebook import phone_numbers
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),
                             os.pardir,
                             "cicd_apprentince_class"))


def test_phone_numbers():
    test_phone_book = {"Janae": "314986448"}
    result = phone_numbers(test_phone_book)
    assert result == {'Person: Janae Phone Number: 314986448'}
