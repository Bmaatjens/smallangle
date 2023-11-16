import click
import numpy as np
from numpy import pi
import pandas as pd
import click

@click.group()
def function():
    pass

@function.command("sine")
@click.option(
    '-n',
    '--number',
    default = 1
)

def sin(number):
    """the number you put in, the sine function acts

    Args:
        number (float): any value except for infinity
    
    Returns: 
        output value coming from sine function with input value
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@function.command("tan")
@click.option(  
    '-n',
    '--number',
    default = 1
)

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


if __name__ == "__main__":
    function()