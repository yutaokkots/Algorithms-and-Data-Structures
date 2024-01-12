'''
given a floating point number ('t') that must be written out to a certain decimal place ('precision') 
and fit inside a width, ('width'), correctly format the input number. 

str.format(*args, **kwargs)

{:^}   ............ centers the value
{width}  .......... placeholder for the width value
.{precision}f ..... specifies the number of decimal places in the output & formatting a floating point number. 
f   ............... indicates formatting a floating point number. 

Therefore:
    '{:^{}.{}f}'.format(t,width,precision)
    ^ string   ^        ^
     ^        ^         ^the first *arg, 't', is surrounded by {},
      ^^                 is centered, using {:^X} this annotation,
        ^^               by the second *arg,'width' ({:^{}})
          ^^^            with a precision (decimal place) defined by the third *arg, 'precision'
             ^           where the 'f' specifies it is a floating point number
                         {:^{}.{}f}

'''
t = 3.14159
precision = 3
width = 20

print('{}'.format(t))
# 3.14159

print('{:.{}f}'.format(t,precision))
# 3.142

print('{:^40.{}f}'.format(t,precision), "<<<")
#                  3.142                   <<<

print('{:>{}.{}f}'.format(t,width,4), "<<<")
#               3.1416 <<<

print('{:<{}.{}f}'.format(t,width,2), "<<<")
# 3.14                 <<<

ex1 = {
    "t": 3.1415,
    "width": 10,
    "precision": 2
}
ex2 = {
    "t": 29.8245,
    "width": 10,
    "precision": 0
}
ex2 = {
    "t": 837.28472,
    "width": 20,
    "precision": 7
}

def solution1(t, width, precision):
    return '{:^{}.{}f}'.format(t,width,precision)

def solution2(t, width, precision):
    return '{:^{width}.{precision}f}'.format(t,width=width,precision=precision)

ans1 = solution1(ex1["t"], ex1["width"], ex1["precision"])
print(f">>>{ans1}<<<")
## >>>   3.14   <<<

ans1 = solution2(ex2["t"], ex2["width"], ex2["precision"])
print(f">>>{ans1}<<<")
## >>>    837.2847200     <<<

'''
example 1:
    t: 3.1415
    width: 10
    precision: 2
    output: "   3.14   "

example 2:
    t: 29.8245
    width: 10
    precision: 0
    output: "    30    "

example 3:
    t: 837.28472
    width: 20
    precision: 7
    output: "    837.2847200     "
'''
