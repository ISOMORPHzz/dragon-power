def max_power(n: int) -> int:

    if n < 1 or n > 99:
        raise ValueError("N должно быть в диапазоне 1..99")
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    
    remainder = n % 3
    
    if remainder == 0:
        # Все тройки: 3 + 3 + ... + 3
        return 3 ** (n // 3)
    
    if remainder == 1:
        # Заменяем одну 3+1 на 2+2  (2·2 = 4 > 3·1 = 3)
        return 4 * (3 ** ((n - 4) // 3))
    
    # remainder == 2
    # Все тройки + одна двойка
    return 2 * (3 ** ((n - 2) // 3))