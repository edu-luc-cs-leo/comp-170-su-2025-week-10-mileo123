# RECURIVE SUM OF DIGITS


def sum_of_digits(n: int, base: int = 10) -> int:
    """Computes the sum of digits for a given number in a given number
    base system. The default number base is 10.
    """
    # Base case, number is less than number base and there is nothing
    # to add. The sum of digits of this number is the number itself.
    if n < base:
        result = n
    else:
        # Obtain the last digit of the number
        last_digit = n % base
        # Remove the last digit from the input
        new_input = n // base
        # recurse with the new data
        result = last_digit + sum_of_digits(new_input)
    return result
    # end method sum_of_digits


# Quick test for sum_of_digits
print("\nTesting sum_of_digits")
print(sum_of_digits(4444))  # expect 16
print(sum_of_digits(1234))  # expect 10


# CODE OPTIMIZATION
# The method above is a bit verbose, for illustrative purposes. It can be
# optimized a bit as follows, because there is no need to define separate
# variables for last_digit and new_input. These values are use only once
# in the code. We assign values to variables when we expect to use them
# in multiple places or when we wish our code to be very illustrative.
#
def sum_of_digits_opt1(n: int, base: int = 10) -> int:
    """Computes the sum of digits for a given number in a given number
    base system. The default number base is 10.
    """
    # Base case, number is less than number base and there is nothing
    # to add. The sum of digits of this number is the number itself.
    if n < base:
        result = n
    else:
        result = (n % base) + sum_of_digits_opt1(n // base)
    return result
    # end method sum_of_digits_opt1


# Quick test for sum_of_digits_opt1
print("\nTesting sum_of_digits_opt1")
print(sum_of_digits_opt1(4444))  # expect 16
print(sum_of_digits_opt1(1234))  # expect 10


# MORE CODE OPTIMIZATION
# The method above can be refined further by the use of the ternary
# operator in the return statement.
#
def sum_of_digits_opt2(n: int, base: int = 10) -> int:
    """Computes the sum of digits for a given number in a given number
    base system. The default number base is 10.
    """
    return n if n < base else (n % base) + sum_of_digits_opt2(n // base)


# Quick test for sum_of_digits_opt2
print("\nTesting sum_of_digits_opt2")
print(sum_of_digits_opt2(4444))  # expect 16
print(sum_of_digits_opt2(1234))  # expect 10


# COUNT OCCURRENCES


def count_occurrences(source: list[int], target: int) -> int:
    """Counts how many time a target value appears in a given list."""
    if source:
        # Input list is not empty. Process its first element at
        # position [0] and then recurse with the remain list [1:...]
        occurrence = 0
        if source[0] == target:
            occurrence = 1
        result = occurrence + count_occurrences(source[1:], target)
    else:
        # input list is empty
        result = 0
    return result
    # end method count_occurrences


# Quick test for count_occurrences
print("\nTesting count_occurrences")
print(count_occurrences([1, 2, 3, 1, 4, 1], 1))  # returns 3
print(count_occurrences([1, 2, 3, 1, 4, 1], 5))  # returns 0
print(count_occurrences(None, 1))  # returns 0
print(count_occurrences([], 1))  # returns 0


# CODE OPTIMIZATION
# Method count_occurences above is a quite verbose, for illustragive
# purposes. A more compact version is given below.
#
def count_occurrences_opt1(source: list[int], target: int) -> int:
    """Counts how many time a target value appears in a given list."""
    if source:
        # Input list is not empty. Process its first element at
        # position [0] and then recurse with the remain list [1:...]
        occurrence = 0 if source[0] == target else 1
        result = occurrence + count_occurrences(source[1:], target)
    else:
        # input list is empty
        result = 0
    return result
    # end method count_occurrences_opt1


# MORE CODE OPTIMIZATION
# Here's an even more compact version with one statement only
# (a return statement spread over multiple lines for readability)
#
def count_occurrences_opt2(source: list[int], target: int) -> int:
    """Counts how many time a target value appears in a given list."""
    return (
        0
        if not source
        else (
            (1 if source[0] == target else 0)
            + count_occurrences_opt2(source[1:], target)
        )
    )
    # end method count_occurrences_opt2


# CONVERT THE FOLLOWING METHOD TO ITERATIVE


def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result
    # end method factorial


def factorial_iterative(n: int) -> int:
    """Iterative computation of n!"""
    # We are going to compute a product, so the initial value of the
    # accumulating variable is 1
    product = 1  # 0!
    # now compute (n-1) with a loop up to and not including n
    for i in range(1, n):
        product *= i
    # Done, n! = n * (n-1)!
    return n * product
    # end method factorial_iterative


# Quick test
print("\nTesting iterative factorial")
print(factorial(10) == factorial_iterative(10))  # expect True


# CODE OPTIMIZATION
# We can write a more robust version of the method
#
def factorial_iterative_opt1(n: int) -> int:
    product = 1
    for i in range(1, n + 1):
        product *= 1
    return product


# CONVERT THE FOLLOWING METHOD TO ITERATIVE


def fibonacci(n):
    if n == 0 or n == 1:
        result = n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    return result
    # end method fibonacci


def fibonacci_iterative(n: int) -> int:
    """Iterative implementation of Fibonacci's number"""
    if n == 0 or n == 1:
        # Trivial case -- by definition F(0)=0 and F(1)=1
        result = n
    else:
        # We initialize two variables with the trivial cases
        prev = 1
        prev_prev = 0
        # Iterate up to n (inclusive)
        for i in range(2, n + 1):
            fib = prev + prev_prev
            prev_prev = prev
            prev = fib
        result = fib
    return result
    # end method fibonacci_iterative


print("\nTesting iterative fibonacci")
for n in range(11):
    print(fibonacci_iterative(n) == fibonacci(n))
