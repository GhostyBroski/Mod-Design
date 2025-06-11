# TESTS FOR LAB 06

# 1: Invalid Inputs: Recognize if the user types something other than a coordinate or the letter 'Q' to quit
# Choose 131.05.Easy.json and try to submit 'r' when prompted for a cell / to quit
# (This is an Error State)

# Expected Output: "ERROR: The value r is invalid input"

# 2: Reversed coordinates: Handle both "B2" and "2B" in the same way
# Using 131.05.Easy.json, use 2B as a cell. Put 8 as a number so we can use this again later.
# (This is a Requirement)

# Expected Output: It will prompt you with "> ", then the number will make it go: "ERROR: The value 8 already exists in the column"

# 3: Lowercase coordinates: Handle both "B2" and "b2" in the same way
# Using 131.05.Easy.json, use b2 as a cell. Put 8 as a number so we can use this again later.
# (This is a Requirement)

# Expected Output: It will prompt you with "> ", then the number will make it go: "ERROR: The value 8 already exists in the column"

# 4: Invalid number: Warn the user if an invalid number such as 0 or 11 is entered into the board
# Using 131.05.Easy.json, use B2 as a cell. Put 11 as a number.
# (This is an Error State)

# Expected Output: "ERROR: The value 11 is invalid"

# 5: Square already filled: Warn the user if the selected square already has a number
# Using 131.05.Easy.json, use A1 as a cell.
# (This is an Error State)

# Expected Output: "ERROR: Square A1 is filled"

# 6: Unique Row: Recognize if the user's number is already present on the selected row
# Using 131.05.Easy.json, use G2 as a cell and input 5.
# (This is a Boundary Condition)

# Expected Output: "ERROR: The value 5 already exists in the row"

# 7: Unique Column: Recognize if the user's number is already present on the selected column
# Using 131.05.Easy.json, use H5 as a cell and input 4.
# (This is a Boundary Condition)

# Expected Output: "ERROR: The value 4 already exists in the column"

# 8: Unique Inside Square: Recognize if the user's number is already present on the selected inside square
# Using 131.05.Easy.json, use H2 as a cell and input 9.
# (This is a Boundary Condition)

# Expected Output: "ERROR: The value 9 already exists in the box"