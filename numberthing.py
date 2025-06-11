

def output_integers(int, binary, octal, hex):
    print(int, binary, octal, hex)

def get_int():
    return 10

def is_integer(int):
    return True

def convert(int):
    binary = convert_to_binary(int)
    octal = convert_to_octal(int)
    hex = convert_to_hex(int)

    return binary, octal, hex

def convert_to_binary(int):
    return "0b11"

def convert_to_octal(int):
    return "o357"

def convert_to_hex(int):
    return "0xf3"

def main():
    int = get_int()
    binary, octal, hex = convert(int)
    output_integers(int, binary, octal, hex)


main()