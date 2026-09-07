from typing import Any

MAX_RENTAL_BATCH_LIMIT = 150.0
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8
DEFAULT_RETURN_INDEX_BASE = 10.0

input_data = [
    ['Matrix', 5, 1.5],
    ['Inception', 'пять', 2.0],
    ['Avatar', 0, 2.5],
    ['Interstellar', [3, ], 3.0]
]


def calculate_overdue_fine(name: str, numeric_days: Any, fine_rate: float) -> tuple[float, float] | None:
    try:
        total_fine = float(numeric_days) * fine_rate
        # Индекс оборачиваемости
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days
        print(f'Фильм: {name} | Итоговый штраф: {total_fine} | Индекс:{return_index}')
    except ValueError:
        print(f'[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для "{name}": could not be converted to float: "{numeric_days}"')
    except TypeError:
        print(f'[ОШИБКА ТИПА] Некорректный тип данных для "{name}": float() argument must be a string or a real number, not { type(numeric_days) }')
    except ZeroDivisionError:
        print(f'[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для "{name}": float divided by zero')
    finally:
        print('--- Проверка транзакции возврата завершена ---')


print('=== ПРОВЕРКА ВОЗВРАТОВ ===')
for i in range(len(input_data)):
    calculate_overdue_fine(input_data[i][0], input_data[i][1], input_data[i][2])