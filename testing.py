import riceutils as utils
import json
import os
import webbrowser

def main():
    result = utils.traverse_directories(os.getcwd(), allFiles=[], writeToFile=True, exceptions = [".git", "__pycache__", "Example use cases"])


if __name__ == "__main__":
    main()