import click
import numpy as np
from numpy import pi
import pandas as pd
import click

# ensures that you can use multiple commands for different functions

@click.group()
def function():
    pass

# name that needs to be called upon in terminal to run

@function.command("sine")

# the input value can be given after typing either one of the strings

@click.option(
    '-n',
    '--number',
    default = 1
)

# a sine function working with an input value

def sin(number):
    """the number you put in, the sine function acts upon

    Args:
        number (float): any value except for infinity
    
    Returns: 
        output value coming from sine function with input value
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

# name that needs to be called upon in terminal to run

@function.command("tan")

# the input value can be given after typing either one of the strings

@click.option(  
    '-n',
    '--number',
    default = 1
)

# a tan function working with an input value

def tan(number):
    """the number you put in, the tan function acts upon

    Args:
        number (float): any value except for infinity
    
    Returns: 
        output value coming from tan function with input value
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

# if you call upon the name of either named function, this makes sure the function will run

if __name__ == "__main__":
    function()