# Функція для обробки колекції (список або кортеж)
def process_data(data, operation):
    try:
        if isinstance(data, list):
            return [operation(x) for x in data]
        elif isinstance(data, tuple):
            return tuple(operation(x) for x in data)
        else:
            return "Потрібно передати список або кортеж"
    except Exception as e:
        return f"Помилка: {e}"


# Функція для фільтрації даних (список або кортеж)
def filter_data(data, predicate):
    try:
        if isinstance(data, list):
            return [x for x in data if predicate(x)]
        elif isinstance(data, tuple):
            return tuple(x for x in data if predicate(x))
        else:
            return "Потрібно передати список або кортеж"
    except Exception as e:
        return f"Помилка: {e}"


# Функція для об’єднання значень
def combine_values(*args):
    """
    Додає всі числа або з'єднує всі рядки.
    :param args: довільна кількість чисел або рядків
    :return: об'єднане значення
    """
    try:
        if not args:
            return "Немає даних"

        if isinstance(args[0], (int, float)):
            return sum(args)

        elif isinstance(args[0], str):
            return "".join(args)

        else:
            return "Тип не підтримується"
    except Exception as e:
        return f"Помилка: {e}"

print("Обробка списку (×2):", process_data([1, 2, 3], lambda x: x * 2))
print("Обробка кортежа (+1):", process_data((10, 20), lambda x: x + 1))

print("Фільтрація списку (>1):", filter_data([1, 2, 3], lambda x: x > 1))
print("Фільтрація кортежа (парні):", filter_data((1, 2, 3, 4), lambda x: x % 2 == 0))

print("Сума чисел:", combine_values(1, 2, 3))  # → 6
print("З'єднання рядків:", combine_values("Сонце", "Марс"))  # → "СонцеМарс"
