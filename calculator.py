"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cubes)


# Replace this with your code


#get the user input
#if input == q, exit loop 
#tokenize the input
#check if operand equals a certain value
#pass the numbers through the equation that the operand suggests
#assign the eqaution to a variable and print the variable

#accept user input


while True:
    user_expression = input("Enter your equation!")
    if user_expression != "q":
        tokenized_input = user_expression.split(' ')

        for i in range(1, len(tokenized_input)): 
            tokenized_input[i] = int(tokenized_input[i]) 
        
        if tokenized_input[0] == "+":
            result = add(tokenized_input[1],tokenized_input[2])

        elif tokenized_input[0] == "-":
            result = subtract(tokenized_input[1],tokenized_input[2])

        elif tokenized_input[0] == "*":
            result = multiply(tokenized_input[1],tokenized_input[2])   

        elif tokenized_input[0] == "/":
            result = divide(tokenized_input[1],tokenized_input[2])    

        elif tokenized_input[0] == "square":
            result = square(tokenized_input[1]) 

        elif tokenized_input[0] == "cube":
            result = cube(tokenized_input[1]) 

        elif tokenized_input[0] == "pow":
            result = power(tokenized_input[1],tokenized_input[2]) 

        elif tokenized_input[0] == "mod":
            result = mod(tokenized_input[1],tokenized_input[2])       

        elif tokenized_input[0] == "x+":
            result = add_mult(tokenized_input[1],tokenized_input[2],tokenized_input[3])  

        elif tokenized_input[0] == "cubes+":
            result = add_cubes(tokenized_input[1],tokenized_input[2])    
        
    elif user_expression =="q":
        break
            
    print (result)

