import riceutils as utils # import the custom module

def main():
    a, b, B= 8, 10, 0.896 # sides a and b make up a triangle. Angle B is adjacent to side b and is in radians

    utils.clear() # custom clear module

    print(f"\n\n\na:{a}, b:{b}, are sides of a triangle, B:{B} is an angle in radians")
    print(f"The hypotenuse of the triangle is {utils.pythab(a,b)}") # does pythagoras with a, b
    print(f"The angle oposite a is {utils.toa(oposite=a, adjacent=b)}") # will output in radians
    print(f"Another way to work out the hypotenuse is using angle B {utils.cah(adjacent=a, cosine=B)}") # works out the hypotenuse using angle B

if __name__ == "__main__":
    main()