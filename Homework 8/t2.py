from typing import Callable, Any
import time

MAX_RENTAL_BATCH_LIMIT = 150.0
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8
DEFAULT_RETURN_INDEX_BASE = 10.0

# Набор 1 (Стандартный)
standard_list = [
    {"category": "Action", "total_sales": 4311.85},
    {"category": "Animation", "total_sales": 4656.30},
    {"category": "Children", "total_sales": 3655.55}
]

# Набор 2 (С одинаковой выручкой)
same_list = [
    {"category": "Classics", "total_sales": 1200.10},
    {"category": "Comedy", "total_sales": 4000.00},
    {"category": "Documentary", "total_sales": 4000.00}
]

# Набор 3 (Единичный элемент)
one_list = [
    {"category": "Drama", "total_sales": 500.00}
]


# 2,4. Type Hints: Callable, Any & list[dict[str, str | float]]
def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    # 3. Google-docstring for the performance_logger decorator
    """
    Decorator gets the list of dicts from function, counts execution_time, unpacks list and gets dictionary elements.

    Args: func (Callable[..., Any]): Incoming function.

    Returns: list[dict[str, str | float]]: Outcoming list of dicts.

    """

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        # 1. Using constant PERFORMANCE_LOG_PREFIX
        print(f'{PERFORMANCE_LOG_PREFIX} Функция {func.__name__} выполнена за {execution_time:.{TIME_DECIMALS}f} сек.')
        print('Топ категорий по выручке:')
        for i, r in enumerate(result, start=1):
            # 1. Using constant TIME_DECIMALS
            print(f'{i}. {r.get('category')}: {r.get('total_sales')}')
        return result

    return wrapper


@performance_logger
def get_sorted_report(dicts_list: list) -> list:
    # 3. Google-docstring for the func
    """
    Function gets list of dicts and sorts them by key value "total_sales" and makes a reverse.

    Args: dicts_list (list): A list of dicts.

    Returns: sorted_dicts (list): A list of sorted and reversed dicts.

    """
    sorted_dicts = sorted(dicts_list, key=lambda dicts_list: dicts_list['total_sales'], reverse=True)
    return sorted_dicts


print('=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===')

print('--- ТЕСТ 1 ---')
get_sorted_report(standard_list)

print('--- ТЕСТ 2 ---')
get_sorted_report(same_list)

print('--- ТЕСТ 3 ---')
get_sorted_report(one_list)
