#Q.1 print helloworld
print("helloworld!!")

#Q.2 describe local variable and global variable code
    # local variable:
    #                  *local variable are those variable which are define within a function or block of code.
    #                  *These are only accessible within that function or block.
    #                   *These are not visible outside the function or block.
    #     Global variable:
    #                     *Global variable are those variable which are define the outside of any function or block.
    #                     *These are accessible from any function or block within the same module or script.

#Q.3 Write a code that describe Indentation error

"""  def example_function():
                print("This is correctly indented")
                    print("This line has incorrect indentation")  # IndentationError here
                 print("Back to correct indentation")
     print example_function()"""

#Q.4 write a code that describe local and global variable with same name?

  # Global variable
x = 10
def example_function():
        # Local variable with the same name as the global variable
     x = 5
     print("Inside the function, local x:", x)
example_function()

print("Outside the function, global x:", x)

#Q.5 Write a code for string, int and float input.
# Taking string input
string_input = input("Enter a string: ")

# Taking integer input
integer_input = int(input("Enter an integer: "))

# Taking float input
float_input = float(input("Enter a float: "))

print("You entered the string:", string_input)
print("You entered the integer:", integer_input)
print("You entered the float:", float_input)


