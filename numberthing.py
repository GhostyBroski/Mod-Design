

def output_integers(int, binary, octal, hex):
    '''Format output for converted numbers'''
    print(int, binary, octal, hex)

def get_int():
    '''Obtain int number from user, Ensure that it is an int and catch all errors'''
    return 10

def is_integer(int):
    return True

def convert(int):
    '''Driver function to call individual conversion fucntions'''
    binary = convert_to_binary(int)
    octal = convert_to_octal(int)
    hex = convert_to_hex(int)

    return binary, octal, hex

def convert_to_binary(int):
    '''Convert int number to binary'''
    return "0b11"

def convert_to_octal(int):
    '''Convert int number to octal'''
    return "o357"

def convert_to_hex(int):
    '''Convert int number to hexadecimal'''
    return "0xf3"

def main():
    int = get_int()
    binary, octal, hex = convert(int)
    output_integers(int, binary, octal, hex)

def test_conversions():
    '''Test runner function for conversions'''
    pass

main()