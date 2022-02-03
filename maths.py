import math

def pythab(a,b): # pythagoras using sides a and b
    try:
        return math.sqrt(a**2 + b**2)
    except:
        return -1

def pythac(a,c): # pythagoras with the hypotenuse
    try:
        return math.sqrt(c**2 - a**2)
    except:
        return -1

def root(a,b): # a is the number b is the root
    try:
        return (a**(1/b))
    except:
        return -1

def soh(sine=0, oposite=0, hypotenuse=0): # input of sine must be in radians for the correct result to be outputed
    if sine == 0:
        return math.asin(oposite/hypotenuse)
    elif oposite == 0:
        return math.sin(sine)*hypotenuse
    elif hypotenuse == 0:
        return oposite/math.sin(sine)
    else:
        return -1

def cah(cosine=0, adjacent=0, hypotenuse=0): # input of sine must be in radians for the correct result to be outputed
    if cosine == 0:
        return math.acos(adjacent/hypotenuse)
    elif adjacent == 0:
        return math.cos(cosine)*hypotenuse
    elif hypotenuse == 0:
        return adjacent/math.cos(cosine)
    else:
        return -1

def toa(tangent=0, oposite=0, adjacent=0): # input of sine must be in radians for the correct result to be outputed
    if tangent == 0:
        return math.atan(oposite/adjacent)
    elif oposite == 0:
        return math.tan(tangent)*adjacent
    elif adjacent == 0:
        return oposite/math.tan(tangent)
    else:
        return -1