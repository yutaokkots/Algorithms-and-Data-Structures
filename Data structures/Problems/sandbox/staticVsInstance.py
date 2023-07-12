## an exercise to create a class and use static and instance methods

## create a class for converting temperatures among Kelvin, Fahrenheit, and Celsius

class Temp():
    @staticmethod
    def f_to_c(f_temp):
        return (f_temp - 32) / (5/9)
    
    @staticmethod
    def c_to_f(c_temp):
        return c_temp * (9/5) + 32



print(Temp.f_to_c(0))
print(Temp.c_to_f(0))