def phone_numbers(numbers):
    result = ""
    for k, v in numbers.items():
        result += f'Person: {k} Phone Number: {v}\n'     
    return result