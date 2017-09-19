# raise exception (args)

try:
    raise ValueError("I have raised an Exception")
except ValueError as exp:
    print("Error", exp)  # Output -> Error I have raised an Exception


# raise execption
try:
    raise ValueError
except ValueError as exp:
    print("Error", exp)     # Output -> Error
