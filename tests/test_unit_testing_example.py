from .cicd_class.phonebook import phone_numbers


def test_phone_numbers():
    test_phone_book = {"Janae": "314986448"}
    result = phone_numbers(test_phone_book)
    assert result == {'Person: Janae Phone Number: 314986448'}
