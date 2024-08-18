def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    if isinstance(numbers, str):
        numbers = numbers.split(',')

    if isinstance(numbers, (list, tuple, set)):
        for number in numbers:
            try:
                num = float(str(number).strip())
                result += num
            except ValueError:
                incorrect_data += 1
                print(f"Некорректный тип данных для подсчёта суммы - {number}")
    else:
        incorrect_data += 1
        print(f"Некорректный тип данных для подсчёта суммы - {numbers}")

    return result, incorrect_data


def calculate_average(numbers):

    try:
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError
        total_sum, incorrect_count = personal_sum(numbers)
        average = total_sum / len(numbers)
        return average
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
