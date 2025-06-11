# 1. Name:
#      Ash Jones
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      This program prompts the user for a month and year, then displays the corresponding calendar table while accounting for the appropriate start of the month and datatypes for the input.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was definitely figuring out the compute offset logic, which I eventually was able to grasp. For me, understanding what the function was even for was the first hurdle. Then, writing how to tabulate through it is what got me going as I realized I could use other functions to help me build the necessary logic such as the days of the month and year. Grasping this, I was able to effectively tackle that part and take on other difficulties such as making my asserts and making sure the offset was accurate.
# 5. How long did it take for you to complete the assignment?
#      2 hrs 32 mins



def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline

def is_leap_year(year):
    '''Determine if a given year is a leap year'''
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))


def num_days_in_month(month, year):
    '''Return the number of days in a given month'''
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return -1  # Invalid month


def compute_offset(year, month):
    '''Compute the offset (day of week) of the 1st day of the given month and year'''
    total_days = 0

    # Add days from full years
    for y in range(1753, year):
        total_days += 366 if is_leap_year(y) else 365

    # Add days from months of the current year
    for m in range(1, month):
        total_days += num_days_in_month(m, year)

    offset = (total_days + 1) % 7  # Jan 1, 1753 was Monday => offset 1
    return offset


def get_month():
    '''Prompt and validate the month input'''
    while True:
        try:
            month = int(input("Enter the month number: "))
            if 1 <= month <= 12:
                return month
            else:
                print("Month must be between 1 and 12.")
        except ValueError:
            print("Month must be an integer.")


def get_year():
    '''Prompt and validate the year input'''
    while True:
        try:
            year = int(input("Enter year: "))
            if year >= 1753:
                return year
            else:
                print("Year must be 1753 or later.")
        except ValueError:
            print("Year must be an integer.")


def main():
    month = get_month()
    year = get_year()

    num_days = num_days_in_month(month, year)
    offset = compute_offset(year, month)

    display_table(offset, num_days)


# Run the main program
if __name__ == "__main__":
    main()