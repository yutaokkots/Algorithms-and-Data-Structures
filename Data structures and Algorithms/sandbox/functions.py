def cycle(*values):
    index = 0

    def get_next():
        nonlocal index
        current_value = values[index]
        index = (index + 1) % len(values)
        return current_value

    return get_next

on_off = cycle('red', 'green', 'blue' )

print(on_off()) #red
print(on_off()) #green
print(on_off()) #blue
print(on_off()) #red

def outer_function ():
    foo = 6
    def inner_function():
        nonlocal foo
        foo += 3
        print("inner function: ", foo)
    inner_function()
    return inner_function

function_call = outer_function()

function_call()
function_call()
function_call()
function_call()

