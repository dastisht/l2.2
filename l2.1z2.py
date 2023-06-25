def decimal_to_hex(decimal):
    hex_digits = "0123456789ABCDEF"
    hex_string = ""

    if decimal == 0:
        return "0"

    if decimal < 0:
        decimal = -decimal
        hex_string = "-"

    while decimal > 0:
        remainder = decimal % 16
        hex_string = hex_digits[remainder] + hex_string
        decimal //= 16

    return hex_string

decimal_number = int(input("Введите целое число: "))
hexadecimal_number = decimal_to_hex(decimal_number)
print("Шестнадцатеричное представление:", hexadecimal_number)
print("Проверка:", hex(decimal_number)[2:])
