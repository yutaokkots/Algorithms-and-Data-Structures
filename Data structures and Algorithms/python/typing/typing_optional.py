"""Optional typing in Python."""

"""
See Union typing. 

Comparative statements:

def func(a:Optional[int]=None) -> int:
    return a

and

def func(a:Union[int, None]) -> int:
    return a


"""
from typing import Optional, Union

# temperatures in kelvin
conversion = 273.15
c_temp1 = 0
c_temp2 = 18
c_temp3 = 34.5

f_temp1 = 88
f_temp2 = 31.4
f_temp3 = 115.2

# Union[bool, None]

def celsius_fahrenheit_conv(temp:float, c_to_f:Optional[bool]=True) -> float:
    if not c_to_f:
        temp_c = round((temp - 32) * (5/9),2)
        print(f"Converted {temp}°F to {temp_c}°C")
        return temp_c
    temp_f = round(temp * (9/5) + 32, 2)
    print(f"Converted {temp}°C to {temp_f}°F")
    return temp_f

a1 = celsius_fahrenheit_conv(c_temp1)
a2 = celsius_fahrenheit_conv(c_temp2, c_to_f=True)
a3 = celsius_fahrenheit_conv(c_temp3)
b1 = celsius_fahrenheit_conv(f_temp1, c_to_f=False)
b2 = celsius_fahrenheit_conv(f_temp2, c_to_f=False)
b3 = celsius_fahrenheit_conv(f_temp3, c_to_f=False)

def fahrenheit_celsius_conv(temp:float, f_to_c:Union[bool, None]=True) -> float:
    if not f_to_c:
        temp_f = round(temp * (9/5) + 32, 2)
        print(f"Converted {temp}°C to {temp_f}°F")
        return temp_f
    temp_c = round((temp - 32) * (5/9),2)
    print(f"Converted {temp}°F to {temp_c}°C")
    return temp_c

a1 = fahrenheit_celsius_conv(f_temp1)
b1 = fahrenheit_celsius_conv(c_temp1, f_to_c=False)