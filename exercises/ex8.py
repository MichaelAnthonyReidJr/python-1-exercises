import math

def f_to_c(fahrenheit):
    celsius = math.floor((fahrenheit - 32) * 5 / 9)
    return f"{fahrenheit} degrees Fahrenheit is {celsius} degrees Celcius."


def c_to_f(celsius):
    fahrenheit = math.floor(celsius * 9 / 5) + 32
    return f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit."







