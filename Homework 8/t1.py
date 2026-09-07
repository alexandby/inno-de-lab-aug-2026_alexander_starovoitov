# INTRO:CONSTANTS
MAX_RENTAL_BATCH_LIMIT = 150.0
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8
DEFAULT_RETURN_INDEX_BASE = 10.0

# INTRO:DATA
batches_data = [
    ("Academy Dinosaur", 30, 2.99, 0.0),
    ("Affair Prejudice", 40, 4.99, 0.1),
    ("Agent Truman", 10, 1.99, 0.0),
    ("African Egg", 50, 3.5, 0.2)
]


# function
# 2,4. Added Type Hints & calculate_rental_batch function
def calculate_rental_batch(quantity: int, rental_rate: float, discount: float = 0.0) -> tuple[float, bool]:
    # 3. Added google-style docstring
    """Calculates the rental batch total with genre discount.

    Applies a discount to each position, calculates the total amount,
    the standard rental rate, and the discounted rate.

    Args:
        quantity: List of batch quantities.
        rental_rate: Rent cost for batches of disk.
        discount: Discount that depends on the disk genre.

    Returns (position args):
        A tuple containing the final sum and the batch limit status.
            - final_sum (float): Total cost of the disks batches.
            - is_limit_exceeded (bool): True if manual input is required because the amount exceeds the limit.

    Examples (named args):
        #>>> calculate_rental_batch(30, 2.99)
        (179.64, True)
        #>>> calculate_rental_batch(quantity=40, rental_rate=4.99, discount=0.1)
    """
    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    # 1. Using the constant MAX_RENTAL_BATCH_LIMIT
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT

    return final_sum, is_limit_exceeded


print('=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===')
for i, (name, sum_val, limit_val, discount_val) in enumerate(batches_data, start=1):
    disks_val, disks_cost = calculate_rental_batch(sum_val, limit_val, discount_val)
    print(f'Партия {i} ({name}): Сумма {disks_val}$. Превышение лимита: {disks_cost}')