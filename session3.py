#исключения

def bvbuirbv():
    pass
# try:
#     delimiter = int(input("Type some number: "))
#     print(10/delimiter)
# except ZeroDivisionError, ValueError:
#     print("error")

def come_function():
    try:
        number = int(input("Type some number: "))
        if number == 0:
            raise ZeroDivisionError("loser")
        print(10/number)
    except ValueError as e:
        print(f"That's not a number {e}")
    except ZeroDivisionError as e:
        print(f"you cant divide by zero {e}")
        return 1
    else:
        print("validation successfully completed")
    finally:
        print("program is finished")

#print(int("abc"))
come_function()