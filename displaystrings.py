def display_names(names):
    for name in names:
        print(name, end = ' ')



def display_names_recursive(x, names):
    if x == 0:
        print(names[x], end = ' ')
    else:
        display_names_recursive(x - 1, names)
        print(names[x], end = ' ')
        

def fibonacci1(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci1(number-1) + fibonacci1(number-2)
    
def fibonacci2(number):
    numbers = [0, 1]
    for i in range(number):
        numbers[i % 2] = numbers[0] + numbers[1]
    return numbers[number % 2]


def main():
    names = ['Adam', 'Bob', 'Charles', 'Doug', 'Eddie']
    x = len(names) - 1
    display_names_recursive(x, names)
    number = 20
    print('')
    print(fibonacci1(number))
    print(fibonacci2(number))


main()