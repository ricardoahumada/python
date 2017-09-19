def somefunction():
    print("some cleaning")


a = 10
b = 0
result = None

try:
    result = a / b
    print(result)

except Exception:           # Output ->
    somefunction()          # some cleaning
    raise                   # Traceback (most recent call last):
                            # File "python", line 8, in <module>
                            # ZeroDivisionError: division by zero
