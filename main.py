from dragon_math import max_power


def main():
    try:
        n = int(input("Введите количество голов драконьей стаи (1..99): "))
        result = max_power(n)
        print(result)
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()