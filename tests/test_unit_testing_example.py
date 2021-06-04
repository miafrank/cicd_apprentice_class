from cicd_class.phonebook import phone_numbers


def test_phone_numbers():
    test_phone_book = {"Janae": "3149846448", "Mia": "6364484018"}
    result = phone_numbers(test_phone_book)
    assert result == "Person: Janae Phone Number: 3149846448\nPerson: Mia Phone Number: 6364484018\n"
