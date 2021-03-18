"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    # define a variable "sum"
    # set this variable as the sum of num1, num2. sum = num1+num2
    # return sum

    sum_nums = num1 + num2
    return sum_nums

def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    #def variable for subtract
    #set subtract variable to find difference between two numbers
    #return subtract variable

    difference = num1 - num2
    return difference


def multiply(num1, num2):
    """Multiply the two inputs together."""
    #define variable for result
    #save result of num1 multiplied by num2
    #return result

    product = num1 * num2
    return product

def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    #define function for divide
    #add quotient variable that divides num1 and num2
    #return quotient

    quotient = num1/num2
    return quotient


def square(num1):
    """Return the square of the input."""
    #define variable for square
    #save result of squaring to the variable
    #return result [squared]

    squared = num1 ** 2
    return squared 

def cube(num1):
    """Return the cube of the input."""

    #define variable for a cube
    #take num1 to the third power
    #return the cube variable

    is_cubed = num1 ** 3
    return is_cubed


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    #define variable for result
    #save result of num1 raised to num2 into result
    #return result

    exponent_result = num1 ** num2
    return exponent_result

def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    #define remainder variable
    #capturn remainder when num1 / num2
    #return remainder variable

    remainder = num1 % num2
    return remainder


# define function add_mult with 3 parameters
# add num1 and num2, multiply the result with num3
# return the final result

def add_mult(num1, num2, num3):
    """ Return the sum of num 1 + num2 multiplied by num3"""
    equation = (num1 + num2) * num3
    return equation 

#define function add_cubes with 2 parameters
#define vaiable that takes the cubes of num1 and num2 and adds them together
#return the sum of the cubes save in that variable

def add_cubes(num1, num2) :
    """ Return the sum of cubes."""
    sum_cubes = (num1**3) + (num2**3)
    return sum_cubes