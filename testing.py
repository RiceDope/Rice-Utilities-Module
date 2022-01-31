from unicodedata import name
import riceutils as utils
import json
import os




def main():
    name = frozenset({"apple", "banana", "cherry"})
    print(f"The variable name is type: {utils.type_comparison(name)}")
if __name__ == "__main__":
    main()