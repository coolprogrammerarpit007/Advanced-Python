def my_decorator(func):
    def wrapper(*args):
        print("Hello, Thankyou for using our function ")
        result = func(*args)
        print("I hope it was nice experience using Us.")
        return  result

    return wrapper


@my_decorator
def add_numbers(*args):
    total = 0

    for number in args:
        total += number

    return f"Total Sum Is: {total}"

print(add_numbers(7,8,9,85,74,52,14,25,63,78,17,96))
print("Function run completed successfully.")