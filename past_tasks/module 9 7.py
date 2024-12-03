def is_prime(func):
    def wrapper(*args, **kwargs):
        checkable = func(*args, **kwargs)
        check = 'Простое'
        for i in range(2, 8): # Все составные числа составлены из различных комбинаций чисел 2, 3, 5 и 7
            if checkable % i == 0:
                check = 'Составное'
                break
        return checkable, check
    return wrapper
@is_prime
def sum_three(*numbers):
    return sum(numbers)
result = sum_three(2, 3, 6)
print(*result)