# this file also references the main_.py file in the same directory

def this_function(a, b):
    product = a * b
    print(f"this_function is found in the module_.py file. \nthe calculation of {a} * {b} = {product}")
    return product

def another_function():
    print("another_function(): True")
    return True

if __name__ == "__main__":
    print("running via module_.py directly.")

print("this print statement will run both when \n1) importing this file into 'main_.py' and running it; and \n2) running this file ('module_.py') directly.")